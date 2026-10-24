from conftest import login


def test_anonymous_cannot_download_private_document(client, app):
    response = client.get(f"/documents/{app.config['TEST_DOC_ID']}/download")
    assert response.status_code in (302, 401)


def test_other_owner_cannot_view_or_download_document(client, app):
    login(client, "bob@example.test", "BobStrongPassword123!")
    doc_id = app.config["TEST_DOC_ID"]
    assert client.get(f"/documents/{doc_id}").status_code == 403
    assert client.get(f"/documents/{doc_id}/download").status_code == 403


def test_ungranted_viewer_cannot_read_or_download(client, app):
    login(client, "charlie@example.test", "CharlieStrongPassword123!")
    doc_id = app.config["TEST_DOC_ID"]
    assert client.get(f"/documents/{doc_id}").status_code == 403
    assert client.get(f"/documents/{doc_id}/download").status_code == 403


def test_read_grant_allows_download_but_not_edit(client, app):
    from app import db, Permission
    with app.app_context():
        grant = Permission(document_id=app.config["TEST_DOC_ID"],
                           user_id=app.config["TEST_USERS"]["viewer"], level="read",
                           granted_by=app.config["TEST_USERS"]["alice"])
        db.session.add(grant)
        db.session.commit()
    login(client, "charlie@example.test", "CharlieStrongPassword123!")
    doc_id = app.config["TEST_DOC_ID"]
    response = client.get(f"/documents/{doc_id}/download")
    assert response.status_code == 200
    assert response.data == b"secret"
    assert client.get(f"/documents/{doc_id}/edit").status_code == 403


def test_revocation_blocks_later_download(client, app):
    from app import db, Permission
    from datetime import datetime, timezone
    with app.app_context():
        grant = Permission(document_id=app.config["TEST_DOC_ID"],
                           user_id=app.config["TEST_USERS"]["viewer"], level="read",
                           granted_by=app.config["TEST_USERS"]["alice"])
        db.session.add(grant)
        db.session.commit()
        grant.revoked_at = datetime.now(timezone.utc)
        db.session.commit()
    login(client, "charlie@example.test", "CharlieStrongPassword123!")
    assert client.get(f"/documents/{app.config['TEST_DOC_ID']}/download").status_code == 403


def test_owner_cannot_be_impersonated_by_document_id(client, app):
    login(client, "bob@example.test", "BobStrongPassword123!")
    doc_id = app.config["TEST_DOC_ID"]
    response = client.post(f"/documents/{doc_id}/delete", follow_redirects=False)
    assert response.status_code == 403
    from app import db, Document
    with app.app_context():
        doc = db.session.get(Document, doc_id)
        assert doc.deleted_at is None


def test_public_registration_cannot_create_admin(client):
    response = client.post("/register", data={
        "full_name": "Mallory", "email": "mallory@example.test",
        "password": "MalloryPassword123!", "role": "admin"
    }, follow_redirects=True)
    assert response.status_code == 200
    from app import db, User
    with client.application.app_context():
        user = User.query.filter_by(email="mallory@example.test").first()
        assert user is not None
        assert user.role == "viewer"


def test_admin_cannot_download_document_without_explicit_grant(client, app):
    login(client, "dana@example.test", "DanaStrongPassword123!")
    assert client.get(f"/documents/{app.config['TEST_DOC_ID']}/download").status_code == 403


def test_editor_cannot_delete_owner_document(client, app):
    from app import db, Permission, Document
    login(client, "alice@example.test", "AliceStrongPassword123!")
    with app.app_context():
        grant = Permission(document_id=app.config["TEST_DOC_ID"],
                           user_id=app.config["TEST_USERS"]["bob"], level="edit",
                           granted_by=app.config["TEST_USERS"]["alice"])
        db.session.add(grant)
        db.session.commit()
    client.post("/logout")
    login(client, "bob@example.test", "BobStrongPassword123!")
    response = client.post(f"/documents/{app.config['TEST_DOC_ID']}/delete")
    assert response.status_code == 403
    with app.app_context():
        doc = db.session.get(Document, app.config["TEST_DOC_ID"])
        assert doc.deleted_at is None

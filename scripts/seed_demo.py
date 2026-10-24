"""Create synthetic demo accounts. Run: python scripts/seed_demo.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import app, db, User

ACCOUNTS = [
    ("Demo Admin", "admin@trustvault.local", "DemoAdminPassword!2026", "admin"),
    ("Demo Owner", "owner@trustvault.local", "DemoOwnerPassword!2026", "owner"),
    ("Demo Viewer", "viewer@trustvault.local", "DemoViewerPassword!2026", "viewer"),
]

with app.app_context():
    for name, email, password, role in ACCOUNTS:
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(full_name=name, email=email, role=role)
            user.set_password(password)
            db.session.add(user)
    db.session.commit()
    print("Demo accounts created. Use synthetic documents only.")
    for _, email, password, role in ACCOUNTS:
        print(f"{role}: {email} / {password}")

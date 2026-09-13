import os
from app import db, User, app

with app.app_context():
    # สร้าง Admin คนแรก
    admin = User(username="admin1", role="admin")
    admin.set_password(os.environ["ADMIN_INITIAL_PASSWORD"])

    # สร้าง User ตัวอย่าง
    user = User(username="user1", role="user")
    user.set_password(os.environ["USER_INITIAL_PASSWORD"])

    # เพิ่มลง session
    db.session.add(admin)
    db.session.add(user)

    # บันทึกลง DB
    db.session.commit()

    print("Admin และ User ตัวอย่างสร้างเรียบร้อยแล้ว!")

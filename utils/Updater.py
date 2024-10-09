# utils/updater.py
import os
import subprocess

def update_bot():
    # أوامر لجلب التحديثات من مستودع GitHub
    try:
        # تأكد من تحديث المستودع
        subprocess.run(["git", "pull"], check=True)
        print("تم جلب التحديثات بنجاح!")
    except Exception as e:
        print("حدث خطأ أثناء جلب التحديثات:", str(e))

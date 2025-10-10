# ai_integration_demo.py

# استيراد الدالة من ملف ta_corrector.py
from ta_corrector import apply_semantic_ta_correction

def run_tests():
    print("--- اختبارات القاعدة الدلالية للتاء المفتوحة ---")
    
    # يجب أن تستخدم النصوص التي تتوافق مع "قرينة_التعيين" في ملف CSV
    
    # 1. اختبار التعيين النحوي الصريح (امرأة نوح)
    text1 = "لقد ضرب الله مثلاً امرأة نوح"
    result1 = apply_semantic_ta_correction(text1)
    print(f"\n[التعيين النحوي] النص الأصلي: {text1}")
    print(f"النص المصحح: {result1}") # النتيجة المتوقعة: امرأت

    # 2. اختبار التعيين بالوصف السابق (جنة نعيم)
    text2 = "فروح وريحان و جنة نعيم"
    result2 = apply_semantic_ta_correction(text2)
    print(f"\n[التعيين بالوصف] النص الأصلي: {text2}")
    print(f"النص المصحح: {result2}") # النتيجة المتوقعة: جنت

    # 3. اختبار التعيين بالحدث (نعمة الألفة)
    text3 = "اذكروا نعمة الله عليكم اذ كنتم اعداء"
    result3 = apply_semantic_ta_correction(text3)
    print(f"\n[التعيين بالفعل/الحدث] النص الأصلي: {text3}")
    print(f"النص المصحح: {result3}") # النتيجة المتوقعة: نعمت (بسبب كلمة اعداء)
    
    # 4. اختبار التعيين بالشخص (رحمة زكريا)
    text4 = "ذكر رحمة ربك عبده زكريا"
    result4 = apply_semantic_ta_correction(text4)
    print(f"\n[التعيين بالشخص] النص الأصلي: {text4}")
    print(f"النص المصحح: {result4}") # النتيجة المتوقعة: رحمت

    # 5. اختبار العموم (يجب أن تبقى مربوطة)
    text5 = "ان رحمت الله قريب من المحسنين"
    result5 = apply_semantic_ta_correction(text5)
    print(f"\n[العموم والإبهام] النص الأصلي: {text5}")
    print(f"النص المصحح: {result5}") # النتيجة المتوقعة: رحمة
    
# تشغيل الاختبارات
if __name__ == "__main__":
    run_tests()

# ai_integration_demo.py

# استيراد الدالة من ملف ta_corrector.py
from ta_corrector import apply_semantic_ta_correction

def run_tests():
    print("--- اختبارات القاعدة الدلالية للتاء المفتوحة ---")
    
    # 1. اختبار التعيين النحوي الصريح (الآلية 1: امرأت نوح)
    text1 = "لقد ضرب الله مثلاً امرأة نوح"
    result1 = apply_semantic_ta_correction(text1)
    print(f"\n[التعيين النحوي] النص الأصلي: {text1}")
    print(f"النص المصحح: {result1}")
    
    # 2. اختبار التعيين بالوصف السابق (الآلية 2: جنت نعيم)
    text2 = "فروح وريحان و جنة نعيم"
    result2 = apply_semantic_ta_correction(text2)
    print(f"\n[التعيين بالوصف] النص الأصلي: {text2}")
    print(f"النص المصحح: {result2}")
    
    # 3. اختبار التعيين بالفعل (الآلية 3: نعمت الله)
    text3 = "وان تعدوا نعمة الله لا تحصوها"
    result3 = apply_semantic_ta_correction(text3)
    print(f"\n[التعيين بالفعل] النص الأصلي: {text3}")
    print(f"النص المصحح: {result3}")

    # 4. اختبار التعيين بالرجاء (الآلية 3: رحمت الله)
    text4 = "اولئك يرجون رحمة الله"
    result4 = apply_semantic_ta_correction(text4)
    print(f"\n[التعيين بالفعل] النص الأصلي: {text4}")
    print(f"النص المصحح: {result4}")

    # 5. اختبار عدم التعيين (التاء المربوطة)
    text5 = "وجدت امراة تملكهم"
    result5 = apply_semantic_ta_correction(text5)
    print(f"\n[العموم والإبهام] النص الأصلي: {text5}")
    print(f"النص المصحح: {result5}")
    
# تشغيل الاختبارات
if __name__ == "__main__":
    run_tests()

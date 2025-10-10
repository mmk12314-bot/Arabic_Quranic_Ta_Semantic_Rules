# ai_integration_demo.py

# استيراد الدالة من ملف ta_corrector.py
from ta_corrector import apply_semantic_ta_correction

def run_tests():
    print("--- اختبارات القاعدة الدلالية للتاء المفتوحة ---")
    
    # 1. اختبار التعيين النحوي الصريح (امرأة نوح)
    # القرينة في CSV: نوح
    text1 = "لقد ضرب الله مثلاً امرأة نوح"
    result1 = apply_semantic_ta_correction(text1)
    print(f"\n[التعيين النحوي] النص الأصلي: {text1}")
    print(f"النص المصحح: {result1}") 

    # 2. اختبار التعيين بالوصف السابق (جنة نعيم)
    # القرينة في CSV: روح
    text2 = "فروح وريحان و جنة نعيم"
    result2 = apply_semantic_ta_correction(text2)
    print(f"\n[التعيين بالوصف] النص الأصلي: {text2}")
    print(f"النص المصحح: {result2}") 

    # 3. اختبار التعيين بالحدث (نعمة الألفة)
    # القرينة في CSV: اعداء
    text3 = "اذكروا نعمة الله عليكم اذ كنتم اعداء"
    result3 = apply_semantic_ta_correction(text3)
    print(f"\n[التعيين بالفعل/الحدث] النص الأصلي: {text3}")
    print(f"النص المصحح: {result3}") 
    
    # 4. اختبار التعيين بالشخص (رحمة زكريا)
    # القرينة في CSV: زكريا
    text4 = "ذكر رحمة ربك عبده زكريا"
    result4 = apply_semantic_ta_correction(text4)
    print(f"\n[التعيين بالشخص] النص الأصلي: {text4}")
    print(f"النص المصحح: {result4}") 

    # 5. اختبار العموم (رحمة الأعراف)
    # القرينة في CSV: قريب (وهو لا يسبب التعيين القاطع هنا)
    text5 = "ان رحمت الله قريب من المحسنين"
    result5 = apply_semantic_ta_correction(text5)
    print(f"\n[العموم والإبهام] النص الأصلي: {text5}")
    print(f"النص المصحح: {result5}") 
    
# تشغيل الاختبارات
if __name__ == "__main__":
    run_tests()

import re

# --- دالة تنقية اللغة العربية (لإزالة التشكيل وضمان المقارنة) ---

def normalize_arabic(text):
    """
    تنقية النص العربي من الحركات والتشكيل والرموز الزائدة لضمان تطابق المقارنة.
    """
    if not text:
        return ""
    
    # إزالة جميع الحركات والتشكيل
    text = re.sub(r'[\u064b-\u065f]', '', text) 
    # توحيد أشكال الألف والياء
    text = re.sub("[إأآ]", "ا", text)
    text = re.sub("ى", "ي", text)
    # إزالة أي شيء ليس حرفاً عربياً أو مسافة
    text = re.sub(r'[^\w\s]', '', text) 
    return text.strip().lower()

# --- بيانات القاعدة (KNOWN_CLUES) ---
# القرائن يتم تنقيتها فوراً لضمان سرعة ودقة البحث
KNOWN_CLUES = {
    "رحمة": [normalize_arabic(c) for c in ["ربك", "يقسمون", "آتيناه", "عبده", "مباركة"]],
    "نعمة": [normalize_arabic(c) for c in ["الله", "تعدوا", "تذكرون", "عليكم", "بصيرة"]],
    "امرأة": [normalize_arabic(c) for c in ["نوح", "لوط", "فرعون", "عمران"]],
    "جنة": [normalize_arabic(c) for c in ["نعيم", "روح", "ريحان", "المأوى"]],
    "سنة": [normalize_arabic(c) for c in ["تبديلا", "تحويلا", "الأولين"]],
    "كلمة": [normalize_arabic(c) for c in ["ربك", "العذاب", "الحسنى"]]
}

# قائمة جذور الكلمات التي يحدث فيها التناوب (لضمان سرعة الفحص)
TA_ALTERNATING_WORD_ROOTS = [normalize_arabic(w.strip("ة")) for w in [
    "رحمة", "نعمة", "سنة", "لعنة", "امرأة", "معصية",
    "فطرة", "بقية", "كلمة", "شجرة", "قرة", "جنة",
    "آية", "بينة", "ثمرة", "غيابة", "جمالة"
]]


# --- دالة التصحيح الرئيسية (apply_pragmatic_ta_rule) ---

def apply_pragmatic_ta_rule(text: str) -> str:
    """
    يطبق قاعدة المعلوم/المجهول (التعيين البرغماتي) لتاء التأنيث.
    """
    # تنقية النص بالكامل قبل تقسيمه لضمان نظافة الكلمات
    words = normalize_arabic(text).split()
    
    corrected_words = []
    
    for i, word_clean in enumerate(words):
        
        current_root = word_clean.strip("تة") 
        
        if current_root in TA_ALTERNATING_WORD_ROOTS:
            
            is_designated = False 
            
            # العثور على مفتاح المعجم الأصلي
            word_key = next((k for k in KNOWN_CLUES.keys() if normalize_arabic(k.strip("ة")) == current_root), None)

            # --- آليات الكشف عن "القرينة المعلومة" (ت) ---
            
            if word_key:
                clues = KNOWN_CLUES[word_key] # القرائن منقاة مسبقاً وجاهزة للمقارنة
                
                start_index = max(0, i - 3)
                end_index = min(len(words), i + 4)
                
                for j in range(start_index, end_index):
                    if i != j:
                        context_word_clean = words[j] # كلمة السياق منقاة مسبقاً
                        
                        if context_word_clean in clues:
                            is_designated = True
                            break
            
            # 3. تطبيق القاعدة الجديدة
            if is_designated:
                corrected_words.append(current_root + "ت")
            else:
                corrected_words.append(current_root + "ة") 
        
        else:
            corrected_words.append(word_clean)

    return " ".join(corrected_words)

# ملاحظة: تم إزالة دالة run_tests من هنا لتبقى في ملف ai_integration_demo.py

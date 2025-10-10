# ta_corrector.py

import csv
import os

# ----------------------------------------------------------------------
# تحديد مكان ملف البيانات
# التعديل: نعود خطوة للخلف (..) للوصول إلى المجلد الرئيسي حيث يوجد ملف CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE_PATH = os.path.join(BASE_DIR, '..', 'جدول البيانات للقاعدة_الدلالية.csv') 
# ----------------------------------------------------------------------

# تحميل البيانات من ملف CSV
def load_semantic_data(file_path):
    """تحميل البيانات التدريبية من ملف CSV."""
    data = []
    try:
        # قراءة الملف باستخدام ترميز utf-8
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"خطأ: لم يتم العثور على ملف البيانات في المسار: {file_path}")
        return None
    except Exception as e:
        print(f"خطأ أثناء قراءة ملف البيانات: {e}")
        return None
    return data

# تحميل البيانات عند بدء تشغيل البرنامج
SEMATNIC_TA_DATA = load_semantic_data(DATA_FILE_PATH)

# قائمة الكلمات التي يحدث فيها التناوب (المستخلصة من البيانات)
if SEMATNIC_TA_DATA:
    TA_WORDS = list(set([d["الكلمة_الأصلية"] for d in SEMATNIC_TA_DATA]))
else:
    TA_WORDS = []

# قائمة بأسماء المعرفة أو الضمائر التي تُنشئ التعيين (لمنطق البحث)
DEFINITE_NOUNS = ["الله", "ربك", "الرسول", "نوح", "لوط", "فرعون", "عمران", "العزيز"]

# ----------------------------------------------------------------------

def apply_semantic_ta_correction(text: str) -> str:
    """
    يطبق طبقة التصحيح الدلالي لتاء التأنيث بالاعتماد على البيانات المحسنة.

    هذه الدالة تستخدم طريقة بحث بسيطة بناءً على القرائن الموثقة في ملف CSV.
    """
    if not SEMATNIC_TA_DATA:
        return text # في حالة فشل تحميل البيانات، نرجع النص الأصلي

    words = text.split()
    corrected_words = []

    for i, word in enumerate(words):
        # تجريد الكلمة من علامات الترقيم (للتسهيل)
        clean_word = word.strip("،.؛:").strip("ةت")
        
        # إذا لم تكن الكلمة من الكلمات التي يحدث فيها التناوب، نتركها كما هي
        if clean_word not in TA_WORDS:
            corrected_words.append(word)
            continue
        
        # 1. البحث عن أقرب تطابق في البيانات الموثقة 
        is_designated = False
        
        for entry in SEMATNIC_TA_DATA:
            # نتأكد أننا نبحث عن الكلمة الصحيحة وأنها مصنفة كـ "تعيين"
            if entry.get("الكلمة_الأصلية") == clean_word and entry.get("تصنيف_التاء") == "تعيين":
                
                designation_type = entry.get("نوع_التعيين", "")
                clue = entry.get("قرينة_التعيين", "").split()[0].strip() # نأخذ أول كلمة من القرينة
                
                if not clue or clue == 'لا': # إذا لم توجد قرينة للتعيين في البيانات
                    continue

                # أ) التعيين النحوي الصريح (القرينة هي كلمة تالية مباشرة)
                if designation_type in ["نحوي صريح", "تعيين بالاسم والنوع"]:
                    if i + 1 < len(words) and words[i+1].strip().strip(",").strip(".").startswith(clue):
                        is_designated = True
                        break
                
                # ب) التعيين بالفعل أو الوصف السياقي (القرينة هي فعل أو وصف سابق)
                elif designation_type in ["فعلي/ثبوت", "سياقي/حدثي", "نوعي/شخصي"]:
                    # نبحث في الكلمات الأربع السابقة (نافذة سياقية)
                    for j in range(max(0, i - 4), i):
                        if words[j].strip().strip(",").strip(".").startswith(clue):
                            is_designated = True
                            break
                    if is_designated:
                        break
        
        # 2. تطبيق التصحيح النهائي: تاء مفتوحة إذا تم التعيين، مربوطة إذا لا
        if is_designated:
            corrected_words.append(clean_word + "ت")
        else:
            corrected_words.append(clean_word + "ة")

    return " ".join(corrected_words)

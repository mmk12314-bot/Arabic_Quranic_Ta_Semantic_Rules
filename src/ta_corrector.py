# ta_corrector.py

import csv
import os

# ----------------------------------------------------------------------
# تحديد مكان ملف البيانات (الموجود في المجلد الرئيسي)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE_PATH = os.path.join(BASE_DIR, '..', 'جدول البيانات للقاعدة_الدلالية.csv') 
# ----------------------------------------------------------------------

# تحميل البيانات من ملف CSV
def load_semantic_data(file_path):
    """تحميل البيانات التدريبية من ملف CSV."""
    # ... (بقية دالة load_semantic_data كما أرسلتها سابقاً)
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
    """
    # ... (بقية دالة apply_semantic_ta_correction كما أرسلتها سابقاً)
    # لا داعي لإعادة كتابة الدالة كاملة إذا لم تتغير
    if not SEMATNIC_TA_DATA:
        return text 

    words = text.split()
    corrected_words = []

    for i, word in enumerate(words):
        clean_word = word.strip("،.؛:").strip("ةت")
        
        if clean_word not in TA_WORDS:
            corrected_words.append(word)
            continue
        
        is_designated = False
        
        for entry in SEMATNIC_TA_DATA:
            if entry.get("الكلمة_الأصلية") == clean_word and entry.get("تصنيف_التاء") == "تعيين":
                
                designation_type = entry.get("نوع_التعيين", "")
                clue = entry.get("قرينة_التعيين", "").split()[0].strip().lower()
                
                if not clue or clue == 'لا':
                    continue

                if designation_type in ["نحوي صريح", "تعيين بالاسم والنوع"]:
                    if i + 1 < len(words) and words[i+1].strip().strip(",").strip(".").lower().startswith(clue):
                        is_designated = True
                        break
                
                elif designation_type in ["فعلي/ثبوت", "سياقي/حدثي", "نوعي/شخصي"]:
                    for j in range(max(0, i - 4), i):
                        if words[j].strip().strip(",").strip(".").lower().startswith(clue):
                            is_designated = True
                            break
                    if is_designated:
                        break
        
        if is_designated:
            corrected_words.append(clean_word + "ت")
        else:
            corrected_words.append(clean_word + "ة")

    return " ".join(corrected_words)

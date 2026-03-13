import streamlit as st
import time

# Configuration
st.set_page_config(page_title="Fazza Jar Pro", page_icon="🤝", layout="wide")

# CSS UI Enhancement
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .main { background-color: #f8f9fa; }
    .stButton>button {
        background: linear-gradient(90deg, #8338EC 0%, #00AC73 100%);
        color: white; border-radius: 30px; border: none; padding: 15px 30px;
        font-size: 20px; font-weight: bold; width: 100%; box-shadow: 0 4px 15px rgba(131, 56, 236, 0.3);
    }
    .metric-box {
        background: white; padding: 20px; border-radius: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05); border-bottom: 5px solid #8338EC;
        text-align: center; margin-bottom: 20px;
    }
    .fazza-card {
        background: white; padding: 25px; border-radius: 25px;
        border-right: 12px solid #00AC73; box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    .badge {
        background: #FFD700; color: black; padding: 4px 12px;
        border-radius: 50px; font-size: 14px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# App Content
st.title("🤝 فزعة جار | Fazza Jar")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col2:
    st.markdown('<div class="metric-box">', unsafe_allow_html=True)
    st.write("✨ رصيد النخوة الشخصي")
    st.subheader("1,450 نقطة")
    st.markdown('<span class="badge">🥇 جار فزّاع ذهبي</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="metric-box">', unsafe_allow_html=True)
    st.write("💰 إجمالي توفير الحي")
    st.subheader("5,200 ريال")
    st.write("نحو استهلاك مستدام")
    st.markdown('</div>', unsafe_allow_html=True)

with col1:
    st.markdown('<div class="fazza-card">', unsafe_allow_html=True)
    st.subheader("ماذا ينقصك يا جار؟")
    service = st.selectbox("اختر نوع الفزعة المطلوبة:", 
                           ["-- اختر من القائمة --", "🚗 اشتراك سيارة (بطارية)", "🔨 دريل / أدوات صيانة", "🪜 سلم طويل", "📦 مساعدة في نقل أغراض"])
    
    if service != "-- اختر من القائمة --":
        if st.button("اطلب فزعة الآن"):
            with st.status("🧠 ذكاء الجوار يعمل الآن...", expanded=True) as status:
                st.write("تحليل النطاق الجغرافي (500 متر)...")
                time.sleep(1.5)
                st.write("مطابقة الطلب مع الجيران الموثقين...")
                time.sleep(1.5)
                status.update(label="✅ تم العثور على جار مستعد!", state="complete", expanded=False)
            
            st.balloons()
            st.markdown(f"""
                <div style="background-color: #e6fff4; padding: 20px; border-radius: 15px; margin-top: 20px;">
                    <h3 style="color: #00AC73;">أبشر بسعدك!</h3>
                    <p><b>الجار:</b> صالح بن محمد (موثق ✅)</p>
                    <p><b>المسافة:</b> 250 متر (شارع 15)</p>
                    <p><b>الحالة:</b> متاح الآن وجاهز للمساعدة</p>
                </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("فزعة جار - النموذج الأولي للعرض الفني (MVP) | 2026")

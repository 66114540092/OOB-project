import streamlit as st
import random

# รายชื่อคนในแต่ละประเทศแยกตามเพศ
people_by_country = {
    "ไทย": {
        "ชาย": ["Rain", "Bird", "Peun", "Heart", "Gun", "Night", "Noah", "Tle", "Green", "Arm", "Tod", "Pich", "Than", "Kong", "Ralf", "Nile", "Yod", "Farm", "Angpao", "Ray"],
        "หญิง": ["Torfun", "Pui", "Jean", "Pla", "Ink", "Bua", "Cin", "Pleon", "Maprang", "Paula", "Noon", "Jeab", "Bun", "Chanoi", "Kat", "Jam", "Roong", "Namcha", "Ploy", "Kaofang"]
    },
    "เวียดนาม": {
        "ชาย": ["Kieu Qui Viet", "Doan Dung", "Than Cong Trung", "Huynh Van Loc", "Luu Xuan Dat", "Minh Dinh Phuoc", "Thao Xuan Toan", "Vang Quang Sinh", "Chiem Van Toai", "Danh Qui Sang", "Kha Trong Bao", "Cong Xuan Phuoc", "Tram Trong Chinh", "Mach Huu Van", "On Huu Hoc", "Vu Anh Dung", "Kha Trong Bao", "Chau Dinh Hoc", "Thuy Duc Chinh", "Duong Van Tuan"],
        "หญิง": ["Vuong Chi Mai", "Do Bich Ha", "Cao Quynh Sa", "Lieu Bich Nhu", "Nguyen Van Phuong", "Le Ai Thi (Thy)", "Vu Thanh Van", "Vu Linh Duyen", "Nguyen Hanh Trang", "Tran Thuy Quynh", "An Diem Le", "Ngo Thuy Linh", "Quach Bich Quyen", "Giang Huyen Tran", "Huynh Hao Nhi", "Nguyen Bich Quan", "Le Le Chi", "Kim Phuong Tien", "Kim Thu Hang", "Lam Bich Diep"]
    },
    "กัมพูชา": {
        "ชาย": ["Ang Rachana", "Su Chakra", "Prum Chhaya", "Vang Vithu", "Soun Sokhom", "Chea Sopheaktra", "Lorn Montha", "Thith Bona", "Mon Narith", "Pen Vichet", "Im Sros", "Hoy Chann", "Uch Rasmey", "Neak Achariya", "Meang Achariya", "Chhan Sokhom", "Mean Pheakdei", "Dith Chanthou", "Keo Noreaksey", "Long Rithy"],
        "หญิง": ["Loun Chaya", "Pen Chakriya", "Yim Sotear", "Song Roumduol", "Jey Sinuon", "Heang Taevy", "Chen Chivy", "Chhem Soriya", "Yos Soriya", "Meang Mony", "Eam Rachana", "Tat Chanlina", "Seng Theary", "Saluk Chanthou", "On Sotearith", "Moul Sokhanya", "Jin Soportevy", "Prum Soriya", "Muy Visna", "Khun Chamroeun"]
    },
    "สิงคโปร์": {
        "ชาย": ["Jiang Yong Zu", "Chee Wen Ming", "Tan De Kang", "Yung Yong Rui", "Lam Yi Hao", "Chong Ming De", "Eng Yong Hui", "Fan Yi Ming", "Lau Seng Hee", "Fang Zheng Min", "Phoon Jia Sheng", "Deng Yi De", "Cheong Jun Feng", "Phoon Yong Rui", "Lee Zi Rui", "Fang Kai Feng", "Li Guo Qiang", "Leong Jun Kai", "Ding Yong Rui", "Lye Hao Ming"],
        "หญิง": ["Tin En Hui", "Zeng Min Hui", "Qin Yan Ling", "Ye Xi Ling", "Zeng Shu Hui", "Zhu Xin En", "Tee Jia Hui", "Lew Jia Min", "Oon En Xin", "Zhuang Jia Xin", "Binte Yi Xi", "Qian Jia Min", "Teong Kai Xin", "Tin Min Hui", "Pan Shu Qi", "Tee Zhi En", "How Yi Xi", "Tee Xi Hui", "Yeh Yi Min", "Hu Rui Min"]
    },
    "ลาว": {
        "ชาย": ["Sengprachanh", "Thammavong", "Chanthanane", "Champasack", "Khouphongsy", "Phomsouvanh", "Phothisarath", "Sisoulith", "Rattanavongsa", "Thammavong", "Sonexarth", "Champasak", "Menorath", "Tayvihane", "Simnouansai", "Manwilaivong", "Phommajack", "Douangmala", "Inthisane", "Kommandam"],
        "หญิง": ["Syvongsa", "Saenbouthalath", "Louangrath", "Khanthavong", "Vongsay", "Souksanh", "Phomsouvanh", "Malaythong", "Genevong", "Bokeo", "Manwilaivong", "Phoutthasinh", "Phaophanit", "Kommandam", "Tayvihane", "Seeha", "Phommajack", "Douangvily", "Vongphakdy", "Xiengboree"]
    },
    "อินโดนีเซีย": {
        "ชาย": ["Balangga Januar", "Galak Putra", "Radika Siregar", "Dacin Irawan", "Jayeng Natsir", "Jindra Jailani", "Galak Habibi", "Jayadi Samosir", "Maras Dongoran", "Emin Halim", "Keili Seeha", "Makani Ketthavong", "Keanu Saenthavisouk", "Okelani Thammavong", "Sathit Khamchanh", "Dorit Keothavong", "Allyn Kaewdara", "Kalei Keobunta", "Aloha Inthisane"],
        "หญิง": ["Vivi Wulandari", "Kania Kusmawati", "Anastasia Susanti", "Cinthia Yolanda", "Nabila Halimah", "Rahayu Nasyiah", "Kamaria Purwanti", "Maida Puspita", "Hilda Namaga", "Latika Andriani", "Eli Widiastuti", "Halima Zulaika", "Maimunah Mandasari", "Karen Yulianti", "Salimah Palastri", "Safina Wijayanti", "Rini Yolanda", "Tina Andriani", "Karimah Namaga", "Mutia Oktaviani"]
    },
    "พม่า": {
        "ชาย": ["Thiha Mg", "Win Hein", "Myo Thura", "Zaw Yarzar", "Zin Myo Ye", "Kaung Khant Thuta", "Min Khant Zin", "Phyoe Mg Linn Sein", "Thurein Min Ye Kyaw", "Thuta Zarni Zeyar Kaung", "Thura Wai", "Thant Phyoe", "Thurein Phyo", "Kyaw Phyo", "Sein Sein Myat", "Wunna Zaw U", "Soe Kaung Thiha", "Thu Myint Ye Myat", "Thet Arkar Zarni Mg", "Zarni Htut Htut Maung"],
        "หญิง": ["Hnin Phyu", "Htet Nanda", "Thinzar Thi", "Aeindra Thawdar", "Win New May", "Aeindra Thin Yadanar", "Thin Yee Thi", "Khaing Thawda Yee San", "Myint Cho Htay Marlar", "Yee Thet Phone Nila", "Thawdar Yuzana", "Zar Thida", "Nine Thuzar", "Zin Mon", "Hlaing Win Khine", "Thi Yadanar Nhin", "Hsu Thet Htun", "Thin Ei Yu Theingi", "Thu Myint Aye Yu", "San Yu Hnin Thinza"]
    },
    "มาเลเซีย": {
        "ชาย": ["Bassil bin Yahya", "Muneer bin Akram", "Majdi bin Qaaid", "Mahdi bin Jawhar", "Awad bin Rushdi", "Ujang bin Danang", "Bayu bin Agus", "Desa bin Bulat", "Uda bin Bachok", "Zakaria bin Bestari", "Majdi bin Taaj", "Amru bin Abdur Razzaaq", "Fareed bin Abdul Fattaah", "Thaamir bin Mushtaaq", "Hibbaan bin Abdus Salam", "Adi bin Tempawi", "Teruna bin Jiwa", "Kesuma bin Merdeka", "Raja bin Kuning", "Selasa bin Selamat"],
        "หญิง": ["Jasra binti Ashqar", "Aneesa binti Zayyaan", "Shaheera binti Shabaan", "Waleeda binti Adnaan", "Rihaab binti Haashid", "Zamrud binti Bongsu", "Pertiwi binti Jumaat", "Melur binti Elias", "Aisyah binti Zakaria", "Kembang binti Danang", "Suhaila binti Sharaf", "Rayyana binti Abdul Quddoos", "Amatullah binti Nawf", "Mastoora binti Abdul Hai", "Jasra binti Zaki", "Adi Putri binti Selamat", "Tempawan binti Mail", "Indah binti Labuh", "Delima binti Sagari", "Mawar binti Selasa"]
    },
    "บรูไน": {
        "ชาย": ["Abdullah Hoe", "Lim Tze", "Awang Kee", "Abdullah Mee", "Mohammad Ramlee", "Yong Kassim"],
        "หญิง": ["Nor Fun", "Dayang Kheng", "Nor Tudin", "Noraini Khan", "Nora Suhaili"]
    },
    "ฟิลิปปินส์": {
        "ชาย": [
    "Cuartio Nestor Hussein Español",
    "Ronnie Joey Abucay Arancel",
    "Kristofer Toro Limcuando Aldo",
    "Reginald Honoratas Catacutan García",
    "Jared Garrett Disomimba Rosales",
    "Jett Joe Sharif Fandiño",
    "Nevada Brandon Ibrahim Fernando",
    "Rodrigo Suelita Ancatan Ramos",
    "Yahir Franklin Camara Legaspí",
    "Aluino Elvio Abu Areopagita",
    "Miles Sincere Baang Liwag",
    "Mauricio Dean Abaygar Alcántar",
    "Jaxon Henry Cabigas Dungog",
    "Lucio Bennett Monzon Clemente",
    "Marco Vance Pandapatan Magno",
    "Tyree Cristiano Reotutar Reyes",
    "Sonny Devon Rahman Roxas",
    "Dangelo Elvin Suico Dimayuga",
    "Harold Donte Supsup Abella",
    "Mekhi Kellen Magpantay Suarez"
],
        "หญิง": ["Jovena Jazmin Gordon Martínez", "Shoshana Ansley Yamson Millares", "Greta Miranda Janani Zacarías", "Tejana Materia Pabustan Robles", "Norma Elyse Ide Escaño", "Kasey Danita Camama Ladera", "Yasmine Anissa Quibuyen Rubio", "Charo Monaique Lazaro Etrone", "Carletta Diana Dinguinbayan Esquivias", "Sarahi Alyson Posangco Buenconsejo"]
    },
}

# รูปภาพของธงแต่ละประเทศ
country_flags = {
    "ไทย": "flags/thailand.png",
    "เวียดนาม": "flags/vietnam.png",
    "กัมพูชา": "flags/cambodia.png",
    "สิงคโปร์": "flags/singapore.png",
    "ลาว": "flags/laos.png",
    "อินโดนีเซีย": "flags/indonesia.png",
    "พม่า": "flags/myanmar.png",
    "มาเลเซีย": "flags/malaysia.png",
    "บรูไน": "flags/brunei.png",
    "ฟิลิปปินส์": "flags/philippines.png",
    # เพิ่มประเทศเพิ่มเติมเหมือนเดิมได้ตามต้องการ
}

# สร้างแบบเลือกประเทศ
selected_country = st.selectbox("เลือกประเทศ", list(people_by_country.keys()))

# สร้างแบบเลือกเพศ
selected_gender = st.radio("เลือกเพศ", list(people_by_country[selected_country].keys()))

# ภาพธงของประเทศที่ถูกเลือก
flag_image = country_flags[selected_country]

# ฟังก์ชันสุ่มชื่อคน
def generate_name():
    name = random.choice(people_by_country[selected_country][selected_gender])
    return name

# Streamlit app
st.title("Random Name Generator In ASEAN")
st.write("Click below to generate your random name!")

# เมื่อกดปุ่ม "Generate Name"
if st.button("Generate Name"):
    name = generate_name()
    # แสดงรูปภาพธงพร้อมชื่อที่สุ่มได้ โดยกำหนดขนาดรูปภาพเล็กลงในแถว
    st.image(flag_image, caption=f"{selected_country}", width=100)
    st.success(f"Your random Name is: {name}")

page_bg_img = '''<style>
.stApp {
    background-image: url("https://upload.wikimedia.org/wikipedia/commons/a/a1/ASEAN_flag_map.png");
    background-size: cover;       
}
</style>'''
st.markdown(page_bg_img, unsafe_allow_html=True)



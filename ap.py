import streamlit as st
from streamlit_option_menu import option_menu
#from streamlit.components.v1 import html
#from st_on_hover_tabs import on_hover_tabs
import requests
#from streamlit_lottie import st_lottie
from PIL import Image
#import streamlit_analytics
import base64
#from streamlit_extras.mention import mention
#from streamlit_extras.app_logo import add_logo
import sqlite3
#from bs4 import BeautifulSoup
#from streamlit_extras.echo_expander import echo_expander

#test

# Set page title
st.set_page_config(page_title="CHARET Mohamed", page_icon = "desktop_computer", layout = "wide", initial_sidebar_state = "auto")

# Use the following line to include your style.css file
st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def render_lottie(url, width, height):
    lottie_html = f"""
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.14/lottie.min.js"></script>
    </head>
    <body>
        <div id="lottie-container" style="width: {width}; height: {height};"></div>
        <script>
            var animation = lottie.loadAnimation({{
                container: document.getElementById('lottie-container'),
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: '{url}'
            }});
            animation.setRendererSettings({{
                preserveAspectRatio: 'xMidYMid slice',
                clearCanvas: true,
                progressiveLoad: false,
                hideOnTransparent: true
            }});
        </script>
    </body>
    </html>
    """
    return lottie_html

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

footer = """
footer{
    visibility:visible;
}
footer:after{
    content:'Copyright © 2023 CHARET Mohamed';
    position:relative;
    color:black;
}
"""
# PDF functions
def show_pdf(file_path):
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="400" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_link(pdf_url, link_text="Click here to view PDF"):
    href = f'<a href="{pdf_url}" target="_blank">{link_text}</a>'
    return href

# Load assets
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# Assets for about me
img_utown = Image.open("utown.PNG")
img_lh = Image.open("lh.PNG")
img_ifg = Image.open("ana.jpg")
#Assets for competitions
# Assets for education

img_nus = Image.open("insea.png")
img_poc = Image.open("uiz.jpg")



# Assets for experiences





img_groundup = Image.open("FRS.jpeg")
img_hedgedrip = Image.open("Actuelia.png")

lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_abqysclq.json")

img_linkedin = Image.open("linkedin.png")
img_github = Image.open("github.png")
img_email = Image.open("email.png")

def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 20px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "youtube": "https://img.icons8.com/ios-filled/100/138a07/youtube-play.png",
                "linkedin": "https://img.icons8.com/ios-filled/100/138a07/linkedin.png",
                "github": "https://img.icons8.com/ios-filled/100/138a07/github--v2.png",
                "wordpress": "https://img.icons8.com/ios-filled/100/138a07/wordpress--v1.png",
                "email": "https://img.icons8.com/ios-filled/100/138a07/filled-message.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  with col2:
    b_no_commas = b.replace(',', '')
    st.markdown(b_no_commas)

def txt4(a, b):
  col1, col2 = st.columns([1.5,2])
  with col1:
    st.markdown(f'<p style="font-size: 25px; color: white;">{a}</p>', unsafe_allow_html=True)
  with col2: #can't seem to change color besides green
    st.markdown(f'<p style="font-size: 25px; color: red;"><code>{b}</code></p>', unsafe_allow_html=True)

#####################

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg.png')   


# Sidebar: If using streamlit_option_menu
with st.sidebar:
    with st.container():
        l, m, r = st.columns((1,3,1))
        with l:
            st.empty()
        with m:
            st.image(img_lh, width=175)
        with r:
            st.empty()
    
    choose = option_menu(
                        "CHARET Mohamed", 
                        ["About Me", "Site Overview", "Experience", "Technical Skills", "Education", "Projects", "Resume", "Testimonials", "Contact"],
                         icons=['person fill', 'globe', 'clock history', 'tools', 'book half', 'clipboard', 'trophy fill', 'heart', 'pencil square', 'image', 'paperclip', 'star fill', 'envelope'],
                         menu_icon="mortarboard", 
                         default_index=0,
                         styles={
        "container": {"padding": "0!important", "background-color": "#f6f6f6"},
        "icon": {"color": "darkorange", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#cfcfb4"},
    }
    )
    youtube_url = "https://www.youtube.com/channel/UClZiidsw5_SjGkO6XUfo40w"
    linkedin_url = "https://www.linkedin.com/in/mohamed-charet-952077223/"
    github_url = "https://github.com/medcharet"
    wordpress_url = "https://antcabbage.wordpress.com"
    email_url = "mailto:mohamedcharet6@gmail.com"
    with st.container():
        l, m, r = st.columns((0.11,2,0.1))
        with l:
            st.empty()
        with m:
            st.markdown(
                social_icons(30, 30, Youtube=youtube_url, LinkedIn=linkedin_url, GitHub=github_url, Wordpress=wordpress_url, Email=email_url),
                unsafe_allow_html=True)
        with r:
            st.empty()

st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
st.title("CHARET Mohamed")
# Create header
if choose == "About Me":
    #aboutme.createPage()
    with st.container():
        left_column, middle_column, right_column = st.columns((1,0.2,0.5))
        with left_column:
            st.header("About Me")
            st.subheader("Actuary/Financial Analyst")
            st.write("👋🏻 Hello, I'm Mohamed! I'm an actuary and financial analyst based in Rabat, Morocco. With two prior relevant experiences as a risk manager and a consultant, I'm constantly seeking unique internships to broaden my horizons before embarking on my career in actuarial science or finance upon graduation.")
            st.write("💼 I chose a career in actuarial science and finance due to my strong affinity for mathematics, a passion for analyzing data, and a keen interest in playing a pivotal role in financial risk management. These fields offer diverse opportunities, ranging from portfolio management to financial product pricing. Moreover, they have a direct impact on financial decisions, whether at the corporate or individual level, which motivates me to make a positive contribution in the ever-evolving financial sector.")
            # st.write("🏋🏻 In addition, I like to exercise in the gym, run, write, play video games and... enjoy eating good food in my free time!")
            st.write("👨🏼‍💻 Academic interests: Mathematics, Financial Markets, Computer Science.")
            st.write("💭 Ideal Career Prospects: Trader, Quant, Actuary, Financial Analyst.")
            st.write("📄 [Resume (1 page)](https://drive.google.com/file/d/1-8jC_RHNonthOp8bfGbXmv1koZQOihx1/view?usp=sharing)")
        with middle_column:
            st.empty()
        with right_column:
            st.image(img_utown)
elif choose == "Site Overview":   
    #overview.createPage()
    st.header("Site Overview")
    st.markdown("""
    Initally creating this as a portfolio website in the form of an extended resume, I came to discover the uniqueness of Streamlit as compared to typical front-end frameworks such as Angular and Bootstrap. Even though Streamlit is primarily used as a web application for dashboarding, its extensive features make it more aesthetically appealing to explore with as compared to alternatives such as Plotly and Shiny.
    
    With the convenience of using Python as a beginner-friendly programming language, I have now decided to evolve this personal project into a time capsule - documenting key moments and achievements that I have attained since commencing my formal education at 7 years old. In addition, should I be successful in completing this project, I intend to provide my codes as open-source, so that other students can document their educational journey in a similar manner.

    A video will also be embedded in this section to provide a detailed tour of this entire web application and its features.

    """)
    with st.container():
            col1, col2, col3 = st.columns((1,3,1))
            with col1:
                st.empty()
            with col2:
                st.video("https://www.youtube.com/watch?v=OuGHAj6YSyk")
            with col3:
                st.empty()
    st.markdown("""
    *For an optimal experience, do browse this site on desktop!*

    Updated May 1, 2023
    """)
# Create section for Work Experience
elif choose == "Experience":
    #st.write("---")
    st.header("Experience")
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_hedgedrip)
        with text_column:
            st.subheader("Risk Manager, [Actuelia Afrique](https://www.actuelia.ma/)")
            st.write("*August 2023 to September*")
            st.markdown("""
            - Monitoring KPIs(Monitoring key performance indicators):
              Continuous monitoring and analysis of an reinsurance company's financial performance and risks is essential. KPIs are utilized to evaluate the financial health, profitability, risk exposure, and regulatory compliance of the company. These metrics may include measures such as solvency ratios, return on equity, investment yields, and more.
            The primary objective of this monitoring is to secure the long-term viability of the company by identifying potential trends, vulnerabilities, and opportunities. Managers and actuaries use this data to make informed decisions regarding policy pricing, asset allocation, risk management, while adhering to regulatory requirements.
            - Calculating the Solvency Capital Requirement (SCR):
                        
              Standard Method: This approach relies on regulatory standards and parameters established by supervisory authorities. Insurance companies use these standards to assess their required capital based on specific risks they face, including market, credit, operational risks, and more.

              Internal Model: Some insurance companies develop their own internal models to assess their SCR. These models are typically more sophisticated, taking into account the company's specific characteristics and internal data to calculate the required capital.

            """)
    with st.container():
        image_column, text_column = st.columns((1,5))
        with image_column:
            st.image(img_groundup)
        with text_column:
            st.subheader("Consultant, [FRS Consulting](https://frsconsulting.fr/en/home/)")
            st.write("*July to September 2023*| [*Testimonial*](https://drive.google.co)")
            st.markdown("""
            - Examining provision methodologies, which include deterministic strategies like Chain LADDER, Chain LADDER London, and the Bornhuetter-Fergusson method, alongside stochastic approaches such as the Mack method and the GLM method.
            - Automating the provisioning calculations is the next step, achieved through the development of a Python-based web page leveraging the Streamlit library, thereby enhancing efficiency and ease of use.
             `Python` `Pricing` `Streamlit` 
            """)




             
            
           
   
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:0px;
    }
    </style>
    ''', unsafe_allow_html=True)
#st.write("##")

# Create section for Technical Skills
elif choose == "Technical Skills":
    #st.write("---")
    st.header("Technical Skills")
    txt3("Actuarial Science", "`Underwriting`, `Reserving`, `Life Insurance`, `Non-life Insurance`, `Predictive Modeling`")
    txt3("Statistics", "`Time Series Modeling`, `Linear Regression`, `ANOVA`, `Principal Component Analysis`, `Statistical Inference`")
    txt3("Finance", "`Financial Mathematics`, `Market Finance`, `Portfolio Management`, `Pricing`, `Stochastic Calculus`, `Financial Econometrics`")
    txt3("Data Science", "`Supervised Learning`, `Unsupervised Learning`, `Classification`")
    txt3("Computer Science", "`LaTeX`, `C++`, `R`, `SAS`, `EXCEL/VBA`, `PYTHON`")

# Create section for Education
#st.write("---")
elif choose == "Education":
    st.header("Education")
    selected_options = ["Summary", "Modules"
                        ]
    selected = st.selectbox("Which section would you like to read?", options = selected_options)
    st.write("Current selection:", selected)
    if selected == "Summary":
        st.subheader("Summary")
        st.write("*Summary of education from primary school till university*")
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(img_nus)
            with text_column:
                st.subheader("Engineer - [Financial and Actuarial] [National Institute of Statistics and Applied Economics] (2021-2024)")
                st.write("Relevant Coursework in Actuarial Science and Finance: Actuarial Mathematics, Financial Risk Management, Time Series Analysis, Investment Analysis, Derivatives Pricing, Portfolio Management, Statistical Methods for Finance, Stochastic Calculus, Financial Modeling, Econometrics, Probability Theory, and Financial Data Analysis.")
                st.markdown("""
                - [NUS Product Club](https://linkedin.com/company/nusproductclub) - Co-founder & President (2023-24)
                - [NUS Statistics and Data Science Society](https://sites.google.com/view/nussds/home) - President (2022), Marketing Director (2021-22)
                - [Google Developer Student Clubs NUS](https://dsc.comp.nus.edu.sg/) - Deputy Head of Finance (2021-22)
                """)
        with st.container():
            image_column, text_column = st.columns((1,2.5))
            with image_column:
                st.image(img_poc)
            with text_column:
                st.subheader("Bachelor of Science - Science Mathematique, [University IBN ZOHR - AGADIR](2018-2021)")
                st.write("My academic journey has been the foundation for the development of my exceptional skills in pure mathematics. I have gained a deep understanding of mathematical fundamentals, covering a wide spectrum from algebra to topology, through mathematical analysis. My ability to solve complex problems using advanced mathematical methods, to construct rigorous proofs, and to apply these skills in various fields reflects my passion and dedication to this discipline. These strong skills in pure mathematics are an essential cornerstone of my education and lay a solid foundation for my future academic and professional pursuits")
               


elif choose == "Resume":   
    resume_url = "https://drive.google.com/file/d/1-8jC_RHNonthOp8bfGbXmv1koZQOihx1/view?usp=sharing"
    st.header("Resume")
    st.write("*In case your current browser cannot display the PDF documents, do refer to the hyperlink below!*")

    st.markdown(pdf_link(resume_url, "**Resume (1 page)**"), unsafe_allow_html=True)
    show_pdf("CV_CHARET_Mohamed.pdf")
    with open("CV_CHARET_Mohamed.pdf", "rb") as file:
        btn = st.download_button(
            label="Download Resume (1 page)",
            data=file,
            file_name="CharetMohamed_Resume.pdf",
            mime="application/pdf"
        )
elif choose == "Testimonials": 
    test_url = "https://drive.google.com/file/d/1-8jC_RHNonthOp8bfGbXmv1koZQOihx1/view?usp=sharing"  
    st.header("Testimonials")
    st.subheader("Some appraisals from my past referees!")
    st.markdown(pdf_link(test_url, "**Compiled Testimonials**"), unsafe_allow_html=True)  
    with st.container():  
        col1, col2, col3 = st.columns((1,1,1))
        with col1:
            st.subheader("SCOR")
            show_pdf("c1.pdf")
        with col2:
            st.subheader("DSDS, NUS")
            show_pdf("c2.pdf")
        with col3:
            st.subheader("IASG")
            show_pdf("c3.pdf")
    with st.container():  
        col4, col5, col6 = st.columns((1,1,1))
        with col1:
            st.subheader("SAF")
            show_pdf("c4.pdf")
        with col2:
            st.subheader("TPJC")
            show_pdf("c5.pdf")
        with col3:
            st.subheader("SJI")
            show_pdf("c6.pdf")
elif choose == "Contact":
# Create section for Contact
    #st.write("---")
    st.header("Contact")
    def social_icons(width=24, height=24, **kwargs):
        icon_template = '''
        <a href="{url}" target="_blank" style="margin-right: 10px;">
            <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
        </a>
        '''

        icons_html = ""
        for name, url in kwargs.items():
            icon_src = {
                "linkedin": "https://cdn-icons-png.flaticon.com/512/174/174857.png",
                "github": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
                "email": "https://cdn-icons-png.flaticon.com/512/561/561127.png"
            }.get(name.lower())

            if icon_src:
                icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)

        return icons_html
    with st.container():
        text_column, mid, image_column = st.columns((1,0.2,0.5))
        with text_column:
            st.write("Let's connect! You may either reach out to me at mohamedcharet6@gmail.com or use the form below!")
            
            def create_database_and_table():
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute('''CREATE TABLE IF NOT EXISTS contacts
                            (name TEXT, email TEXT, message TEXT)''')
                conn.commit()
                conn.close()
            create_database_and_table()

            st.subheader("Contact Form")
            if "name" not in st.session_state:
                st.session_state["name"] = ""
            if "email" not in st.session_state:
                st.session_state["email"] = ""
            if "message" not in st.session_state:
                st.session_state["message"] = ""
            st.session_state["name"] = st.text_input("Name", st.session_state["name"])
            st.session_state["email"] = st.text_input("Email", st.session_state["email"])
            st.session_state["message"] = st.text_area("Message", st.session_state["message"])


            column1, column2= st.columns([1,5])
            if column1.button("Submit"):
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
                        (st.session_state["name"], st.session_state["email"], st.session_state["message"]))
                conn.commit()
                conn.close()
                st.success("Your message has been sent!")
                # Clear the input fields
                st.session_state["name"] = ""
                st.session_state["email"] = ""
                st.session_state["message"] = ""
            def fetch_all_contacts():
                conn = sqlite3.connect('contact_form.db')
                c = conn.cursor()
                c.execute("SELECT * FROM contacts")
                rows = c.fetchall()
                conn.close()
                return rows
            
            if "show_contacts" not in st.session_state:
                st.session_state["show_contacts"] = False
            if column2.button("View Submitted Forms"):
                st.session_state["show_contacts"] = not st.session_state["show_contacts"]
            
            if st.session_state["show_contacts"]:
                all_contacts = fetch_all_contacts()
                if len(all_contacts) > 0:
                    table_header = "| Name | Email | Message |\n| --- | --- | --- |\n"
                    table_rows = "".join([f"| {contact[0]} | {contact[1]} | {contact[2]} |\n" for contact in all_contacts])
                    markdown_table = f"**All Contact Form Details:**\n\n{table_header}{table_rows}"
                    st.markdown(markdown_table)
                else:
                    st.write("No contacts found.")


            st.write("Alternatively, feel free to check out my social accounts below!")
            linkedin_url = "https://www.linkedin.com/in/mohamedcharet/"
            github_url = "https://github.com/medcharet"
            email_url = "mailto:mohamedcharet6@gmail.com"
            st.markdown(
                social_icons(32, 32, LinkedIn=linkedin_url, GitHub=github_url, Email=email_url),
                unsafe_allow_html=True)
            st.markdown("")
            #st.write("© 2023 CHARET Mohamed")
            #st.write("[LinkedIn](https://linkedin.com/in/mohamedcharet) | [Github](https://github.com/mohamedcharet) | [Linktree](https://linktr.ee/mohamedcharet)")
        with mid:
            st.empty()
        with image_column:
            st.image(img_ifg)
st.markdown("*Copyright © 2024 CHARET Mohamed*")


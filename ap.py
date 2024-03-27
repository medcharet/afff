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
img_utown = Image.open("utown.png")
img_lh = Image.open("lh.png")
img_ifg = Image.open("ana.jpg")
#Assets for competitions
# Assets for education

img_nus = Image.open("insea.png")
img_poc = Image.open("uiz.jpg")

img_groundup = Image.open("FRS.jpeg")
img_hedgedrip = Image.open("actuelia.png")
# # Assets for contact
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

#def txt3(a, b):
  #col1, col2 = st.columns([1,2])
  #with col1:
    #st.markdown(f'<p style="font-size: 20px;">{a}</p>', unsafe_allow_html=True)
  #with col2:
    # Split the text at the comma and wrap each part in backticks separately
    #b_parts = b.split(',')
    #b_formatted = '`' + ''.join(b_parts) + '`'
    #st.markdown(f'<p style="font-size: 20px; font-family: monospace;">{b_formatted}</p>', unsafe_allow_html=True)
    #st.markdown(f'<p style="font-size: 20px; color: red;"></code>{b}</code></p>', unsafe_allow_html=True)

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
                # st.markdown("""
                # Withdrew from course in 2020, before performing a clean slate transfer to pursue a Bachelor's Degree in Data Science and Analytics
                # - [NUS Students' Science Club](https://www.nussciencelife.com/) - Marketing Executive, Welfare Subcommittee
                # - Pharmaceutical Science (Class of 2023) - Assistant Class Representative
                # """)
       


# elif choose == "Projects":
#     # Create section for Projects
#     #st.write("---")
#     st.header("Projects")
#     with st.container():
#         text_column, image_column = st.columns((3,1))
#         with text_column:
#             st.subheader("Blockchain Social Media Webscraper")
#             st.write("*Project for US-based stealth startup, Bitmetrix.ai*")
#             st.markdown("""
#             - Utilised snscrape to scrape tweets from top blockchain websites such as CoinGecko and CoinMarketCap
#             - Built webscraper using BeautifulSoup4 to scrape content from fintech news websites such as https://blockchain.news
#             """)
#             # st.write("[Github Repo](https://github.com/harrychangjr/sales-prediction)")
#             mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/blockchain-webscraping",)
#         with image_column:
#             st.image(images_projects[14])
#     with st.container():
#         text_column, image_column = st.columns((3,1))
#         with text_column:
#             st.subheader("Enhanced TikTok Analytics Dashboard")
#             st.write("*Self-initiated project*")
#             st.markdown("""
#             - Provided options to plot Tiktok user overview data using 3D lineplots, 3D scatterplots, 3D surfaceplots and radar chart from Plotly
#             - Filtered number of hashtags per Tiktok video to investigate relationship between hashtag count and other variables: views, comments, likes and shares
#             - Performed hashtag analysis using Word2Vec to calculate cosine similarity scores and deduce correlation with average performance scores of each hashtag
#             """)
#             # st.write("[Github Repo](https://github.com/harrychangjr/sales-prediction)")
#             mention(label="Streamlit App", icon="streamlit", url="https://huggingface.co/spaces/harrychangjr/tiktok_analytics",)
#             mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/tiktok-analytics",)
#         with image_column:
#             st.image(images_projects[13])
#     with st.container():
#         text_column, image_column = st.columns((3,1))
#         with text_column:
#             st.subheader("Creating Sales Volume Prediction Model with Regression Methods")
#             st.write("*Self-initiated project based on e-commerce case study*")
#             st.markdown("""
#             - Conducted exploratory data analysis (EDA) to identify relationships between variables using correlation heatmaps and histograms
#             - Trained and compared multiple regression, random forest and XGBoost to build optimal model for sales volume prediction
#             - Performed randomized search with cross-validation to increase performance of random forest regressor and reduce MSE
#             """)
#             # st.write("[Github Repo](https://github.com/harrychangjr/sales-prediction)")
#             mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/sales-prediction",)
#         with image_column:
#             st.image(images_projects[0])
#     with st.container():
#         text_column, image_column = st.columns((3,1))
#         with text_column:
#             st.subheader("Optimising Article Quality with ChatGPT and NLP")
#             st.write("*Self-initiated project using past articles written for module SP1541: Exploring Science Communication in Popular Science in Academic Year 2020/21 Semester 1*")
#             st.markdown("""
#             - Preliminary analysis - comparing word counts, readability scores and sentiment (compound) scores of all 6 article variants using NLTK and Textstat
#             - Generated word clouds to highlight frequently used words in each article variant
#             - Identified top 10 most commonly used words between variants of the same article to assess suitability of ChatGPT in enhancing article quality
#             """)
#             #st.write("[Github Repo](https://github.com/harrychangjr/sp1541-nlp)")
#             mention(label="Streamlit App", icon="streamlit", url="https://sp1541-nlp.streamlit.app",)
#             mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/sp1541-nlp",)
#         with image_column:
#             st.image(images_projects[1])
#     with st.container():
#         text_column, image_column = st.columns((3,1))
#         with text_column:
#             st.subheader("Statistical Learning: Analysis on Video Game Sales")
#             st.write("*Completed project within 48 hours for module ST4248: Statistical Learning II in Academic Year 2022/23 Semester 2*")
#             #st.write("Methods performed on [Kaggle dataset](https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings):")
#             st.markdown("""
#             - Utilised multiple regression to investigate impact of publishers on global sales by regression coefficient, including performing one-hot encoding on 'Publisher' categorical variable
#             - Compared performances of multiple linear regression, random forest and XGBoost to predict global sales using critic scores and user scores from Metacritic
#             - Trained linear mixed-effects model to investigate impact of publishers, platform and genres in global sales
#             """)
#             #st.write("[Github Repo](https://github.com/harrychangjr/st4248-termpaper) | [Term Paper](https://github.com/harrychangjr/st4248-termpaper/blob/main/ST4248%20Term%20Paper%20(A0201825N)%20v5.pdf)")
#             mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/st4248-termpaper",)
#         with image_column:
#             st.image(images_projects[2])
#     with st.container():
#         text_column, image_column = st.columns((3,1))
#         with text_column:
#             st.subheader("Statistical Learning: Nourish Your Body with Data")
#             st.write("*Completed group project for module ST4248: Statistical Learning II in Academic Year 2022/23 Semester 2*")
#             st.markdown("""
#             - Adapted [previous project](https://drive.google.com/file/d/10ZOdQ8Q7UnevXxODAQs1YOstNSsiKh7G/view?usp=sharing) from DSA3101: Data Science in Practice, with the usage of statistical learning methods instead
#             - Performed random forest classification and clustering methods to identify different consumer segments of grocery shoppers in supermarkets
#             - Built recommendation system using matrix factorisation to recommend healthier food alternatives for grocery shoppers from different backgrounds
#             """)
#             #st.write("[Final Report](https://drive.google.com/file/d/1YuYxSTuDstSvyUa-bn782sLE5kCfbyH8/view?usp=sharing) | [Pitch Deck](https://www.canva.com/design/DAFeSnJeqgM/uXpz0kw8e7If4T1PG2tpaQ/view?utm_content=DAFeSnJeqgM&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink) | [Product Demo](https://www.youtube.com/watch?v=XMlt-kfdC7g)")
#             mention(label="Final Report", icon="📄", url="https://drive.google.com/file/d/1YuYxSTuDstSvyUa-bn782sLE5kCfbyH8/view?usp=sharing",)
#         with image_column:
#             st.image(images_projects[3])
#     with st.container():
#         text_column, image_column = st.columns((3,1))
#         with text_column:
#             st.subheader("Data Science Project on Biopics Dataset from Kaggle")
#             st.write("*Self-initiated project using various machine learning methods on [biopics dataset](https://www.kaggle.com/datasets/fivethirtyeight/fivethirtyeight-biopics-dataset)*")
#             st.markdown("""
#             - Ran regression models to predict box office revenue (linear regression, random forest, support vector machines)
#             - Used k-means clustering with principal components analysis to identify similar types of movies
#             - Built content-based recommendation system using cosine similarity to recommend similar movies based on input title
#             """)
#             #st.write("[Github Repo](https://github.com/harrychangjr/biopics) | [RPubs](https://rpubs.com/harrychangjr/biopics)")
#             mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/biopics",)
#         with image_column:
#             st.image(images_projects[4])
#     with st.container():
#         text_column, image_column = st.columns((3,1))
#         with text_column:
#             st.subheader("Optimisation for Large-Scale Data-Driven Inference: Anime Recommendation System")
#             st.write("*Completed assignment for module DSA4212: Optimisation for Large-Scale Data-Driven Inference in Academic Year 2022/23 Semester 2*")
#             st.markdown("""
#             - Built recommendation system using various non-factor models, including content-based collaborative filtering and clustering
#             - Utilised matrix factorisation (single value decomposition) to optimise performance of recommendation system with lower test MSE
#             - Provided optional recommendations to further optimise performance e.g scraping additional data, using deep learning methods
#             """)
#             #st.write("[Github Repo](https://github.com/harrychangjr/dsa4212) | [Report](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%202%20Group%2039%20Report.pdf)")
#             mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/dsa4212",)
#         with image_column:
#             st.image(images_projects[5])
#     with st.container():
#         text_column, image_column = st.columns((3,1))
#         with text_column:
#             st.subheader("Optimisation for Large-Scale Data-Driven Inference: Word Embedding")
#             st.write("*Completed assigmment for module DSA4212: Optimisation for Large-Scale Data-Driven Inference in Academic Year 2022/23 Semester 2*")
#             st.markdown("""
#             - Trained Word2Vec model on 20 Newsgroups dataset from scikit-learn package in Python, which provides a number of similar words based on input word
#             - Evaluated usefulness of model by applying model to text classification (46% accuracy) and sentiment analysis (86.4% accuracy)
#             """)
#             #st.write("[Github Code](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%203%20Group%2039.ipynb) | [Report](https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%203%20Group%2039%20Report.pdf)")
#             mention(label="Github Code", icon="github", url="https://github.com/harrychangjr/dsa4212/blob/main/DSA4212%20Assignment%203%20Group%2039.ipynb",)
#         with image_column:
#             st.image(images_projects[6])
#     with st.container():
#         text_column, image_column = st.columns((3,1))
#         with text_column:
#             st.subheader("Data-Driven Marketing: Exploration of cellphone billing and subscriber data")
#             st.write("*Self-initiated project based on past assignment from module BT4211: Data-Driven Marketing*")
#             st.markdown("""
#             - Performed preliminary churn analysis, customer segmentation and descriptive analysis to understand more about dataset
#             - Trained logit and probit models, as well as providing model estimations for duration models
#             - Utilised random forest classifier to predict customer churn
#             """)
#             #st.write("[Github Repo](https://github.com/harrychangjr/cellphone-billing) | [RPubs](https://rpubs.com/harrychangjr/cellphone)")
#             mention(label="Github Repo", icon="github", url="https://github.com/harrychangjr/cellphone-billing",)
#         with image_column:
#             st.image(images_projects[7])
#     with st.container():
#         text_column, image_column = st.columns((3,1))
#         with text_column:
#             st.subheader("Data Visualization: Analysis on Spotify Dataset from [tidytuesday](https://github.com/rfordatascience/tidytuesday/blob/master/data/2020/2020-01-21)")
#             st.write("*Completed group project for module DSA2101: Essential Data Analytics Tools: Data Visualization in Academic Year 2021/22 Semester 2*")
#             st.markdown("""
#             - Investigated variables that differentiates songs of different genres, which could be useful in designing recommendation systems
#             - Explored how do the four seasons affect number of songs produced in each period
#             - Visualizations used: ridgeline faceted density plot, boxplot, line chart, faceted donut chart
#             """)
#             #st.write("[Github Code](https://github.com/harrychangjr/dsa2101/blob/main/DSA2101_Group%20B.Rmd) | [RPubs](https://rpubs.com/harrychangjr/dsa2101-groupb)")
#             mention(label="Github Code", icon="github", url="https://github.com/harrychangjr/dsa2101/blob/main/DSA2101_Group%20B.Rmd",)
#         with image_column:
#             st.image(images_projects[8])
#     with st.container():
#         text_column, image_column = st.columns((3,1))
#         with text_column:
#             st.subheader("Computers and the Humanities: Chloropleths using Google Sheets and Folium in Python")
#             st.write("*Completed assignment for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2*")
#             st.markdown("""
#             - Visualized the total number of performances of A Doll's House by country, using a chloropleth from Google Sheets
#             - Drafted scatterplots and boxplots using seaborn to investigate relationship between number of events per country and number of years these plays have been performed
#             - Created chloropleth using Folium in Google Colab to compare total performance counts in China, categorised by province
#             """)
#             #st.write("[Google Sheets](https://docs.google.com/spreadsheets/d/1NBlGM7Sjcybbpl1Esa55qLRJw-Seti1LhC93EhV_68w/edit?usp=sharing) | [Google Colab](https://colab.research.google.com/drive/1RHqtb5XC7PkJDpNEb-BY3tO-8mI2j32E?usp=sharing)")
#             mention(label="Google Drive", icon="🗂️", url="https://drive.google.com/drive/folders/1Iva0oLZim6zJlAndoSzR63pUq4NCznim?usp=share_link",)
#         with image_column:
#             st.image(images_projects[9])
#     with st.container():
#         text_column, image_column = st.columns((3,1))
#         with text_column:
#             st.subheader("Computers and the Humanities: Network Analysis on Harry Potter Film Database")
#             st.write("*Completed assignment for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2*")
#             st.markdown("""
#             - Utilised custom Python file based on NetworkX and Glob to create networks using Harry Potter film database
#             - Drafted visualizations using matplotlib and seaborn to compare densities and weighted degree values of nodes from generated networks
#             - Customised network visualization using Gephi to investigate relationship between various Harry Potter film directors
#             """)
#             #st.write("[Github Code](https://github.com/harrychangjr/get1030/blob/main/A0201825N_GET1030_Tutorial_4.ipynb)")
#             mention(label="Github Code", icon="github", url="https://github.com/harrychangjr/get1030/blob/main/A0201825N_GET1030_Tutorial_4.ipynb",)
#         with image_column:
#             st.image(images_projects[10])
#     with st.container():
#         text_column, image_column = st.columns((3,1))
#         with text_column:
#             st.subheader("Computers and the Humanities: Text Processing and Analysis on Song Lyrics")
#             st.write("*Completed assignment for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2*")
#             st.markdown("""
#             - Utilised custom Python file based on NetworkX and Glob to create networks using Harry Potter film database
#             - Drafted visualizations using matplotlib and seaborn to compare proportions of nouns and verbs between different songs
#             - Analysed type/token ratios of songs from both albums to evaluate which album produced better quality songs based on words used
#             """)
#             #st.write("[Github Code](https://github.com/harrychangjr/get1030/blob/main/A0201825N%20-%20GET1030%20Tutorial%203.ipynb)")
#             mention(label="Github Code", icon="github", url="https://github.com/harrychangjr/get1030/blob/main/A0201825N%20-%20GET1030%20Tutorial%203.ipynb",)
#         with image_column:
#             st.image(images_projects[11])
#     with st.container():
#         text_column, image_column = st.columns((3,1))
#         with text_column:
#             st.subheader("Computers and the Humanities: Spotify in the Covid-19 Era")
#             st.write("*Completed group project for module GET1030: Computers and the Humanities in Academic Year 2020/21 Semester 2*")
#             st.markdown("""
#             - Compiled and scraped Spotify data from [Spotify](https://www.spotifycharts.com), [Kaggle](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks), and [OWID](https://ourworldindata.org/coronavirus/country/singapore) to analyse top songs played in Singapore during Covid-19
#             - Drafted Tableau dashboard to showcase correlation between various features of top songs, including tempo, acousticness and popularity
#             - Embedded 30-second snippet of featured song on dashboard for increased interactiveness
#             """)
#             #st.write("[Github Code](https://github.com/harrychangjr/get1030/blob/main/A0201825N%20-%20GET1030%20Tutorial%203.ipynb)")
#             mention(label="Final Report", icon="📄", url="https://github.com/harrychangjr/get1030/blob/main/GET1030%20Final%20Project.pdf",)
#         with image_column:
#             st.image(images_projects[12])
#elif choose == "Site Analytics":
    #st.header("Site Analytics")
    #with st.container():
      #with streamlit_analytics.track():
            #st.text_input("Enter something below if you'd like!", key="name_input", 
                      #help="Just type something!", 
                      #value="Type something here!", 
                      #max_chars=100, 
                      #type="default",
                      #)
            #st.markdown("""
            #<style>
                #/* Add custom CSS styles for the text input */
                ##name_input input[type=text] {
                    #background-color: #f2f2f2;
                    #border: none;
                    #padding: 8px;
                    #font-size: 16px;
                    #width: 100%;
                #}
            #</style>
            #""", unsafe_allow_html=True)
            #st.button("Click me!")
            #st.write("...and now add `?analytics=on` to the URL to see the analytics dashboard 👀")

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
            #with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
                #st.write('Please help us improve!')
                #Name=st.text_input(label='Your Name',
                                    #max_chars=100, type="default") #Collect user feedback
                #Email=st.text_input(label='Your Email', 
                                    #max_chars=100,type="default") #Collect user feedback
                #Message=st.text_input(label='Your Message',
                                        #max_chars=500, type="default") #Collect user feedback
                #submitted = st.form_submit_button('Submit')
                #if submitted:
                    #st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')
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
st.markdown("*Copyright © 2023 CHARET Mohamed*")


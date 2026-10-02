"""All site content lives here. Edit this file, then run `python3 src/build.py`."""

SITE = {
    "name": "Dulaj Dasanayake",
    "first": "Dulaj",
    "last": "Dasanayake",
    "full_name": "Dulaj Kavinda Dasanayake",
    "cv_url": "https://drive.google.com/file/d/1sNIkvmHZt5kOc4aSiup0BzGbhzcI7GYi/view?usp=sharing",
    "email": "dulaj[DOT]kavinda[DOT]dasanayake[AT]gmail[DOT]com",
    "address": "Gampaha, Sri Lanka",
    "year": 2025,
}

NAV = [
    ("home", "Home", "index.html"),
    ("education", "Education", "education.html"),
    ("career", "Career", "career.html"),
    ("research", "Research", "research.html"),
    ("awards", "Awards", "awards.html"),
]

# (kind, url, label). kind "fa" = Font Awesome class, "img" = file in images/icons
HERO_SOCIALS = [
    ("fa", "https://www.linkedin.com/in/dulaj-kavinda-dasanayake/", "fa-linkedin", "LinkedIn"),
    ("fa", "https://www.instagram.com/dulaj_kavinda_98/profilecard/?igsh=bGtsMHJtd2VpN2Zx", "fa-instagram", "Instagram"),
    ("img", "https://x.com/dulajkavinda98?s=21&t=XB2X6NZhT37xtIvBAcLJww", "twitter-x", "X"),
    ("fa", "https://github.com/Dulaj-Kavinda", "fa-github", "GitHub"),
]

FOOTER_SOCIALS = [
    ("fa", "https://www.linkedin.com/in/dulaj-kavinda-dasanayake/", "fa-linkedin", "LinkedIn"),
    ("fa", "https://github.com/Dulaj-Kavinda", "fa-github", "GitHub"),
    ("img", "https://scholar.google.com/citations?hl=en&user=IfszygYAAAAJ", "google-scholar", "Google Scholar"),
    ("img", "https://medium.com/@DulajDasanayake", "medium", "Medium"),
    ("img", "https://www.researchgate.net/profile/Dulaj-Dasanayake", "researchgate", "ResearchGate"),
]

TYPEWRITER_ROLES = ["Computer Science &amp; Engineering Graduate", "Software Engineer"]

HOME_CARDS = [
    ("education.html", "card-education.jpg", "Education", "Learn about the academic journey that shaped my passion."),
    ("career.html", "card-career.jpg", "Career", "Explore the experiences that define my growth."),
    ("research.html", "card-research.jpg", "Research", "Discover the academic and applied research I’ve contributed to."),
    ("awards.html", "card-awards.jpg", "Awards", "See the recognitions that reflect my commitment."),
]

BLOG_POSTS = [
    {
        "image": "blog_hl7.png",
        "date": "Jul 1, 2022",
        "title": "What exactly is HL7 v2?",
        "text": "An easy-to-follow guide to understanding HL7 v2 and why it plays a crucial role in streamlining healthcare data exchange.",
        "url": "https://medium.com/@DulajDasanayake/what-exactly-is-hl7-v2-147c121d0c52",
    },
    {
        "image": "blog_RL.jpg",
        "date": "Jul 7, 2025",
        "title": "The Basics of Reinforcement Learning: How AI Learns from Trial and Error",
        "text": "Explores how AI agents learn optimal behaviors by interacting with environments, receiving feedback, and refining actions over time.",
        "url": "https://medium.com/@DulajDasanayake/the-basics-of-reinforcement-learning-how-ai-learns-from-trial-and-error-3ca11ecd362c",
    },
    {
        "image": "blog-img2.png",
        "date": "Coming Soon",
        "title": "New insights on AI &amp; systems",
        "text": "Stay tuned for my next article covering current research and industry applications.",
        "url": None,
    },
]

# ---------------------------------------------------------------- education
EDUCATION = [
    {
        "logo": "uom-logo.png", "alt": "UOM Logo",
        "heading": "University of Moratuwa, Sri Lanka",
        "subheading": "B.Sc. Engineering (Hons.) Computer Science and Engineering",
        "entries": [(
            "Oct. 2018 – Jul. 2023",
            "Cumulative Grade Point Average (CGPA): 3.86/4.0 - First Class Honors - Dean’s List"
            "<br><br>Engaged in academic research, contributing to system design, and collaborating with faculty "
            "on projects in computer science, AI, and software development.",
        )],
        "badge": ("https://uom.lk", "University of Moratuwa"),
    },
    {
        "logo": "esoft-logo.png", "alt": "ESOFT Logo",
        "heading": "ESOFT Metro Campus",
        "subheading": "Pearson Approved Diploma in Software Engineering",
        "entries": [(
            "Jan. 2018 – Jun. 2018",
            "Gained foundational knowledge in software engineering practices through coursework and practical lab sessions.",
        )],
        "badge": ("https://www.esoft.lk", "ESOFT Metro Campus"),
    },
    {
        "logo": "bc-logo.png", "alt": "Bandaranayake College Logo",
        "heading": "Bandaranayake College, Sri Lanka",
        "subheading": "General Certificate of Education Advanced &amp; Ordinary Levels",
        "entries": [
            (
                "GCE A/L Examination – May 2015 – Aug. 2017",
                "Obtained All ‘A’ (High Distinction) passes in the Physical Science stream (Physics, Combined "
                "Mathematics, Chemistry) with a Z-Score of 2.1565. Ranked <strong>23<sup>rd</sup> in the district</strong> "
                "and <strong>230<sup>th</sup> island-wide</strong> out of over <strong>32,000 students</strong> in Sri Lanka.",
            ),
            (
                "GCE O/L Examination – Jan. 2008 – Dec. 2014",
                "Achieved All ‘A’ (High Distinction) passes including Mathematics, Science, and English. "
                "Recognized for <strong>best performance</strong> in the college with the highest aggregate of marks.",
            ),
        ],
        "badge": ("https://www.bcg.lk/", "Bandaranayake College"),
    },
]

# ------------------------------------------------------------------- career
CAREER = [
    {
        "logo": "xeptagon-logo.png", "alt": "Xeptagon Logo",
        "heading": "Software Engineer",
        "entries": [("May 2025 – Present",
                     "Contributed to climate finance trading platform and modular full-stack microservices.")],
        "tech": "JavaScript, TypeScript, Node.js, Nest.js, Docker, Git",
        "badge": ("https://www.xeptagon.com", "Xeptagon (Pvt) Ltd"),
    },
    {
        "logo": "lseg-logo.png", "alt": "LSEG Logo",
        "heading": "Software Engineer",
        "entries": [("Jul. 2023 – Apr. 2025",
                     "Enhanced post-trade processing with test automation and Kafka integration.")],
        "tech": "C++, Java, Git, CMake, Conan, Apache Kafka, Jenkins",
        "badge": ("https://www.lseg.com", "London Stock Exchange Group"),
    },
    {
        "logo": "wso2-logo.png", "alt": "WSO2 Logo",
        "heading": "Software Engineering Intern",
        "entries": [("Dec. 2021 – Aug. 2022",
                     "Developed HL7v2 mapping accelerator for open-source healthcare integration.")],
        "tech": "Java, WSO2 EI, HTTP REST, HL7",
        "badge": ("https://wso2.com", "WSO2 Lanka (Pvt) Ltd"),
    },
    {
        "logo": "thinkblue-logo.png", "alt": "Think Blue Logo",
        "heading": "Data Science Engineering Intern",
        "entries": [("Jan. 2022 – Jul. 2022",
                     "Handled data scraping, visualization, and analysis for business insights.")],
        "tech": "Python, Pandas, Matplotlib, MongoDB",
        "badge": ("https://www.thinkbluedata.com", "Think Blue Data Co. Ltd"),
    },
]

# ----------------------------------------------------------------- research
RESEARCH = [
    {
        "title": "Hybrid Machine Learning for Strategic Market Exit Forecasting: Adversarial Modeling and Supervised Classification",
        "role": "Extension on Final Year Research &amp; Development Project",
        "description": (
            "This work extends the prior bottom-turning-point research to market top (exit) prediction. It proposes a hybrid pipeline that unifies "
            "<em>WGAN-GP</em> multi-step price forecasting, <em>Elliott-inspired neural wave-shape recognition</em>, and an <em>XGBoost</em> top-point classifier with dual-scale labeling. "
            "The approach improves F1 and simulated profit capture across U.S. stocks (AAPL, TSLA, SBUX) and cryptocurrencies (BTC, ETH, LTC)."
        ),
        "points": [
            "Dual-resolution labeling for tops using short and long step windows to reduce noise and scale ambiguity.",
            "WGAN-GP + GRU generator for 4-step ahead forecasting; features reused downstream.",
            "Neural wave-shape detector aligned with Elliott patterns over a 9-point waveform (observed + predicted).",
        ],
        "publication": (
            "<strong>Dulaj Dasanayake</strong>, Jalitha Kalsara, Madara Gunarathna, Chan Mahaarachchi, Sapumal Ahangama, Indika Perera.<br>"
            "<em>“Hybrid Machine Learning for Strategic Market Exit Forecasting: Adversarial Modeling and Supervised Classification.”</em><br>"
            "<span><strong>Accepted for presentation</strong> at The 8th International Conference on Information and Communications Technology (ICOIACT) 2025, "
            "4–5 December 2025, Yogyakarta, Indonesia. Proceedings (to appear).</span>"
        ),
    },
    {
        "title": "Generative Adversarial Network (GAN)-Based Forecasting of Market Movements and Prediction of Bottom Turning Points",
        "role": "Final Year Research &amp; Development Project",
        "description": (
            "Proposed a novel approach for forecasting market turning points using deep learning. The solution combines a WGAN-GP model with Gated Recurrent Units (GRUs) "
            "for time series representation learning, and an XGBoost classifier for bottom point identification using latent features. The model was tested across "
            "cryptocurrency and stock markets, outperforming standard LSTM/GRU/GAN baselines."
        ),
        "points": [
            "Designed WGAN-GP with GRU layers for sequential price prediction.",
            "Extracted hidden features for bottom point classification via XGBoost.",
            "Conducted extensive feature engineering using Fourier analysis, PCA, and VAE.",
            "Built a web interface using Next.js for real-time visualization of predictions.",
        ],
        "figure": ("fyp-architecture.png", "Forecasting System Architecture",
                   "Architecture of the GAN-GRU-based forecasting framework"),
        "links": [("https://youtu.be/sZjwhfJUSSc", "Watch Project Video")],
        "publication": (
            "<strong>D.M.D.K. Dasanayake</strong>, H.Y. Dilshan, H.D.K.Y. Rathnaweera, Sapumal Ahangama, Indika Perera.<br>"
            "<em>“A Novel Approach for Deep Learning-Powered Forecasting of Market Bottoms in Cryptocurrency and Stock Trading”</em>,<br>"
            "<span>Proceedings of the 2023 IEEE International Conference on Big Data, Sorento, Italy.</span>"
        ),
        "publication_links": [("https://ieeexplore.ieee.org/abstract/document/10386273", "View IEEE Publication")],
        "publication_figure": ("bigdata-presentation.jpg", "IEEE BigData 23 Presentation",
                               "Virtually presented the paper at IEEE BigData 2023"),
    },
    {
        "title": "HL7v2 Mapping Accelerator for Open Healthcare Integration",
        "role": "Independent Research Project at WSO2",
        "description": (
            "Designed and implemented a lightweight mapping engine for the HL7v2 messaging standard, supporting healthcare data transformation into JSON and XML formats. "
            "The accelerator leverages YAML templates and integrates with WSO2 EI to enable real-time interoperability across clinical systems."
        ),
        "points": [
            "Developed segment-to-JSON mapping logic using Java and event-driven architecture principles.",
            "Contributed to WSO2’s open-source healthcare integration framework.",
            "Explored use cases in electronic medical records (EMRs) and lab systems for real-world validation.",
            "Published a foundational technical blog to demystify HL7v2 and its role in modern healthcare APIs.",
        ],
        "figure": ("hl7-architecture.png", "HL7v2 Architecture",
                   "System architecture of the HL7v2 transformation pipeline"),
        "links": [("https://medium.com/@DulajDasanayake/what-exactly-is-hl7-v2-147c121d0c52", "Read Blog Article")],
    },
]

# ------------------------------------------------------------------- awards
AWARDS = [
    {
        "logos": [("uom-logo.png", "UOM Logo")],
        "title": "Dean's List",
        "date": "Oct. 2018 – Jul. 2023",
        "description": "Recognized for academic excellence by achieving Dean's List status in 6 out of 8 semesters at the University of Moratuwa, Sri Lanka.",
    },
    {
        "logos": [("awards/huawei-logo.png", "Huawei Logo")],
        "title": "5th Place – All-Island ICT Competition (Network Track)",
        "date": "Dec. 2022",
        "description": "Ranked 5th in Huawei's national-level ICT Competition (Network Track), demonstrating strong understanding and application of core networking technologies.",
        "images": [("awards/huawei-ict-competition.png", "The Huawei ICT Competition")],
        "note": "The Huawei ICT Competition is a global talent development program that challenges university students to solve complex problems in networking, cloud computing, and AI. The Network Track focuses on enterprise-level routing, switching, and network security.",
    },
    {
        "logos": [("awards/huawei-logo.png", "Huawei Logo")],
        "title": "Excellent Student Award in APAC Region – Huawei Global AppsUP 2021",
        "date": "Oct. 2021",
        "highlight": "\"Smart Reader\" mobile application using Flutter integrating Huawei kits won the Excellent Student Award from the Asia Pacific region.",
        "description": "Integrating Huawei's scanning and machine learning kits within the Flutter framework was identified as a significant contribution. Used technologies are Flutter, Dart, and HMS Core. The app is launched on Huawei AppGallery.",
        "images": [("awards/appsup-award.png", "Huawei AppsUP Award")],
        "note": "Huawei's AppsUP is an international app innovation contest aimed at encouraging developers to create impactful applications using Huawei Mobile Services (HMS) Core. It provides a platform for showcasing mobile innovations across multiple regions.",
    },
    {
        "logos": [("awards/ieee.png", "IEEE Logo"), ("awards/iasa-logo.png", "IASA Logo")],
        "title": "Top 20 – InnovMind IDEATHON",
        "date": "Dec. 2020",
        "highlight": "Selected for the Top 20 finalists for the project, \"IoT Based Touchless Elevator Control\" at the InnovMind Ideathon by IEEE IAS, SLTC.",
        "description": "It was implemented as a novel application for the passengers' using elevators, designed to avoid touching the virus-contaminated surfaces on elevator buttons for the issue that arose with the COVID pandemic. A touchless elevator system is designed using a QR code scanner for device identification and MQTT protocol for communication with elevator controllers.",
        "images": [("awards/innovomind-competition.jpg", "InnovMind IDEATHON"),
                   ("awards/innovomind-certificate.jpg", "InnovMind IDEATHON Certificate")],
        "note": "InnovMind Ideathon is a national innovation challenge organized by IEEE SLTC Industrial Applications Society to promote creative engineering ideas. It invites multidisciplinary student teams to present problem-solving concepts with real-world potential.",
    },
    {
        "logos": [("awards/ieee.png", "IEEE Logo"), ("awards/ieeextreme14.png", "IEEE Xtreme Logo")],
        "title": "73rd Place – IEEE Xtreme 14.0",
        "date": "Oct. 2020",
        "description": "Ranked 73rd in Sri Lanka in the globally competitive 24-hour coding contest IEEE Xtreme 14.0, highlighting algorithmic thinking and real-time problem-solving.",
        "note": "IEEE Xtreme is an international, 24-hour programming competition where teams of IEEE student members compete in solving algorithmic challenges under time pressure, testing both collaboration and problem-solving expertise.",
    },
    {
        "logos": [("awards/seds-mora.jpg", "SEDS Logo"), ("awards/acc-logo.png", "ACC Logo")],
        "title": "1st Runners Up – Tracking Device Design Competition",
        "date": "Sep. 2019",
        "highlight": "Awarded 1st Runners Up in a joint competition by SEDS Mora and Arthur C. Clarke Institute for designing a precision tracking unit for a water rocket.",
        "description": "The design is a measurement unit for a water rocket to find the distance from its launching position to the falling position and the maximum altitude it travels. GPS technology with NodeMCU is used as a microcontroller to get measurements and a mobile phone was used as the display having communication through Wi-Fi. A barometer was used to find the altitude.",
        "note": "This competition, organized by SEDS Mora in collaboration with the Arthur C. Clarke Institute, challenges students to engineer hardware-based tracking solutions for space-themed applications such as model rockets and scientific payloads.",
    },
]

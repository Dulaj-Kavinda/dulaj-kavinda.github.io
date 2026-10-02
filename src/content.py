"""All site content lives here. Edit this file, then run `python3 src/build.py`."""

SITE = {
    "name": "Dulaj Dasanayake",
    "first": "Dulaj",
    "last": "Dasanayake",
    "full_name": "Dulaj Kavinda Dasanayake",
    "cv_url": "https://drive.google.com/file/d/1sNIkvmHZt5kOc4aSiup0BzGbhzcI7GYi/view?usp=sharing",
    "email": "dulaj[DOT]kavinda[DOT]dasanayake[AT]gmail[DOT]com",
    "address": "Morgantown, West Virginia, United States",
    "year": 2026,
}

NAV = [
    ("home", "Home", "index.html"),
    ("education", "Education", "education.html"),
    ("career", "Career", "career.html"),
    ("research", "Research", "research.html"),
    ("projects", "Projects", "projects.html"),
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

TYPEWRITER_ROLES = ["Ph.D. Student in Biomedical Engineering", "Computer Science &amp; Engineering Graduate", "Software Engineer"]

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
        "heading": "West Virginia University, USA",
        "subheading": "Doctor of Philosophy (Ph.D.) in Biomedical Engineering",
        "entries": [(
            "Jan. 2026 – Present",
            "Brain Mapping &amp; Neuroimaging Lab, Benjamin M. Statler College of Engineering and Mineral Resources."
            "<br><br>Research focus: diffusion MRI tractometry, nonlinear tract registration, white matter analysis and machine learning.",
        )],
        "badge": ("https://www.wvu.edu", "West Virginia University"),
    },
    {
        "logo": "uom-logo.png", "alt": "UOM Logo",
        "heading": "University of Moratuwa, Sri Lanka",
        "subheading": "B.Sc. Engineering (Hons.) Computer Science and Engineering",
        "entries": [(
            "Oct. 2018 – Jul. 2023",
            "Cumulative GPA: 3.90/4.20 (3.86/4.0) – First Class Honors – Dean’s List for 6 out of 8 semesters; "
            "ranked 20th out of 120 students in the department "
            "(<a href=\"https://drive.google.com/file/d/1MuvsmXDl-b49mvCi8-lr4ISp1A0SyojW/view?usp=sharing\" target=\"_blank\"><u>Academic Transcript</u></a>)."
            "<br><br>Relevant coursework: Intelligent Systems, Machine Learning, Data Mining &amp; Information Retrieval, Distributed Systems, "
            "Database Systems, Software Architecture, Concurrent Programming, Bioinformatics.",
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
        "heading": "Graduate Research Assistant – Brain Mapping &amp; Neuroimaging Lab",
        "entries": [("Jan. 2026 – Present",
                     "Conducting Ph.D. research on diffusion MRI tractometry and white matter microstructure analysis, "
                     "processing large neuroimaging datasets on HPC environments with DIPY-based pipelines.")],
        "tech": "Python, DIPY, SLURM HPC, Bash, Linux",
        "badge": ("https://www.wvu.edu", "West Virginia University"),
    },
    {
        "logo": "xeptagon-logo.png", "alt": "Xeptagon Logo",
        "heading": "Senior Software Engineer | Software Engineer",
        "entries": [("Nov. 2025 – Dec. 2025 | May 2025 – Nov. 2025",
                     "Designed and developed full-stack modules integrating commercial APIs with climate finance trading platforms "
                     "and eco-management systems, and built containerized microservices for independent deployment and scalability.")],
        "tech": "React, Next.js, Node.js, NestJS, .NET, Docker, PostgreSQL, AWS, Git",
        "badge": ("https://www.xeptagon.com", "Xeptagon (Pvt) Ltd"),
    },
    {
        "logo": "lseg-logo.png", "alt": "LSEG Logo",
        "heading": "Software Engineer",
        "entries": [("Jul. 2023 – Apr. 2025",
                     "Developed and tested the Post Trade Transaction Processing System (PTTPS) for the FX team, and enhanced the "
                     "FortressFX test framework with Kafka topic updates, step definitions and Jenkins-based integration testing.")],
        "tech": "C++, Java, CMake, Conan, Apache Kafka, Jenkins, Oracle DB, Git",
        "badge": ("https://www.lseg.com", "London Stock Exchange Group"),
    },
    {
        "logo": "wso2-logo.png", "alt": "WSO2 Logo",
        "heading": "Software Engineering Intern",
        "entries": [("Dec. 2021 – Aug. 2022",
                     "Completed an independent research project implementing a mapping accelerator for the HL7v2 messaging standard in "
                     "WSO2 Open Healthcare, with YAML-based event transformations between HL7v2 and XML/JSON.")],
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

SKILLS = [
    ("Programming Languages", "Python, Java, JavaScript, C++, Dart, MATLAB, Bash/Shell"),
    ("Neuroimaging &amp; MRI Tools", "DIPY"),
    ("AI/ML &amp; Data Science", "PyTorch, TensorFlow, Scikit-learn, Pandas, NumPy, Matplotlib, Jupyter Notebook"),
    ("Web &amp; Mobile Development", "React, Node.js, Next.js, NestJS, .NET, HTML, CSS, Flutter"),
    ("Databases", "MySQL, Oracle, PostgreSQL, Firestore"),
    ("Cloud, DevOps &amp; HPC", "Azure, Docker, Apache Kafka, CMake, Jenkins, SLURM HPC, Git"),
    ("Other Technologies", "Elasticsearch, Arduino, WSO2 Enterprise Integrator, Huawei Kits"),
    ("Writing Tools", "Overleaf (LaTeX), Mendeley, Zotero"),
    ("Operating Systems", "Linux/Ubuntu, macOS, Windows"),
    ("Languages", "English (Fluent), Sinhala (Native)"),
]

CERTIFICATIONS = [
    ("Diffusion Imaging in Python Workshop 2026 – DIPY", "https://workshop.dipy.org/services/certificates/view/2026/dulaj_dasanayake.pdf"),
    ("Neural Networks and Deep Learning – DeepLearning.AI (Coursera)", "https://coursera.org/share/f40217ed48582287d0bbc329a5822a47"),
    ("The Complete Flutter Development Bootcamp with Dart – Udemy", "https://www.udemy.com/certificate/UC-6e86e59b-2898-4b62-8897-dc4a290fcc4b/"),
    ("Networking Essentials – Cisco Networking Academy", "https://www.credly.com/badges/f2667f87-3490-479e-8f78-a4d4285cb886?source=linked_in_profile"),
    ("HMS Foundation Course – Huawei Developers", "https://drive.google.com/file/d/1z7DLaVblzg1j8nXyqFbpEPK0X0goyX-o/view?usp=sharing"),
    ("Jenkins: Beginner To Pro – Udemy", "https://drive.google.com/file/d/1rdtqokhhG_eWE04WFsJwXe_3VwyDPWlC/view?usp=sharing"),
]

VOLUNTEERING = [
    ("Mar. 2023", "Organized the Department Career Fair as part of the organizing committee – Department of Computer Science and Engineering, University of Moratuwa"),
    ("Jun. 2019 – Aug. 2023", "Contributed to virtual asteroid search campaigns and knowledge-sharing sessions – SEDS Mora, University of Moratuwa"),
    ("Aug. 2020 – Aug. 2021", "Hosted knowledge-sharing sessions for students – ACM Student Chapter, University of Moratuwa"),
    ("Aug. 2019", "Volunteered as an instructor in mathematics seminars at Kotadeniyawa Central College – Students Union, University of Moratuwa"),
]

PROJECTS = [
    {
        "heading": "Predictor Web Application", "subheading": "Research Implementation Project",
        "entries": [("Apr. 2023 – Jul. 2023", "Developed a dynamic web application integrating a machine learning model with a full-stack architecture for market bottom prediction and price forecasting.")],
        "tech": "Python, Next.js, Azure",
        "links": [("https://youtu.be/K5R4pNfBMA0", "Video")],
    },
    {
        "heading": "American Express Credit Default Prediction", "subheading": "Machine Learning Project",
        "entries": [("Mar. 2023 – Jun. 2023", "Conducted a comparative study of classification models (LightGBM – ROC AUC: 0.9613, XGBoost, SVM, KNN) on a 16M+ record imbalanced financial dataset.")],
        "tech": "Python, Pandas, Scikit-learn",
        "links": [("https://github.com/Dulaj-Kavinda/ML-Mini-Project_Amex-DefaultPrediction", "Source")],
    },
    {
        "heading": "Sinhala Metaphor Searcher", "subheading": "Data Mining and IR Project",
        "entries": [("Dec. 2022 – Jan. 2023", "Built a specialized search engine for Sinhala song metaphors using text mining, preprocessing, faceted and multi-field search over a custom annotated corpus.")],
        "tech": "Elasticsearch, Node.js, Angular, Python",
        "links": [("https://github.com/Dulaj-Kavinda/SinhalaMetaphor_SE", "Source")],
    },
    {
        "heading": "Smart Travel Planner Application", "subheading": "Software Engineering Group Project",
        "entries": [("Jul. 2021 – Dec. 2021", "Created a rule-based itinerary planner integrating Google Places and Maps APIs for real-time recommendations and navigation based on user preferences.")],
        "tech": "Flutter, Dart, Firestore, Google APIs",
        "links": [("https://github.com/hypers-lab/smart-travel-planner", "Source")],
    },
    {
        "heading": "IoT-Based Touchless Elevator System", "subheading": "IoT Hardware Project",
        "entries": [("Aug. 2020 – Dec. 2020", "Designed a mobile app and QR-based identification system for touchless elevator access using MQTT communication. Selected for the semi-final round of SLIoT organized by Sri Lanka Telecom and IESL.")],
        "tech": "Flutter, Dart, Arduino, MQTT",
        "links": [("https://github.com/Dulaj-Kavinda/Touchless_Elevator", "Source")],
    },
]

# ----------------------------------------------------------------- research
RESEARCH = [
    {
        "title": "White Matter Tractometry and Diffusion MRI Analysis",
        "role": "Ph.D. Research – Brain Mapping &amp; Neuroimaging Lab, West Virginia University (Jan. 2026 – Present)",
        "description": (
            "Research on diffusion MRI-based white matter analysis using tractometry pipelines and the integration of machine learning. "
            "Technical fields: diffusion MRI, tractometry, nonlinear registration, machine learning."
        ),
        "points": [
            "Studying tract-specific microstructural properties (FA, MD) using along-tract statistical analysis.",
            "Working with MRI preprocessing pipelines including denoising, tractography, bundle segmentation, and bundle analytics on HPC environments.",
        ],
    },
    {
        "title": "Large Language Model-Based Deobfuscation of Obfuscated Android SDKs",
        "role": "Remote Collaboration, College of William &amp; Mary, USA (May 2025 – Jan. 2026)",
        "description": (
            "Contributed to research on deobfuscating heavily obfuscated Android SDKs using large language models. "
            "Technical fields: large language models (LLMs), Android security, prompt engineering."
        ),
        "points": [
            "Investigated model behavior under control flow flattening and Mixed Boolean Arithmetic (MBA).",
            "Explored prompt engineering strategies to improve cross-file consistency and scalability.",
        ],
    },
    {
        "title": "Hybrid Machine Learning for Strategic Market Exit Forecasting: Adversarial Modeling and Supervised Classification",
        "role": "Extension on Final Year Research &amp; Development Project (Mar. 2025 – Jul. 2025)",
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
            "<strong>D. Dasanayake</strong>, M. Gunarathna, C. Mahaarachchi, J. Kalsara, S. Ahangama, I. Perera.<br>"
            "<em>“Hybrid Machine Learning for Strategic Market Exit Forecasting: Adversarial Modeling and Supervised Classification”</em>,<br>"
            "<span>Proceedings of the 8th IEEE International Conference on Information and Communications Technology (ICOIACT 2025), "
            "IEEE, Dec. 2025, Yogyakarta, Indonesia.</span>"
        ),
        "publication_links": [("https://doi.org/10.1109/ICOIACT67584.2025.11344867", "View IEEE Publication")],
    },
    {
        "title": "Generative Adversarial Network (GAN)-Based Forecasting of Market Movements and Prediction of Bottom Turning Points",
        "role": "Final Year Research &amp; Development Project – Undergraduate Thesis (Oct. 2022 – Jul. 2023)",
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
            "<span>Proceedings of the 2023 IEEE International Conference on Big Data (Big Data 2023), IEEE, Dec. 2023, Sorrento, Italy.</span>"
        ),
        "publication_links": [("https://doi.org/10.1109/BigData59044.2023.10386273", "View IEEE Publication")],
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
        "title": "Deppe Fellowship Award – West Virginia University",
        "date": "Benjamin M. Statler College of Engineering and Mineral Resources",
        "highlight": "Awarded the Deppe Fellowship by the Benjamin M. Statler College of Engineering and Mineral Resources at West Virginia University for the academic year, as a Ph.D. student in the BMN Lab.",
        "description": "",
        "note": "The Deppe endowment provides graduate student research fellowships in the biological, biotechnological and biomedical sciences at the Statler College. Recipients are selected by the appropriate officials in the College with the approval of the Dean. The gift is also expected to qualify for a match under Senate Bill 287, the West Virginia Research Trust Fund.",
    },
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
    {
        "title": "Mahapola Merit Scholarship",
        "date": "Oct. 2018",
        "description": "Awarded by the University Grants Commission, Sri Lanka, for academic excellence in the G.C.E. Advanced Level; ranked 23rd in the district and 230th island-wide out of over 32,000 candidates.",
    },
]

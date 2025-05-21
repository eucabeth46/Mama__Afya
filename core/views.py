from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def team(request):
    team = [
        {
            'name': 'Dr. Nderu',
            'role': 'Project supervisor',
            'image': 'images/team/nderu1.jpeg',
            'bio': 'Experienced University Lecturer with a demonstrated history of working in the higher education industry. Skilled in Software Development, (Python, Java, C#, C++, R, JavaScript, Android, PHP, C++, and Databases. Strong education professional with a Doctor of Philosophy - PhD focused in Computer Science from University of Vincennes in Saint-Denis, Paris, France.',
            'linkedin': 'dr-nderu',
            'github': 'dr-nderu',
            'twitter': 'dr_nderu'
        },
        {
            'name': 'Eucabeth Awino',
            'role': 'Project Lead',
            'bio': "Led the team in building the UI/UX of a mobile-app using React Native with Firebase Authentication, ensuring cross-platform performance. Orchestrated team collaboration, sprint planning, code reviews, and architecture while implementing real-time Firestore updates and Redux state management.",
            'image': 'images/team/eucabeth.jpg',
            'linkedin': 'eucabeth-awino',
            'github': 'https://github.com/eucabeth46',
            'twitter': 'eucabeth_awino'
        },
        {
            'name': 'Lemmis Murangiri',
            'role': 'AI/ML Engineer',
            'bio': 'Specialized in developing and implementing machine learning models for maternal health risk prediction. Focused on data preprocessing, feature engineering, and model optimization to ensure reliable predictions for healthcare providers.',
            'image': 'images/team/lemmis.jpg',
            'linkedin': 'lemmis-murangiri',
            'github': 'lemmis',
            'twitter': 'lemmis_m'
        },
        {
            'name': 'Felix Rotich',
            'role': 'AI/ML Engineer',
            'bio': 'Felix Rotich- a Data Scientist responsible for extracting meaningful insights from maternal health data. I was deeply involved in understanding the data landscape, performing rigorous exploratory analysis to uncover key patterns and trends, and applying statistical methods to address critical questions related to improving maternal health outcomes in Kenya. My expertise was essential in preparing and analyzing data that informed the development of predictive models and data-driven interventions, effectively transforming raw data into actionable knowledge for the project',
            'image': 'images/team/felix.jpg',
            'linkedin': 'felix-rotich',
            'github': 'felixrotich',
            'twitter': 'felix_rotich'
        }, 
        {
             'name': 'Faith Mwangi',
            'role': 'Project Designer',
            'bio': "Faith Wanjiru Mwangi - a Project Designer focused on improving maternal health outcomes. I collaborated with data scientists to integrate data-driven insights into the project design, ensuring interventions addressed key issues in maternal health in Kenya. My work was crucial in turning complex data into actionable strategies, enhancing the project's impact.",
            'image': 'images/team/faith.jpg',
            'linkedin': 'faith-mwangi',
            'github': 'faithwanjiru',
            'twitter': 'faith_mwangi'
        },
        {
            'name': 'Denis Ndegwa',
            'role': 'Backend Developer',
            'bio': 'Denis Munene Ndegwa is a data-driven engineer and machine learning enthusiast who led the backend development and containerization of the Maternal Risk Prediction API. Leveraging his skills in Python and FastAPI, Denis designed and implemented RESTful endpoints, integrated MongoDB for data persistence, and managed the entire Docker-based containerization process to ensure the application is scalable and deployable. His work focused on ensuring reliable API performance while integrating machine learning predictions to support maternal health interventions in Kenya.',
            'image': 'images/team/munene.jpeg',
            'linkedin': 'denis-ndegwa',
            'github': 'https://github.com/MUNENE1212',
            'twitter': 'denis_ndegwa'
        }
    ]

    partners = [
        {
            'name': 'World Bank',
            'logo': 'images/partners/wb.jpg',
            'website': 'https://www.who.int/',
            'description': 'Technical expertise and global standards for maternal healthcare'
        },
        {
            'name': 'KIEP SKIES',
            'logo': 'images/partners/skies.png',
            'website': 'https://www.unicef.org/',
            'description': 'Supporting maternal and child health initiatives across Kenya'
        },
        {
            'name': 'JKUAT',
            'logo': 'images/partners/jkuat.jpg',
            'website': 'https://www.jkuat.ac.ke/',
            'description': 'Academic research and technology development partner'
        },
        {
            'name': 'JHUB',
            'logo': 'images/partners/jhub.jpg',
            'website': 'https://jhubafrica.com/',
            'description': 'Innovation hub focused on innovations'
        },
    ]
    
    testimonials = [
        {
            'name': 'Dr. Sarah Kamau',
            'position': 'Chief Medical Officer, Kenyatta National Hospital',
            'image': 'images/testimonials/sarah_kamau.jpg',
            'quote': 'MamaGuardian AI has revolutionized how we approach maternal risk assessment. The predictive capabilities have helped us prioritize resources and save lives.',
        },
        {
            'name': 'Jane Wambui',
            'position': 'Midwife Supervisor, Kiambu County',
            'image': 'images/testimonials/jane_wambui.jpg',
            'quote': 'The user-friendly interface makes it easy for our healthcare workers to quickly identify high-risk cases, even in rural areas with limited resources.',
        },
        {
            'name': 'Prof. David Mwangi',
            'position': 'Director of Digital Health, Ministry of Health',
            'image': 'images/testimonials/david_mwangi.jpg',
            'quote': 'This innovation aligns perfectly with our national strategy to leverage AI for improving healthcare outcomes across Kenya.',
        },
    ]
    
    awards = [
        {
            'name': 'Best Health Tech Innovation',
            'year': '2024',
            'organization': 'Kenya Innovation Awards',
            'image': 'images/awards/innovation_award.png',
        },
        {
            'name': 'Global Health Impact Award',
            'year': '2023',
            'organization': 'World Health Summit',
            'image': 'images/awards/impact_award.png',
        },
        {
            'name': 'AI for Good Challenge Winner',
            'year': '2023',
            'organization': 'Google.org',
            'image': 'images/awards/ai_good_award.png',
        },
    ]

    return render(request, 'core/team.html', {
        'team': team, 
        'partners': partners,
        'testimonials': testimonials,
        'awards': awards
    })

def technical(request):
    return render(request, 'core/technical.html')
def gallery(request):
    return render(request, 'core/gallery.html')

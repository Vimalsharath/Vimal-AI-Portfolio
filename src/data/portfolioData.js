const portfolioData = {

  personal: {
    name: "R. V. Vimal",
    role: "AI & Full Stack Developer",
    college: "SRM Valliammai Engineering College",
    branch: "Computer Science and Engineering",
    cgpa: "8.54",

    email: "vimal141205@gmail.com",
    github: "https://github.com/Vimalsharath",
    linkedin: "https://linkedin.com/in/vimal-r-v-aba06b298?",

    resume: "/resume.pdf",
  },


  about:
    "I am a Computer Science Engineering student passionate about Artificial Intelligence, Machine Learning, Deep Learning, Generative AI and Full Stack Development. I enjoy building intelligent applications that solve real-world problems.",


  education: {
    degree: "B.E Computer Science and Engineering",
    college: "SRM Valliammai Engineering College",
    cgpa: "8.54",
  },


  skills: {

    Programming: [
      "Python",
      "Java",
      "C",
      "JavaScript",
      "HTML",
      "CSS"
    ],

    AI_ML: [
      "Machine Learning",
      "Deep Learning",
      "Generative AI",
      "RAG",
      "LangChain",
      "ChromaDB"
    ],

    Frameworks: [
      "React",
      "FastAPI"
    ],

    Tools: [
      "Git",
      "GitHub",
      "VS Code"
    ]

  },


  internships: [
   {
      company: "FutureIntern",
      role: "Web Development Intern",
      duration: "2025",
      description:
        "Developed portfolio website and weather forecasting application using API integration."
    }

  ],


  certifications: [

    "AWS Certified Cloud Practitioner",

    "NCVET Skill Competency Certification",

    "Forage / TATA - Data Visualization: Empowering Business with Effective Insights",

    "Python for Data Science Internship Certificate",

    "Prince Infotech Technical Workshop"

  ],



  projects: [

    {
      title:
      "AI Portfolio with RAG Chatbot",

      image:
      "/images/portfolio.png",

      technologies:[
        "React",
        "FastAPI",
        "LangChain",
        "ChromaDB",
        "Groq"
      ],

      description:
      "AI-powered portfolio website that uses Retrieval Augmented Generation to answer questions about my resume, skills and projects."
    },


    {
      title:
      "Alzheimer's Disease Prediction",

      image:
      "/images/alzheimer.png",

      technologies:[
        "Python",
        "TensorFlow",
        "RCNN",
        "ResNet50"
      ],

      description:
      "Deep learning model using RCNN with ResNet50 backbone to classify Alzheimer's MRI images."
    },

{
      title:
      "Weather Forecasting Application",

      image:
      "/images/weather.png",

      technologies:[
        "HTML",
        "CSS",
        "JavaScript",
        "Weather API"
      ],

      description:
      "Weather application providing real-time weather information using API integration."
    },


    {
      title:
      "Police Department ERP Model",

      image:
      "/images/police.png",

      technologies:[
        "Java",
        "Database",
        "ERP"
      ],

      description:
      "ERP system for police case registration, assignment and deployment management."
    }

  ]

};


export default portfolioData;
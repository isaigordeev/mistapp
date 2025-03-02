def generate_prompt(exp, role):
    return f"""
    Given the following text description of a person's role and skills, and a specific job role description, classify the most appropriate LinkedIn job title. The classification should be as precise as possible, ensuring it aligns with common LinkedIn role categories.

    Text Description:
    {exp}

    Role Description:
    {role}

    Based on this information, output only a binary decision (1 or 0).
    """





experience = """Isai Gordeev
École Polytechnique
72, Boulevard des Maréchaux, Palaiseau, 91120 isai.gordeev.2022@polytechnique.org, github.com/isaigordeev
EDUCATION
École Polytechnique, Palaiseau, France
Engineer’s Degree
Moscow Institute of Physics and Technology, Dolgoprudny, Russia
Bachelor’s Degree
EXPERIENCE
2022 – curr.
2019 – 2023
  Causal inference for multivariate time series, Machine Learning Engineer Ai-Vidence, France
Developed a generation pipeline of synthetic multivariate time series.
Developed a pipeline for causal inference using a state-of-the-art transformer model (CGTST) to discover summary adjacency graphs for multivariate time series. 2024
Port congestion prediction with GNN, Machine Learning Engineer
CGM CMA, France
Developed a package for congestion pipeline prediction. Led a team of 3 students in experiment conduction.
Designed and trained a model based on graph attention, transformer encoders, and tabular embeddings trained on an internal congestion dataset in the target port network 2023 – 2024
Phase Lipid Classification Project, Intern
Laboratory for Advanced Studies of Membrane Proteins, Russia
Developed a package for lipid lattice phase classification based on convolutional and transfor-
mer models, trained on SASX synthetic and real data
PROJECTS
Low-resource Language Translator
2022 – 2023
 Mined corpus for a low-resourced language including OCR recognition (tesseract).
Fine-tuned a family of translation purpose models (NLLB, MADLAD)
Notetaking web-application
Developed a minimal note-taking application using an idea of hyperlinks based on PHP ba- ckend. 2023
PUBLICATIONS
FLORES+ translation and machine translation evaluation for the Erzya language
approved for WMT24, Miami, Florida, USA 2024
SKILLS
code : Python, C++, shell, SQL
stack : torch, tensorflow, transformers, pandas, numpy, sklearn
technologies : cython, tesseract, git, manim, dataiku, vim, docker, eigen, pygame natural languages : Russian, French, English
AWARDS AND HONORS
2023 – 2024
   Eiffel Excellence scholarship All-Russian MIPT Physics Olympiad
2022 – 2025 2017, 2018, 2019"""



sample_lead_role = """At Mistral AI, we're on a mission to revolutionize the world with cutting-edge AI technology. We're a dynamic, passionate team spread across Europe, the UK, the USA and Asia, united by our passion for AI and our drive to make it ubiquitous and accessible.

We're looking for an AI Deployment Lead to join our Solutions team and help our customers unlock the full potential of AI. In this role, you'll be at the forefront of deploying our advanced models and products, tackling real-world challenges, and ensuring our customers achieve their most ambitious goals.

If you're passionate about AI, thrive in competitive environments, and love making a tangible impact, this is the role for you. Join us and be part of a team that's shaping the future of technology.
Role Summary
As our AI Deployment Lead, you'll be the catalyst driving the adoption and scaling of cutting-edge AI solutions. It's a purely IC role.
You'll work at the intersection of innovation and impact, empowering businesses to leverage GenAI for transformative results.
You'll guide companies in integrating GenAI solutions, making AI a tangible part of their operations.
You'll drive the scaling of GenAI technologies, ensuring seamless transitions from concept to production.
You'll partner closely with our product and science teams to deliver state-of-the-art AI solutions tailored to client needs.
You'll tackle complex business problems with AI, delivering measurable outcomes and strategic advantages.
You'll contribute to the evolution of AI technology, influencing how businesses operate and compete in the modern world.
Key responsibilities
Delivering value to the customers
Execute on effective technical discovery to understand potential clients' needs, challenges, and desired outcomes in collaboration with Account Executives.
Contribute to effectively identifying, qualifying, and disqualifying opportunities where Mistral solutions can unlock the most value for the customer. 
On the project, Influence evaluation criteria and gain control of evaluations and the evaluation process
Create a strategic vision for the customer on the project, based on a deep understanding of their strategy, desired positive business outcomes, and required capabilities.  

Product deployment
Guide and support customers in deploying our models and products into their infrastructure.
Work closely with customers to deploy relevant solutions according to their specific requirements.
Regularly liaise with the product and technical teams to relay feedback and suggest improvements.
Develop custom features for customers as needed.

Project management
Define and track success metrics of the POC being rolled out at customers.
Operate as a program leader, leveraging internal Mistral teams (Applied Engineers) as well as teams on the customer side to make sure project moves forward.
You may be a good fit if
You hold a degree in a relevant scientific field (e.g., Computer Science, Data Science, Engineering, etc.).
You have been involved in a customer facing role
You have strong project & stakeholder management skills
You are proficient in developing custom prototypes using frameworks in Python or Javascript
You have foundational knowledge in AI/ML/Data science
You have ability to connect technology and business value 
You are result driven and resilient
Ideally you have
Familiarity with sales qualification concepts"""

sample_junior_role = """As an Applied Engineering Intern, you will work closely with our Applied AI Engineering team to facilitate the adoption of Mistral AI products among customers and collaborate with them to address complex technical challenges. This role is based in Paris, with an internship duration of 3 to 6 months. We are open to CIFRE programs as a continuation after the internship.
Key Responsibilities
Contribute to the deployment of state-of-the-art GenAI applications, driving technological transformation with our customers.
Collaborate with researchers, AI engineers, and product engineers on complex customer projects.
Work with the product and science team to continuously improve our product and model capabilities based on customer feedback.
You may be a good fit if
You are currently pursuing a degree in AI, data science, or a related field from a tier 1 engineering school or university.
You have strong programming skills in Python.
You are familiar with machine learning algorithms and natural language processing techniques.
You hold basic understanding of MLOps and deploying machine learning use cases.
You have good communication skills with the ability to explain technical concepts to both technical and non-technical audiences.
Ideally you have
Experience with deep learning frameworks such as PyTorch.
Familiarity with version control systems (e.g., Git) and Linux shell environment.
Experience working in HPC Environments
Publication record in AI or a related field
Benefits
🥕 Food : Daily lunch vouchers
🥎 Sport : Monthly contribution to a Gympass subscription
🚴 Transportation : Monthly contribution to a mobility pass"""


STANDART_PROMPT = generate_prompt(experience, sample_junior_role)

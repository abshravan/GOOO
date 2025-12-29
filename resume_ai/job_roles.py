"""
Job Roles Module
Contains static job role definitions and required skills mapping
"""

# Comprehensive job roles with their required skills
JOB_ROLES = {
    "Software Engineer": [
        "python", "java", "javascript", "c++", "c#", "programming",
        "data structures", "algorithms", "git", "version control",
        "api", "rest", "sql", "debugging", "testing", "agile"
    ],
    "Frontend Developer": [
        "html", "css", "javascript", "typescript", "react", "vue",
        "angular", "frontend", "ui", "ux", "responsive design",
        "webpack", "npm", "git", "web development"
    ],
    "Backend Developer": [
        "python", "java", "node.js", "go", "ruby", "php",
        "api", "rest", "graphql", "database", "sql", "nosql",
        "mongodb", "postgresql", "mysql", "microservices", "docker"
    ],
    "Full Stack Developer": [
        "javascript", "python", "java", "react", "node.js",
        "html", "css", "database", "sql", "api", "rest",
        "frontend", "backend", "git", "agile", "docker"
    ],
    "Data Scientist": [
        "python", "r", "machine learning", "statistics", "data analysis",
        "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",
        "sql", "data visualization", "jupyter", "deep learning"
    ],
    "Machine Learning Engineer": [
        "python", "machine learning", "deep learning", "tensorflow",
        "pytorch", "scikit-learn", "neural networks", "nlp", "computer vision",
        "model deployment", "mlops", "docker", "kubernetes", "aws", "gcp"
    ],
    "Data Engineer": [
        "python", "sql", "etl", "data pipeline", "spark", "hadoop",
        "airflow", "kafka", "data warehouse", "bigquery", "redshift",
        "aws", "azure", "gcp", "scala", "java"
    ],
    "Data Analyst": [
        "sql", "excel", "python", "r", "data analysis", "statistics",
        "tableau", "power bi", "data visualization", "reporting",
        "business intelligence", "analytics"
    ],
    "DevOps Engineer": [
        "linux", "docker", "kubernetes", "ci/cd", "jenkins", "terraform",
        "ansible", "aws", "azure", "gcp", "bash", "python",
        "monitoring", "git", "infrastructure as code"
    ],
    "Cloud Engineer": [
        "aws", "azure", "gcp", "cloud", "terraform", "kubernetes",
        "docker", "networking", "security", "ci/cd", "linux",
        "infrastructure", "serverless", "lambda"
    ],
    "Mobile App Developer": [
        "swift", "kotlin", "java", "react native", "flutter",
        "ios", "android", "mobile development", "ui/ux", "api",
        "rest", "firebase", "git", "app deployment"
    ],
    "iOS Developer": [
        "swift", "objective-c", "ios", "xcode", "uikit", "swiftui",
        "cocoapods", "mobile development", "app store", "git", "api"
    ],
    "Android Developer": [
        "kotlin", "java", "android", "android studio", "jetpack",
        "mobile development", "google play", "firebase", "git", "api"
    ],
    "QA Engineer": [
        "testing", "qa", "selenium", "automation testing", "manual testing",
        "test cases", "bug tracking", "jira", "api testing", "python",
        "java", "quality assurance", "agile"
    ],
    "Product Manager": [
        "product management", "agile", "scrum", "roadmap", "user stories",
        "stakeholder management", "analytics", "wireframing", "jira",
        "communication", "leadership", "market research"
    ],
    "UI/UX Designer": [
        "ui design", "ux design", "figma", "sketch", "adobe xd",
        "wireframing", "prototyping", "user research", "usability testing",
        "design systems", "responsive design", "html", "css"
    ],
    "Security Engineer": [
        "cybersecurity", "security", "penetration testing", "vulnerability assessment",
        "networking", "firewalls", "encryption", "linux", "python",
        "security tools", "compliance", "incident response"
    ],
    "Database Administrator": [
        "sql", "database", "mysql", "postgresql", "oracle", "sql server",
        "database design", "optimization", "backup", "recovery",
        "performance tuning", "linux", "scripting"
    ],
    "Business Analyst": [
        "business analysis", "requirements gathering", "sql", "excel",
        "data analysis", "documentation", "stakeholder management",
        "process improvement", "agile", "jira", "communication"
    ],
    "System Administrator": [
        "linux", "windows server", "networking", "active directory",
        "bash", "powershell", "virtualization", "vmware", "security",
        "monitoring", "troubleshooting", "backup"
    ],
    "Network Engineer": [
        "networking", "cisco", "routing", "switching", "tcp/ip",
        "vpn", "firewalls", "load balancing", "dns", "network security",
        "troubleshooting", "network design"
    ],
    "Game Developer": [
        "c++", "c#", "unity", "unreal engine", "game development",
        "3d graphics", "physics", "game design", "scripting",
        "optimization", "git"
    ],
    "Blockchain Developer": [
        "blockchain", "solidity", "ethereum", "smart contracts", "web3",
        "cryptography", "javascript", "node.js", "rust", "go",
        "distributed systems"
    ],
    "AI/ML Researcher": [
        "machine learning", "deep learning", "research", "python",
        "tensorflow", "pytorch", "mathematics", "statistics",
        "nlp", "computer vision", "paper writing", "experimentation"
    ],
    "Site Reliability Engineer": [
        "sre", "linux", "kubernetes", "docker", "monitoring", "prometheus",
        "grafana", "python", "go", "incident response", "automation",
        "ci/cd", "cloud", "scalability"
    ],
    "Technical Writer": [
        "technical writing", "documentation", "api documentation",
        "markdown", "git", "editing", "communication", "technical knowledge",
        "user guides", "tutorials"
    ],
    "Solutions Architect": [
        "architecture", "cloud", "aws", "azure", "design patterns",
        "microservices", "api design", "scalability", "security",
        "technical leadership", "communication", "documentation"
    ],
    "Embedded Systems Engineer": [
        "c", "c++", "embedded systems", "microcontrollers", "embedded linux",
        "rtos", "hardware", "firmware", "debugging", "protocols",
        "electronics", "iot"
    ],
    "Computer Vision Engineer": [
        "computer vision", "deep learning", "opencv", "python",
        "tensorflow", "pytorch", "image processing", "object detection",
        "machine learning", "c++", "cuda"
    ],
    "NLP Engineer": [
        "nlp", "natural language processing", "machine learning", "python",
        "transformers", "bert", "gpt", "tensorflow", "pytorch",
        "text processing", "deep learning"
    ],
    "Research Scientist": [
        "research", "machine learning", "statistics", "python", "r",
        "mathematics", "experimentation", "paper writing", "data analysis",
        "scientific computing", "deep learning"
    ]
}


def get_all_job_roles() -> list:
    """
    Get list of all available job roles.

    Returns:
        List of job role names
    """
    return list(JOB_ROLES.keys())


def get_skills_for_role(role: str) -> list:
    """
    Get required skills for a specific job role.

    Args:
        role: Job role name

    Returns:
        List of required skills for the role
    """
    return JOB_ROLES.get(role, [])


def get_role_skills_mapping() -> dict:
    """
    Get the complete job role to skills mapping.

    Returns:
        Dictionary mapping job roles to their required skills
    """
    return JOB_ROLES.copy()

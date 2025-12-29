"""
Skill Extractor Module
Extracts skills from resume text and computes job role similarity
"""

import re
from typing import List, Dict, Tuple
from job_roles import get_role_skills_mapping


def normalize_skill(skill: str) -> str:
    """
    Normalize skill text for comparison.

    Args:
        skill: Raw skill text

    Returns:
        Normalized skill text (lowercase, no extra whitespace)
    """
    return skill.lower().strip()


def extract_skills_from_text(text: str) -> List[str]:
    """
    Extract potential skills from resume text using pattern matching.
    This is a simple fallback method if LLM extraction fails.

    Args:
        text: Resume text

    Returns:
        List of extracted skills
    """
    # Convert to lowercase for matching
    text_lower = text.lower()

    # Common technical skills and tools
    common_skills = [
        "python", "java", "javascript", "typescript", "c++", "c#", "ruby", "php", "go", "rust", "kotlin", "swift",
        "html", "css", "react", "vue", "angular", "node.js", "express", "django", "flask", "spring",
        "sql", "mysql", "postgresql", "mongodb", "redis", "elasticsearch",
        "aws", "azure", "gcp", "docker", "kubernetes", "terraform", "ansible",
        "git", "github", "gitlab", "jira", "agile", "scrum",
        "machine learning", "deep learning", "tensorflow", "pytorch", "scikit-learn",
        "data analysis", "data science", "statistics", "pandas", "numpy",
        "linux", "unix", "bash", "powershell",
        "rest api", "graphql", "microservices",
        "ci/cd", "jenkins", "github actions",
        "testing", "junit", "pytest", "selenium",
        "communication", "leadership", "teamwork", "problem solving"
    ]

    found_skills = []
    for skill in common_skills:
        if skill in text_lower:
            found_skills.append(skill.title())

    return list(set(found_skills))  # Remove duplicates


def parse_skills_from_llm_output(llm_output: str) -> List[str]:
    """
    Parse skills from LLM output (comma-separated or line-separated).

    Args:
        llm_output: Raw output from LLM

    Returns:
        List of parsed skills
    """
    # Remove common prefixes/suffixes
    output = llm_output.strip()

    # Try comma-separated first
    if ',' in output:
        skills = [s.strip() for s in output.split(',')]
    # Try newline-separated
    elif '\n' in output:
        skills = [s.strip() for s in output.split('\n')]
    # Try semicolon-separated
    elif ';' in output:
        skills = [s.strip() for s in output.split(';')]
    else:
        # Single skill or space-separated
        skills = [s.strip() for s in output.split()]

    # Clean up skills
    cleaned_skills = []
    for skill in skills:
        # Remove bullet points, numbers, etc.
        skill = re.sub(r'^[\d\.\-\*\•]+\s*', '', skill)
        skill = skill.strip()

        # Skip empty or very short strings
        if len(skill) > 1:
            cleaned_skills.append(skill)

    return cleaned_skills


def calculate_skill_match_score(candidate_skills: List[str], required_skills: List[str]) -> float:
    """
    Calculate similarity score between candidate skills and required skills.

    Args:
        candidate_skills: List of skills from candidate's resume
        required_skills: List of required skills for a job role

    Returns:
        Match score between 0.0 and 1.0
    """
    if not required_skills:
        return 0.0

    # Normalize all skills
    candidate_skills_norm = set(normalize_skill(s) for s in candidate_skills)
    required_skills_norm = set(normalize_skill(s) for s in required_skills)

    # Calculate exact matches
    exact_matches = candidate_skills_norm.intersection(required_skills_norm)

    # Calculate partial matches (e.g., "react.js" matches "react")
    partial_matches = 0
    for req_skill in required_skills_norm:
        if req_skill not in exact_matches:
            for cand_skill in candidate_skills_norm:
                if req_skill in cand_skill or cand_skill in req_skill:
                    partial_matches += 0.5
                    break

    # Calculate score
    total_matches = len(exact_matches) + partial_matches
    score = total_matches / len(required_skills_norm)

    return min(score, 1.0)  # Cap at 1.0


def rank_job_roles_by_skills(candidate_skills: List[str]) -> List[Tuple[str, float]]:
    """
    Rank all job roles based on candidate skills.

    Args:
        candidate_skills: List of skills from candidate's resume

    Returns:
        List of (job_role, score) tuples sorted by score (descending)
    """
    role_skills_mapping = get_role_skills_mapping()

    scores = []
    for role, required_skills in role_skills_mapping.items():
        score = calculate_skill_match_score(candidate_skills, required_skills)
        scores.append((role, score))

    # Sort by score descending
    scores.sort(key=lambda x: x[1], reverse=True)

    return scores


def format_job_roles_with_scores(ranked_roles: List[Tuple[str, float]], top_n: int = 10) -> str:
    """
    Format ranked job roles with scores for display or LLM input.

    Args:
        ranked_roles: List of (job_role, score) tuples
        top_n: Number of top roles to include

    Returns:
        Formatted string of job roles with scores
    """
    output = []
    for i, (role, score) in enumerate(ranked_roles[:top_n], 1):
        output.append(f"{i}. {role} - Similarity Score: {score:.2%}")

    return "\n".join(output)


def get_top_matching_roles(candidate_skills: List[str], top_n: int = 5) -> List[Dict]:
    """
    Get top N matching job roles for candidate skills.

    Args:
        candidate_skills: List of skills from candidate's resume
        top_n: Number of top roles to return

    Returns:
        List of dictionaries with role, score, and required_skills
    """
    ranked_roles = rank_job_roles_by_skills(candidate_skills)
    role_skills_mapping = get_role_skills_mapping()

    top_roles = []
    for role, score in ranked_roles[:top_n]:
        top_roles.append({
            "role": role,
            "score": score,
            "required_skills": role_skills_mapping[role]
        })

    return top_roles

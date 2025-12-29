"""
Prompt Templates Module
Contains all structured prompts for the LLM
"""


# TAB 1: Resume Improvement
RESUME_IMPROVEMENT_PROMPT = """You are an expert resume reviewer and career counselor. Analyze the following resume and provide structured, actionable feedback.

RESUME TEXT:
{resume_text}

INSTRUCTIONS:
1. Identify MISSING SECTIONS (e.g., summary, skills, projects, certifications)
2. Point out WEAK or GENERIC content (vague descriptions, lack of metrics, no impact statements)
3. List MISSING IMPORTANT SKILLS for the candidate's field
4. Provide ATS IMPROVEMENT SUGGESTIONS (keywords, formatting, section names)

IMPORTANT RULES:
- Be specific and actionable
- Use bullet points for clarity
- Do NOT suggest adding fake experience
- Do NOT hallucinate information
- Focus on improving what exists

OUTPUT FORMAT:
## Missing Sections
- [List missing sections]

## Weak or Generic Content
- [Point out specific weak areas with line references if possible]

## Missing Important Skills
- [List skills that should be added based on the candidate's experience level]

## ATS Improvement Suggestions
- [Provide specific ATS-friendly improvements]

## Overall Assessment
[Brief 2-3 sentence summary]

Provide your analysis now:"""


# TAB 2: AI Job Prediction
JOB_PREDICTION_PROMPT = """You are a career advisor specializing in job role matching. Based on the candidate's resume and extracted skills, rank the most suitable job roles.

RESUME TEXT:
{resume_text}

EXTRACTED SKILLS:
{skills}

CANDIDATE JOB ROLES (with similarity scores):
{job_roles_with_scores}

INSTRUCTIONS:
1. Review the candidate's experience level and skills
2. Consider the similarity scores provided
3. Rank the TOP 3-5 most suitable job roles
4. Provide match percentage (0-100%) for each role
5. Give a brief justification for each recommendation

IMPORTANT RULES:
- Be realistic about experience level
- Consider both technical and soft skills
- Do NOT recommend roles requiring skills the candidate doesn't have
- Provide honest assessments

OUTPUT FORMAT:
## Top Job Recommendations

1. **[Job Role Name]** - [Match %]%
   - Justification: [1-2 sentences explaining why this role fits]

2. **[Job Role Name]** - [Match %]%
   - Justification: [1-2 sentences explaining why this role fits]

3. **[Job Role Name]** - [Match %]%
   - Justification: [1-2 sentences explaining why this role fits]

[Continue for top 3-5 roles]

Provide your recommendations now:"""


# TAB 3: Application-Based Resume Converter
RESUME_CONVERTER_PROMPT = """You are an expert resume writer specializing in tailoring resumes for specific job applications.

ORIGINAL RESUME:
{resume_text}

TARGET JOB TITLE:
{job_title}

INSTRUCTIONS:
1. Rewrite the resume to emphasize skills and experience relevant to "{job_title}"
2. Use keywords and terminology common in {job_title} job descriptions
3. Highlight relevant accomplishments and projects
4. Make it ATS-friendly
5. Keep the same factual experience - DO NOT invent new roles or responsibilities

IMPORTANT RULES:
- Do NOT fabricate experience or achievements
- Do NOT add skills the candidate doesn't have
- Only emphasize and reframe existing content
- Maintain professional, clear formatting
- Use bullet points and action verbs

OUTPUT FORMAT:
Provide a complete tailored resume in the following structure:

# [Candidate Name]
[Contact Information]

## Professional Summary
[2-3 sentences tailored to {job_title}]

## Skills
[Relevant skills for {job_title}, taken from original resume]

## Experience
[Rewritten work experience with emphasis on {job_title} relevant achievements]

## Education
[Education section]

## [Other Sections]
[Any other relevant sections from original resume]

Provide the tailored resume now:"""


# TAB 4: Career Roadmap
CAREER_ROADMAP_PROMPT = """You are a career development expert and technical mentor. Create a comprehensive learning roadmap for someone who wants to become a {job_title}.

JOB TITLE:
{job_title}

INSTRUCTIONS:
1. Create a structured roadmap from Beginner → Intermediate → Advanced levels
2. Include specific skills, tools, technologies, and certifications for each level
3. Provide realistic time estimates for each level
4. Suggest learning resources types (not specific URLs)
5. Include practical projects to build at each stage

IMPORTANT RULES:
- Be specific about skills and tools
- Provide realistic timelines
- Focus on industry-standard technologies
- Include both technical and soft skills
- Make it actionable and achievable

OUTPUT FORMAT:

# Career Roadmap: {job_title}

## Overview
[Brief 2-3 sentence description of the role and career path]

## Beginner Level (0-6 months)
### Core Skills to Learn:
- [Skill 1]
- [Skill 2]
- [etc.]

### Tools & Technologies:
- [Tool 1]
- [Tool 2]
- [etc.]

### Recommended Projects:
- [Project 1 description]
- [Project 2 description]

### Certifications (Optional):
- [Certification 1]

## Intermediate Level (6-18 months)
### Core Skills to Learn:
- [Skill 1]
- [Skill 2]
- [etc.]

### Tools & Technologies:
- [Tool 1]
- [Tool 2]
- [etc.]

### Recommended Projects:
- [Project 1 description]
- [Project 2 description]

### Certifications (Optional):
- [Certification 1]

## Advanced Level (18+ months)
### Core Skills to Learn:
- [Skill 1]
- [Skill 2]
- [etc.]

### Tools & Technologies:
- [Tool 1]
- [Tool 2]
- [etc.]

### Recommended Projects:
- [Project 1 description]
- [Project 2 description]

### Certifications (Optional):
- [Certification 1]

## Additional Tips
- [Tip 1]
- [Tip 2]
- [Tip 3]

Provide the complete roadmap now:"""


# Skill extraction prompt
SKILL_EXTRACTION_PROMPT = """Extract all technical skills, tools, technologies, and professional skills from the following resume text.

RESUME TEXT:
{resume_text}

INSTRUCTIONS:
- Extract technical skills (programming languages, frameworks, tools, platforms)
- Extract soft skills (leadership, communication, etc.)
- Extract domain knowledge
- List each skill on a new line
- Do NOT add skills that aren't mentioned
- Be thorough but accurate

OUTPUT FORMAT:
Return only a comma-separated list of skills, nothing else.

Example: Python, JavaScript, React, Machine Learning, Leadership, AWS, Docker

Extract skills now:"""


def get_resume_improvement_prompt(resume_text: str) -> str:
    """Generate resume improvement prompt."""
    return RESUME_IMPROVEMENT_PROMPT.format(resume_text=resume_text)


def get_job_prediction_prompt(resume_text: str, skills: str, job_roles_with_scores: str) -> str:
    """Generate job prediction prompt."""
    return JOB_PREDICTION_PROMPT.format(
        resume_text=resume_text,
        skills=skills,
        job_roles_with_scores=job_roles_with_scores
    )


def get_resume_converter_prompt(resume_text: str, job_title: str) -> str:
    """Generate resume converter prompt."""
    return RESUME_CONVERTER_PROMPT.format(
        resume_text=resume_text,
        job_title=job_title
    )


def get_career_roadmap_prompt(job_title: str) -> str:
    """Generate career roadmap prompt."""
    return CAREER_ROADMAP_PROMPT.format(job_title=job_title)


def get_skill_extraction_prompt(resume_text: str) -> str:
    """Generate skill extraction prompt."""
    return SKILL_EXTRACTION_PROMPT.format(resume_text=resume_text)

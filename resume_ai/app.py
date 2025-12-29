"""
Local AI Resume & Career Assistant
Main Gradio Application with 4 tabs
"""

import gradio as gr
from llm import create_llm_client
from resume_parser import parse_resume, validate_resume_text
from skill_extractor import (
    parse_skills_from_llm_output,
    rank_job_roles_by_skills,
    format_job_roles_with_scores,
    extract_skills_from_text
)
from prompts import (
    get_resume_improvement_prompt,
    get_job_prediction_prompt,
    get_resume_converter_prompt,
    get_career_roadmap_prompt,
    get_skill_extraction_prompt
)
from utils import (
    save_uploaded_file,
    validate_file_type,
    truncate_text,
    format_error_message,
    check_text_length
)


# Global LLM client
llm_client = None


def initialize_llm(model_name: str = "llama3.1"):
    """Initialize the LLM client."""
    global llm_client
    try:
        llm_client = create_llm_client(model=model_name)
        if llm_client.is_available():
            return f"✅ Connected to Ollama with model: {model_name}"
        else:
            return "❌ Cannot connect to Ollama. Please ensure it's running."
    except Exception as e:
        return format_error_message(e)


# ===================================
# TAB 1: Resume Improvement
# ===================================
def improve_resume(resume_file):
    """
    Analyze resume and provide improvement suggestions.

    Args:
        resume_file: Uploaded resume file

    Returns:
        Improvement suggestions
    """
    try:
        if resume_file is None:
            return "❌ Please upload a resume file."

        # Validate file type
        file_path = save_uploaded_file(resume_file)
        if not validate_file_type(file_path):
            return "❌ Please upload a PDF or DOCX file."

        # Parse resume
        resume_text = parse_resume(file_path)

        if not validate_resume_text(resume_text):
            return "❌ Could not extract meaningful text from the resume. Please check the file."

        # Check text length
        is_valid, estimated_tokens, message = check_text_length(resume_text)
        if not is_valid:
            resume_text = truncate_text(resume_text, max_length=8000)

        # Generate prompt
        prompt = get_resume_improvement_prompt(resume_text)

        # Call LLM
        if llm_client is None:
            return "❌ LLM client not initialized. Please restart the application."

        response = llm_client.generate(prompt, temperature=0.3, max_tokens=2048)

        return response

    except Exception as e:
        return format_error_message(e)


# ===================================
# TAB 2: AI Job Prediction
# ===================================
def predict_jobs(resume_file):
    """
    Predict suitable job roles based on resume.

    Args:
        resume_file: Uploaded resume file

    Returns:
        Job predictions with match percentages
    """
    try:
        if resume_file is None:
            return "❌ Please upload a resume file."

        # Validate file type
        file_path = save_uploaded_file(resume_file)
        if not validate_file_type(file_path):
            return "❌ Please upload a PDF or DOCX file."

        # Parse resume
        resume_text = parse_resume(file_path)

        if not validate_resume_text(resume_text):
            return "❌ Could not extract meaningful text from the resume. Please check the file."

        # Truncate if needed
        resume_text = truncate_text(resume_text, max_length=8000)

        # Extract skills using LLM
        skill_prompt = get_skill_extraction_prompt(resume_text)

        if llm_client is None:
            return "❌ LLM client not initialized. Please restart the application."

        skills_output = llm_client.generate(skill_prompt, temperature=0.2, max_tokens=500)

        # Parse skills
        candidate_skills = parse_skills_from_llm_output(skills_output)

        # If LLM extraction failed, use fallback
        if not candidate_skills:
            candidate_skills = extract_skills_from_text(resume_text)

        if not candidate_skills:
            return "❌ Could not extract skills from the resume. Please ensure the resume contains relevant skills."

        # Rank job roles
        ranked_roles = rank_job_roles_by_skills(candidate_skills)

        # Format for LLM
        job_roles_formatted = format_job_roles_with_scores(ranked_roles, top_n=10)
        skills_formatted = ", ".join(candidate_skills)

        # Generate job prediction
        prediction_prompt = get_job_prediction_prompt(
            resume_text=resume_text[:3000],  # Truncate for context
            skills=skills_formatted,
            job_roles_with_scores=job_roles_formatted
        )

        response = llm_client.generate(prediction_prompt, temperature=0.4, max_tokens=1500)

        return response

    except Exception as e:
        return format_error_message(e)


# ===================================
# TAB 3: Application-Based Resume Converter
# ===================================
def convert_resume(resume_file, job_title):
    """
    Tailor resume for specific job application.

    Args:
        resume_file: Uploaded resume file
        job_title: Target job title

    Returns:
        Tailored resume
    """
    try:
        if resume_file is None:
            return "❌ Please upload a resume file."

        if not job_title or len(job_title.strip()) == 0:
            return "❌ Please enter a target job title."

        # Validate file type
        file_path = save_uploaded_file(resume_file)
        if not validate_file_type(file_path):
            return "❌ Please upload a PDF or DOCX file."

        # Parse resume
        resume_text = parse_resume(file_path)

        if not validate_resume_text(resume_text):
            return "❌ Could not extract meaningful text from the resume. Please check the file."

        # Truncate if needed
        resume_text = truncate_text(resume_text, max_length=8000)

        # Generate conversion prompt
        prompt = get_resume_converter_prompt(resume_text, job_title.strip())

        if llm_client is None:
            return "❌ LLM client not initialized. Please restart the application."

        response = llm_client.generate(prompt, temperature=0.5, max_tokens=3000)

        return response

    except Exception as e:
        return format_error_message(e)


# ===================================
# TAB 4: Career Roadmap
# ===================================
def generate_roadmap(job_title):
    """
    Generate career roadmap for a job title.

    Args:
        job_title: Target job title

    Returns:
        Career roadmap
    """
    try:
        if not job_title or len(job_title.strip()) == 0:
            return "❌ Please enter a job title."

        # Generate roadmap prompt
        prompt = get_career_roadmap_prompt(job_title.strip())

        if llm_client is None:
            return "❌ LLM client not initialized. Please restart the application."

        response = llm_client.generate(prompt, temperature=0.6, max_tokens=3000)

        return response

    except Exception as e:
        return format_error_message(e)


# ===================================
# Gradio UI
# ===================================
def create_ui():
    """Create Gradio interface with tabs."""

    with gr.Blocks(title="Local AI Resume & Career Assistant", theme=gr.themes.Soft()) as app:
        gr.Markdown(
            """
            # 📄 Local AI Resume & Career Assistant

            **Powered by Local LLMs via Ollama**

            This application helps you improve your resume, predict suitable job roles,
            tailor resumes for specific applications, and generate career roadmaps.

            **Note:** Ensure Ollama is running with `ollama serve` and you have pulled a model like `llama3.1`.
            """
        )

        # Status indicator
        status_text = gr.Textbox(
            label="System Status",
            value=initialize_llm(),
            interactive=False,
            lines=2
        )

        with gr.Tabs():
            # ===================================
            # TAB 1: Resume Improvement
            # ===================================
            with gr.Tab("📝 Resume Improvement"):
                gr.Markdown(
                    """
                    Upload your resume to get detailed improvement suggestions including:
                    - Missing sections
                    - Weak or generic content
                    - Missing important skills
                    - ATS optimization tips
                    """
                )

                with gr.Row():
                    with gr.Column():
                        resume_file_1 = gr.File(
                            label="Upload Resume (PDF or DOCX)",
                            file_types=[".pdf", ".docx", ".doc"]
                        )
                        improve_btn = gr.Button("🔍 Analyze Resume", variant="primary")

                    with gr.Column():
                        improvement_output = gr.Textbox(
                            label="Improvement Suggestions",
                            lines=20,
                            placeholder="Upload a resume and click 'Analyze Resume' to get feedback..."
                        )

                improve_btn.click(
                    fn=improve_resume,
                    inputs=[resume_file_1],
                    outputs=[improvement_output]
                )

            # ===================================
            # TAB 2: AI Job Prediction
            # ===================================
            with gr.Tab("🎯 AI Job Prediction"):
                gr.Markdown(
                    """
                    Upload your resume to discover the most suitable job roles based on your skills.
                    Get top 3-5 job recommendations with match percentages and justifications.
                    """
                )

                with gr.Row():
                    with gr.Column():
                        resume_file_2 = gr.File(
                            label="Upload Resume (PDF or DOCX)",
                            file_types=[".pdf", ".docx", ".doc"]
                        )
                        predict_btn = gr.Button("🎯 Predict Job Roles", variant="primary")

                    with gr.Column():
                        prediction_output = gr.Textbox(
                            label="Job Predictions",
                            lines=20,
                            placeholder="Upload a resume and click 'Predict Job Roles' to see recommendations..."
                        )

                predict_btn.click(
                    fn=predict_jobs,
                    inputs=[resume_file_2],
                    outputs=[prediction_output]
                )

            # ===================================
            # TAB 3: Application-Based Resume Converter
            # ===================================
            with gr.Tab("✏️ Resume Converter"):
                gr.Markdown(
                    """
                    Tailor your resume for a specific job application.
                    Enter the target job title and get an optimized, ATS-friendly resume.
                    """
                )

                with gr.Row():
                    with gr.Column():
                        resume_file_3 = gr.File(
                            label="Upload Resume (PDF or DOCX)",
                            file_types=[".pdf", ".docx", ".doc"]
                        )
                        job_title_input = gr.Textbox(
                            label="Target Job Title",
                            placeholder="e.g., Senior Software Engineer, Data Scientist, Product Manager",
                            lines=1
                        )
                        convert_btn = gr.Button("✏️ Convert Resume", variant="primary")

                    with gr.Column():
                        conversion_output = gr.Textbox(
                            label="Tailored Resume",
                            lines=20,
                            placeholder="Upload a resume, enter a job title, and click 'Convert Resume'..."
                        )

                convert_btn.click(
                    fn=convert_resume,
                    inputs=[resume_file_3, job_title_input],
                    outputs=[conversion_output]
                )

            # ===================================
            # TAB 4: Career Roadmap
            # ===================================
            with gr.Tab("🗺️ Career Roadmap"):
                gr.Markdown(
                    """
                    Generate a comprehensive learning roadmap for any career path.
                    Get structured guidance from Beginner to Advanced levels with skills, tools, and timelines.
                    """
                )

                with gr.Row():
                    with gr.Column():
                        roadmap_job_title = gr.Textbox(
                            label="Job Title",
                            placeholder="e.g., Machine Learning Engineer, Full Stack Developer",
                            lines=1
                        )
                        roadmap_btn = gr.Button("🗺️ Generate Roadmap", variant="primary")

                    with gr.Column():
                        roadmap_output = gr.Textbox(
                            label="Career Roadmap",
                            lines=20,
                            placeholder="Enter a job title and click 'Generate Roadmap'..."
                        )

                roadmap_btn.click(
                    fn=generate_roadmap,
                    inputs=[roadmap_job_title],
                    outputs=[roadmap_output]
                )

        # Footer
        gr.Markdown(
            """
            ---
            **Tips:**
            - Ensure Ollama is running: `ollama serve`
            - Install model if needed: `ollama pull llama3.1`
            - For best results, use clear and detailed resumes
            - All processing is done locally on your machine
            """
        )

    return app


if __name__ == "__main__":
    app = create_ui()
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )

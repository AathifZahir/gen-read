from google import genai

client = genai.Client(api_key="AIzaSyCFF3UdJo4ETZ2xyYftPDNyIel90pi_fXM")


def gemini_transform(txt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"""I'm working on a software project and need a well-structured and professional README.md file. 
        Please generate a complete README that includes the project title, a clear description of what the project does, 
        a list of key features, the technologies used (tech stack), setup and installation instructions, 
        usage guidelines with example commands, any configuration or environment variables required, 
        API documentation (if applicable), instructions for contributing, the license type, and contact information. 
        Format it using Markdown and include appropriate code blocks for installation and usage. Use this code 
        \n {txt}""",
    )
    print(response.text)
    return response.text

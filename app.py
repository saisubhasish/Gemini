import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

from logger import logger

load_dotenv(find_dotenv())

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Blog post with AI\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "## The Paradox of Progress: How AI is Shaping Our Future\n\nThe rise of artificial intelligence (AI) has sparked a wave of both excitement and fear. Some see it as the harbinger of a utopian future, where machines solve our problems and free us to pursue higher aspirations. Others envision a dystopian world dominated by intelligent machines, where humans become obsolete and enslaved. This essay argues that the impact of AI is a complex paradox, offering immense potential for progress while simultaneously posing unprecedented challenges.\n\nOn the one hand, AI is already revolutionizing numerous fields. In healthcare, AI-powered tools are assisting doctors in diagnosing diseases with greater accuracy and developing personalized treatments. In transportation, self-driving cars promise to increase safety and efficiency while reducing traffic congestion. In education, AI-powered tutors can personalize learning experiences and cater to individual needs. These are just a few examples of how AI is transforming our lives for the better.\n\nHowever, the rapid advancement of AI also raises significant concerns. One major worry is the potential for job displacement. As AI automates tasks previously performed by humans, many jobs are at risk. This could lead to widespread unemployment and economic instability, particularly for those with lower levels of education and skills.\n\nAnother concern is the ethical implications of AI. For example, the use of facial recognition technology raises privacy issues, while the development of autonomous weapons systems raises the specter of a future war fought by machines. These are complex ethical dilemmas that require careful consideration and thoughtful regulation.\n\nFurthermore, the increasing power of AI raises questions about its potential impact on our own intelligence and autonomy. As AI systems become more sophisticated, they may eventually surpass human intelligence in certain areas. This could lead to a situation where humans become increasingly reliant on AI, potentially eroding our own critical thinking skills and decision-making abilities.\n\nIn conclusion, the impact of AI on our future is both promising and fraught with danger. While AI offers unprecedented opportunities for progress and innovation, it also poses significant challenges that we must address carefully. It is essential to foster responsible development and deployment of AI technologies, ensuring that they are used for the benefit of humanity and not against it. Only through a combination of technological advancements, ethical considerations, and robust societal dialogue can we navigate the paradox of progress and unlock the true potential of AI for a better future. \n",
      ],
    },
  ]
)

input_data = input("Please enter your message: ")

logger.info(f"User Input: {input_data}")

response = chat_session.send_message(input_data)

logger.info(f"AI Response: {response.text}")

print(response.text)
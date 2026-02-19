import google.generativeai as genai

genai.configure(api_key="AIzaSyB8BYQGmm6GA1eabQdYPsqF3KMzJo5IQZo")

for m in genai.list_models():
    print(m.name)

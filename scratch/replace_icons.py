import os

path = r'd:\SLIIT\Year 04 Semester 1\Research Project\research website\ELDEASE-WEBSITE\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '<i class="fa-brands fa-flutter"></i>': '<img src="images/tech/flutter.svg" alt="Flutter" style="width: 35px; height: 35px;" />',
    '<i class="fa-brands fa-python"></i>': '<img src="images/tech/python.svg" alt="Python" style="width: 35px; height: 35px;" />',
    '<i class="fas fa-bolt"></i>': '<img src="images/tech/fastapi.svg" alt="FastAPI" style="width: 35px; height: 35px;" />',
    '<i class="fas fa-fire"></i>': '<img src="images/tech/firebase.svg" alt="Firebase" style="width: 35px; height: 35px;" />',
    '<i class="fas fa-brain"></i>': '<img src="images/tech/tensorflow.svg" alt="TensorFlow" style="width: 35px; height: 35px;" />',
    '<i class="fas fa-comments"></i>': '<img src="images/tech/nlp.svg" alt="NLP" style="width: 35px; height: 35px;" />',
    '<i class="fas fa-robot"></i>': '<img src="images/tech/ml.svg" alt="Machine Learning" style="width: 35px; height: 35px;" />',
    '<i class="fas fa-microphone-lines"></i>': '<img src="images/tech/whisper.svg" alt="Whisper AI" style="width: 35px; height: 35px;" />'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html with tech images')

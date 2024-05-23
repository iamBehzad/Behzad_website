from django.shortcuts import render

# Create your views here.
def index_view(request):
    context = {'Name': 'Behzad',  'Profile':'Internship', 'Phone': '+98 914 346 5560','Email': 'behzad.Abbasy@gmail.com' ,
               'About' : 'I am a PhD candidate with extensive experience in machine learning, deep learning, reinforcement learning,'
                    'image processing, machine vision, natural language processing, and optimization/metaheuristic algorithms,'
                    'including evolutionary computation and swarm intelligence. I have experience developing Machine learning'
                    'algorithms using Python and popular libraries such as PyTorch, TensorFlow, Keras, OpenCV, NLTK, Scikit-learn,'
                    'and etc.' }
    return render(request, 'website/index.html', context)
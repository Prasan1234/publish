from django.shortcuts import HttpResponse


# Create your views here.

def home(request):
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is </p>
        </body>
    </html>
    '''
    return HttpResponse(html)
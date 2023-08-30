from django.shortcuts import HttpResponse


# Create your views here.

def home(request):
    html = f'''
    <html>
        <body>
            <h1>Prasanth</h1>
            <p>From django </p>
        </body>
    </html>
    '''
    return HttpResponse(html)

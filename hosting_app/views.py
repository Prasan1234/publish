from django.shortcuts import HttpResponse


# Create your views here.

def home(request):
    html = f'''
    <html>
        <body>
            <h1>Prasanth</h1>
            <h1>Tesing vercel deployment </h1> 
            <p>using django </p>
        </body>
    </html>
    '''
    return HttpResponse(html)

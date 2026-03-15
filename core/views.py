from django.http import HttpResponse

def home_view(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Red Product API - Dashboard</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f7f6; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .card { background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); text-align: center; max-width: 500px; }
            h1 { color: #e63946; margin-bottom: 10px; }
            p { color: #457b9d; font-size: 1.1rem; }
            .status { display: inline-block; padding: 5px 15px; background: #a7c957; color: white; border-radius: 20px; font-weight: bold; font-size: 0.9rem; margin-top: 10px; }
            .links { margin-top: 20px; text-align: left; background: #f1faee; padding: 15px; border-radius: 8px; }
            a { color: #1d3557; text-decoration: none; font-weight: bold; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🔴 Red Product Backend</h1>
            <p>Le serveur API est opérationnel et prêt à servir le frontend.</p>
            <div class="status">● Serveur en ligne</div>
            <div class="links">
                <strong>Accès rapides :</strong><br>
                🚀 <a href="/api/hotels/">Liste des Hôtels (API)</a><br>
                🔐 <a href="/admin/">Interface Administration</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)
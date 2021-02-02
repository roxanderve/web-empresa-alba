from .models import Link

def context_dict(request): # diccionara para extender el contexto de las redes sociales
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx
from django.shortcuts import render

#Paso 6: Crear las vistas usando variables
def inicio(request): #PASO 13: Reemplazo contenido para que se adapte a mi idea
    contexto = {
        'titulo': 'El Despertar del Héroe',
        'texto': 'Has despertado en los campos de Hyrule. Eres Link, un joven destinado a grandes aventuras. A lo lejos ves el Bosque Kokiri, hogar de tu infancia, y el majestuoso Castillo Hyrule. Una voz misteriosa te susurra: "El destino de Hyrule está en tus manos". ¿Qué camino elegirás?',
        'imagen': 'https://easycdn.es/1/imagenes/the-legend-of-zelda-breath-of-the-wild-nintendo-switch_344428.jpg',
        'opciones': [
            {'url': 'bosque', 'texto': 'Explorar el Bosque Kokiri'},
            {'url': 'castillo', 'texto': 'Dirigirse al Castillo de Hyrule'}
        ]
    } 
    return render(request, 'historia/pagina.html', contexto)

#Link en el bosque: Encuentra la Espada Kokiri
def bosque(request):
    contexto = {
        'titulo': 'El Bosque Kokiri',
        'texto': 'El bosque esta lleno de vida y miesterio. Los Kokiri, niños eternos del bosque, te saludan con curiosidad. En el Gran Árbol Deku encuentras la legendaria Espada Kokiri brillando con una luz mágica. El tomarla, sientes una energía ancestral recorrer tu cuerpo. Ahora puedes elegir: ¿explorar el antiguo Templo del Tiempo o aventurarte hacia el Lago Hylia?',
        'imagen': 'https://via.placeholder.com/400', #Cambiar imagen 
        'opciones': [
            {'url': 'templo':'Entrar en el Templo del Tiempo'},
            {'url': 'lago': 'Explorar el Lago Hylia'}
        ]
    }
    return render(request, 'historia/pagina.html', contexto)

#Link en el Castillo: Link conoce a la Princesa Zelda
def castillo(request):
    contexto = {
        'titulo': 'El Castillo de Hyrule',
        'texto': 'Logras inflirtarte dentro del castillo y conoces a la Princesa Zelda. Ella te revela una profecía: Ganondorf, el rey del desierto, planea apoderarse de la Trifuerza y sumir a Hyrule en la oscuridad. Zelda te pide que reúnas las tres Piedras Espirituales apra abrir la Puerta del Tiempo y detenerlo. Esta es una misión peligrosa... ¿Aceptarás el llamado del destino?',
        'imagen': 'https://via.placeholder.com/400', #Cambair imagen
        'opciones': [
            {'url': 'mision', 'texto': 'Aceptar la misión de Zelda'},
            {'url': 'final_malo', 'texto': 'Rechazar y huir del castillo'}
        ]
    }
    return render(request, 'historia/pagina.html', contexto)

def templo(request):
    contexto = {
        'titulo': 'El Templo del Tiempo',
        'texto': 'Entras al sagrado Templo del Tiempo. Al colocar el Espada Maestra en su pedestal, una luz cegadora te envuelve. Has viajado 7 años al futuro. Ahora eres el Héroe del Tiempo, destinado a enfrentar a Ganondorf. Con valentía y determinación restauras la paz en Hyrule.',
        'imagen': 'https://via.placeholder.com/400', #Cambair imagen
    }
    return render(request, 'historia/final.html', contexto)

#Link conoce a los Zora
def lago(request):
    contexto = {
        'titulo': 'El Lago Hylia',
        'texto': 'Las aguas cristalinas',
        'imagen': 'https://via.placeholder.com/400'
    }
    return render(request, 'historia/final.html', contexto)

def final_malo(request):
    contexto = {
        'titulo': 'Final triste',
        'texto': 'Tus decisiones te han llevado a un final desafortunado.',
        'imagen': 'https://via.placeholder.com/400'
    }
    return render(request, 'historia/final.html', contexto)
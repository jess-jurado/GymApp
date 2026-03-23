import cloudinary
import cloudinary.api
from routes.rutina_routes import buscar_imagen_en_cloudinary

# Configuración de Cloudinary (la misma que en rutina_routes.py)
cloudinary.config(
    cloud_name='dntqaxsko',
    api_key='323523837582744',
    api_secret='ES85Ti4VrGNKOJ07wiBLBRFE8u8'
)

def verificar_imagenes_cloudinary():
    print("🔍 VERIFICANDO CLOUDINARY...")
    print("=" * 50)
    
    # Lista algunos ejercicios para probar
    ejercicios_prueba = [
        'Press de banca',
        'Sentadillas', 
        'Curl de bíceps',
        'Dominadas',
        'Press militar',
        'Peso muerto',
        'Fondos en paralelas',
        'Elevaciones laterales',
        'Crunch abdominal',
        'Plancha'
    ]
    
    print("📋 Probando búsqueda de imágenes...")
    for ejercicio in ejercicios_prueba:
        imagen_url = buscar_imagen_en_cloudinary(ejercicio)
        if imagen_url:
            print(f"✅ {ejercicio}: {imagen_url}")
        else:
            print(f"❌ {ejercicio}: NO ENCONTRADA")
    
    print("\n📊 Listando recursos en Cloudinary...")
    try:
        recursos = cloudinary.api.resources(type='upload', max_results=200)
        print(f"Total de imágenes en Cloudinary: {len(recursos['resources'])}")
        print("\nPrimeras 20 imágenes:")
        for recurso in recursos['resources']:
            print(f"   - {recurso['public_id']}")
    except Exception as e:
        print(f"❌ Error accediendo a Cloudinary: {e}")

if __name__ == "__main__":
    verificar_imagenes_cloudinary()
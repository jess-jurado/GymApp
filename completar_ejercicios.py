from config import get_db_connection

def completar_ejercicios():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # LISTA COMPLETA DE EJERCICIOS
    ejercicios_completos = [
        # ABDOMINALES - Core Profundo
        ('Ab_wheel', 'Abdominales', 'Core_Profundo', 'Ab_wheel'),
        ('Plancha_apoyo_antebrazos', 'Abdominales', 'Core_Profundo', 'Plancha_apoyo_antebrazos'),
        ('Plancha_balon_bosu', 'Abdominales', 'Core_Profundo', 'Plancha_balon_bosu'),
        ('Plank_to_push_up', 'Abdominales', 'Core_Profundo', 'Plank_to_push_up'),
        
        # ABDOMINALES - Inferiores
        ('Elevación_piernas_banco_inclinado', 'Abdominales', 'Inferiores', 'Elevación_piernas_banco_inclinado'),
        ('Elevación_rodillas_silla_romana', 'Abdominales', 'Inferiores', 'Elevación_rodillas_silla_romana'),
        ('Elevación_piernas_colgado_barra', 'Abdominales', 'Inferiores', 'Elevación_piernas_colgado_barra'),
        ('Futters_kicks', 'Abdominales', 'Inferiores', 'Futters_kicks'),
        ('Mountain_climbers', 'Abdominales', 'Inferiores', 'Mountain_climbers'),
        ('Plancha_elevacion_pierna', 'Abdominales', 'Inferiores', 'Plancha_elevacion_pierna'),
        
        # ABDOMINALES - Oblicuos
        ('Crunch_lateral_banco_inclinado', 'Abdominales', 'Oblicuos', 'Crunch_lateral_banco_inclinado'),
        ('Giro_polea_cuerda', 'Abdominales', 'Oblicuos', 'Giro_polea_cuerda'),
        ('Plancha_lateral_elevacion_cadera', 'Abdominales', 'Oblicuos', 'Plancha_lateral_elevacion_cadera'),
        ('Russian_twist_con_peso', 'Abdominales', 'Oblicuos', 'Russian_twist_con_peso'),
        ('Side_bends_mancuerna', 'Abdominales', 'Oblicuos', 'Side_bends_mancuerna'),
        
        # ABDOMINALES - Superiores
        ('Crunch_banco_inclinado', 'Abdominales', 'Superiores', 'Crunch_banco_inclinado'),
        ('Crunch_clasico', 'Abdominales', 'Superiores', 'Crunch_clasico'),
        ('Crunch_maquina', 'Abdominales', 'Superiores', 'Crunch_maquina'),
        ('Crunch_piernas_elevadas', 'Abdominales', 'Superiores', 'Crunch_piernas_elevadas'),
        ('Crunch_polea_alta', 'Abdominales', 'Superiores', 'Crunch_polea_alta'),
        ('Plancha_isometrica_tradicional', 'Abdominales', 'Superiores', 'Plancha_isometrica_tradicional'),
        
        # BICEPS - Basico_crecimiento
        ('Curl_banco_inclinado_mancuernas', 'Biceps', 'Basico_crecimiento', 'Curl_banco_inclinado_mancuernas'),
        ('Curl_barra_recta', 'Biceps', 'Basico_crecimiento', 'Curl_barra_recta'),
        ('Curl_barra_z', 'Biceps', 'Basico_crecimiento', 'Curl_barra_z'),
        ('Curl_concentrado', 'Biceps', 'Basico_crecimiento', 'Curl_concentrado'),
        ('Curl_mancuernas_alterno', 'Biceps', 'Basico_crecimiento', 'Curl_mancuernas_alterno'),
        ('Curl_martillo_mancuernas', 'Biceps', 'Basico_crecimiento', 'Curl_martillo_mancuernas'),
        ('Curl_polea_baja', 'Biceps', 'Basico_crecimiento', 'Curl_polea_baja'),
        
        # BICEPS - Polea_tension
        ('Curl_barra_polea_baja', 'Biceps', 'Polea_tension', 'Curl_barra_polea_baja'),
        ('Curl_maquina_scott_predicador', 'Biceps', 'Polea_tension', 'Curl_maquina_scott_predicador'),
        ('Curl_polea_alta', 'Biceps', 'Polea_tension', 'Curl_polea_alta'),
        ('Curl_polea_baja_martillo', 'Biceps', 'Polea_tension', 'Curl_polea_baja_martillo'),
        ('Polea_tension_polea_alta', 'Biceps', 'Polea_tension', 'Polea_tension_polea_alta'),
        
        # ESPALDA - Anchura_dorsales
        ('Jalon_convergente_maquina', 'Espalda', 'Anchura_dorsales', 'Jalon_convergente_maquina'),
        ('Jalon_pecho_maquina', 'Espalda', 'Anchura_dorsales', 'Jalon_pecho_maquina'),
        ('Pull_over_maquina', 'Espalda', 'Anchura_dorsales', 'Pull_over_maquina'),
        ('Remo_maquina_hammer_strength', 'Espalda', 'Anchura_dorsales', 'Remo_maquina_hammer_strength'),
        
        # ESPALDA - Grosor_parte_media
        ('Remo_inclinado_mancuernas', 'Espalda', 'Grosor_parte_media', 'Remo_inclinado_mancuernas'),
        ('Remo_mancuerna', 'Espalda', 'Grosor_parte_media', 'Remo_mancuerna'),
        
        # ESPALDA - Lumbar
        ('Hiperextensiones_banco', 'Espalda', 'Lumbar', 'Hiperextensiones_banco'),
        
        # ESPALDA - Trapecio
        ('Encogimiento_mancuernas', 'Espalda', 'Trapecio', 'Encogimiento_mancuernas'),
        ('Encogimiento_maquina', 'Espalda', 'Trapecio', 'Encogimiento_maquina'),
        
        # PECHO - Clavicular
        ('Apertura_mancuerna_banco', 'Pecho', 'Clavicular', 'Apertura_mancuerna_banco'),
        ('Apertura_maquina', 'Pecho', 'Clavicular', 'Apertura_maquina'),
        ('Press_mancuernas_banco_inclinado', 'Pecho', 'Clavicular', 'Press_mancuernas_banco_inclinado'),
        ('Press_maquina_inclinada', 'Pecho', 'Clavicular', 'Press_maquina_inclinada'),
        
        # PECHO - Esternocostal
        ('Apertura_mancuernas_banco_declinado', 'Pecho', 'Esternocostal', 'Apertura_mancuernas_banco_declinado'),
        ('Press_mancuernas_banco_declinado', 'Pecho', 'Esternocostal', 'Press_mancuernas_banco_declinado'),
        ('Press_maquina_declinada', 'Pecho', 'Esternocostal', 'Press_maquina_declinada'),
        
        # PECHO - Pecho_medio
        ('Apertura_mancuerna_banco_plano', 'Pecho', 'Pecho_medio', 'Apertura_mancuerna_banco_plano'),
        ('Apertura_maquina_peck_deck', 'Pecho', 'Pecho_medio', 'Apertura_maquina_peck_deck'),
        ('Press_mancuernas_banco_plano', 'Pecho', 'Pecho_medio', 'Press_mancuernas_banco_plano'),
        ('Press_maquina_plana', 'Pecho', 'Pecho_medio', 'Press_maquina_plana'),
        
        # PIERNAS - Cuadriceps
        ('Extensiones_pierna_maquina', 'Piernas', 'Cuadriceps', 'Extensiones_pierna_maquina'),
        ('Prensa_piernas', 'Piernas', 'Cuadriceps', 'Prensa_piernas'),
        ('Sentadilla_hack', 'Piernas', 'Cuadriceps', 'Sentadilla_hack'),
        ('Sentadilla_maquina_smith', 'Piernas', 'Cuadriceps', 'Sentadilla_maquina_smith'),
        ('Sentadillas_con_barra', 'Piernas', 'Cuadriceps', 'Sentadillas_con_barra'),
        ('Steps_ups_mancuernas', 'Piernas', 'Cuadriceps', 'Steps_ups_mancuernas'),
        ('Zancada_mancuerna', 'Piernas', 'Cuadriceps', 'Zancada_mancuerna'),
        
        # PIERNAS - Glúteos
        ('Abducción_cadera_maquina', 'Piernas', 'Glúteos', 'Abducción_cadera_maquina'),
        ('Hip_thrust_barra', 'Piernas', 'Glúteos', 'Hip_thrust_barra'),
        ('Patada_gluteo_polea', 'Piernas', 'Glúteos', 'Patada_gluteo_polea'),
        ('Puente_gluteos', 'Piernas', 'Glúteos', 'Puente_gluteos'),
        ('Sentadillas_bulgaras', 'Piernas', 'Glúteos', 'Sentadillas_bulgaras'),
        
        # PIERNAS - Isquiotibiales
        ('Curl_piernas_sentado_maquina', 'Piernas', 'Isquiotibiales', 'Curl_piernas_sentado_maquina'),
        ('Curl_piernas_tumbado_maquina', 'Piernas', 'Isquiotibiales', 'Curl_piernas_tumbado_maquina'),
        ('Peso_muerto_rumano', 'Piernas', 'Isquiotibiales', 'Peso_muerto_rumano'),
        
        # PIERNAS - Pantorrillas
        ('Elevaciones_talones_maquina', 'Piernas', 'Pantorrillas', 'Elevaciones_talones_maquina'),
        ('Saltos_mancuernas', 'Piernas', 'Pantorrillas', 'Saltos_mancuernas'),
        
        # TRICEPS - Mancuernas
        ('Extension_mancuerna', 'Triceps', 'Mancuernas', 'Extension_mancuerna'),
        ('Patada_triceps_mancuerna', 'Triceps', 'Mancuernas', 'Patada_triceps_mancuerna'),
        ('Press_cerrado', 'Triceps', 'Mancuernas', 'Press_cerrado'),
        ('Press_frances_mancuernas', 'Triceps', 'Mancuernas', 'Press_frances_mancuernas'),
        
        # TRICEPS - Maquinas
        ('Extension_asistida_maquina', 'Triceps', 'Maquinas', 'Extension_asistida_maquina'),
        ('Extension_maquina_cable', 'Triceps', 'Maquinas', 'Extension_maquina_cable'),
        ('Extension_maquina', 'Triceps', 'Maquinas', 'Extension_maquina'),
        ('Press_maquina', 'Triceps', 'Maquinas', 'Press_maquina')
    ]
    
    print("🔄 Insertando ejercicios...")
    ejercicios_insertados = 0
    ejercicios_existentes = 0
    
    for ejercicio in ejercicios_completos:
        nombre, grupo, subgrupo, imagen = ejercicio
        
        try:
            cursor.execute('''
                INSERT INTO Ejercicios (Nombre_ejercicio, Grupo_muscular, Subgrupo_muscular, imagen_url)
                VALUES (%s, %s, %s, %s)
            ''', (nombre, grupo, subgrupo, imagen))
            ejercicios_insertados += 1
            print(f"✅ Nuevo: {nombre}")
        except Exception as e:
            if "duplicate key" in str(e) or "already exists" in str(e):
                ejercicios_existentes += 1
                # print(f"⚠️ Ya existe: {nombre}")
            else:
                print(f"❌ Error con {nombre}: {e}")
    
    conn.commit()
    cursor.close()
    conn.close()
    
    print(f"\n🎯 RESUMEN:")
    print(f"   - Ejercicios insertados: {ejercicios_insertados}")
    print(f"   - Ejercicios ya existentes: {ejercicios_existentes}")
    print(f"   - Total en base de datos: {ejercicios_insertados + ejercicios_existentes}")

if __name__ == "__main__":
    completar_ejercicios()
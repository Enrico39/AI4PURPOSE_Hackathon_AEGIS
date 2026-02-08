# -----------------------------------------------------------------------------------------
# HELIOS
# Team AEGIS | AI4PURPOSE Hackathon
# -----------------------------------------------------------------------------------------
# DESCRIZIONE:
# Questo script simula il motore decisionale di Helios (Proof of Concept).
# Incrocia dati ambientali reali (SUHI by Latitudo 40) con dati sanitari sintetici simulati (Privacy compliant).
#
# REQUISITI:
# Inserire il file della mappa SUHI (.tif) nella cartella 'data/'
# -----------------------------------------------------------------------------------------

import os
import sys
import rasterio
import matplotlib.pyplot as plt
import numpy as np
import random

# --- CONFIGURAZIONE PATH DINAMICO (PER GITHUB) ---
# Ottiene la cartella dove si trova questo script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Costruisce il percorso relativo alla cartella 'data'
# NOME DEL FILE: Assicurati che il tuo file nella cartella 'data' abbia questo nome
filename = "naples_suhi.tif" 
file_path = os.path.join(base_dir, "data", filename)

def simulate_patients_on_map(path):
    print(f"--- ☀️ AVVIO PIATTAFORMA HELIOS ---")
    print(f"📁 Caricamento mappa da: {path}")
    
    # Controllo pre-esecuzione per aiutare l'utente
    if not os.path.exists(path):
        print(f"\n❌ ERRORE: File non trovato!")
        print(f"   Per far funzionare la demo:")
        print(f"   1. Crea una cartella chiamata 'data' nello stesso posto di questo script.")
        print(f"   2. Inserisci il file della mappa SUHI al suo interno.")
        print(f"   3. Rinomina il file in '{filename}' o aggiorna la variabile nel codice.\n")
        return

    try:
        with rasterio.open(path) as src:
            # Leggi i dati RGB per la visualizzazione
            data = src.read([1, 2, 3])
            plot_data = np.transpose(data, (1, 2, 0))
            height, width = data.shape[1], data.shape[2]
            
            # --- GENERAZIONE PAZIENTI FINTI (MOCK DATA) ---
            print("🔄 Simulazione incrocio dati Anagrafe Fragilità (So.Re.Sa)...")
            patients = []
            target_patients = 80 # Numero di soggetti simulati
            
            while len(patients) < target_patients:
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
                
                # CONTROLLO ANTI-SFONDO NERO (Esclude mare e bordi)
                pixel_vals = data[:, y, x]
                if np.sum(pixel_vals) < 20: 
                    continue
                
                # Simulazione Fragilità (Randomizzata per la Demo)
                is_fragile = random.choice([True, False, True]) 
                
                # Analisi Calore SUHI (Logica: Tanto Rosso + Poco Blu = Caldo)
                r_val = pixel_vals[0]
                b_val = pixel_vals[2]
                is_hot_zone = (r_val > 130) and (b_val < 110)
                
                # --- HELIOS DECISION LOGIC ---
                if is_fragile and is_hot_zone:
                    status = "CRITICO"
                    color = '#FF0000' # Rosso Puro (Kill Zone)
                    size = 200
                    zorder = 10
                elif is_fragile:
                    status = "WATCHLIST"
                    color = '#FF8C00' # Arancione (Rischio Monitorato)
                    size = 100
                    zorder = 5
                else:
                    status = "SICURO"
                    color = '#00FF00' # Verde (Safe)
                    size = 50
                    zorder = 1
                
                patients.append({'x': x, 'y': y, 'color': color, 'size': size, 'zorder': zorder})

            # --- DASHBOARD GRAFICA ---
            # Stile "Command Room" scuro
            plt.figure(figsize=(14, 12), facecolor='#0a0a0a') 
            ax = plt.gca()
            ax.set_facecolor('#0a0a0a')
            
            plt.imshow(plot_data)
            
            # Rendering Pazienti
            print("📍 Rendering visualizzazione tattica...")
            for p in patients:
                plt.scatter(p['x'], p['y'], c=p['color'], s=p['size'], 
                           edgecolors='black', linewidth=2.0, zorder=p['zorder']) 
            
            # TITOLO PROGETTO
            plt.title("HELIOS", fontsize=40, fontweight='bold', color='white', pad=20)
            
            # BARRA INFORMATIVA TATTICA
            reds = sum(1 for p in patients if p['color'] == '#FF0000')
            oranges = sum(1 for p in patients if p['color'] == '#FF8C00')
            
            info_text = f" TARGET ATTIVI: {target_patients}  |  🔴 CRITICITÀ ESTREME: {reds}  |  🟠 WATCHLIST: {oranges} "
            
            plt.text(width/2, height + (height*0.05), info_text, 
                     fontsize=14, color='white', fontfamily='monospace', fontweight='bold',
                     ha='center', va='center',
                     bbox=dict(facecolor='black', edgecolor='#333333', boxstyle='round,pad=0.6', linewidth=1))
            
            plt.axis('off')
            plt.tight_layout()
            
            print(f"✅ Dashboard generata con successo. Trovati {reds} casi critici.")
            plt.show()

    except Exception as e:
        print(f"❌ Errore imprevisto: {e}")

# Esecuzione
if __name__ == "__main__":
    simulate_patients_on_map(file_path)
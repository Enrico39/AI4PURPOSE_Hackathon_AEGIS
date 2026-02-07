# ☀️ HELIOS
### Heat Emergency Localized Intelligence Operating System
**Team AEGIS | AI4PURPOSE Hackathon 2026**

> **"Il caldo non colpisce a caso. Colpisce chirurgicamente."**

---

## 🚨 Il Problema
Le ondate di calore sono il "killer silenzioso" del cambiamento climatico. Attualmente, i piani di emergenza si basano su allerte meteo generiche rivolte all'intera popolazione. Questo approccio reattivo porta a:
* ❌ **Dispersione delle risorse** di soccorso in zone non critiche.
* ❌ **Mancata identificazione** dei soggetti realmente a rischio (es. chi assume psicofarmaci o vive in isole di calore).
* ❌ **Sovraccarico prevenibile** delle terapie intensive.

## 💡 La Soluzione: Helios
**Helios** non è una semplice app meteo. È un sistema operativo di **Data Fusion** che trasforma la gestione delle ondate di calore da reattiva a **predittiva**.

Il sistema incrocia in tempo reale due layer di dati fondamentali:
1.  **Dato Ambientale (Fisica):** L'intensità delle Isole di Calore Urbane (**SUHI**) fornita dai satelliti di **Latitudo 40**.
2.  **Dato Clinico (Biologia):** Il profilo di vulnerabilità dei cittadini estratto dai database sanitari regionali (**So.Re.Sa**).

Il risultato è una **mappa di rischio chirurgica** che permette alla Protezione Civile e al 118 di intervenire *prima* che si verifichi l'emergenza clinica.

---

## 🏗️ Architettura & Logica AI

Helios calcola un **Indice di Priorità di Intervento** basato sulla seguente logica:

> **RISCHIO = (SUHI Ambientale) x (Vettore Vulnerabilità)**

### 1. Layer Ambientale (Latitudo 40)
Utilizziamo i dati satellitari Sentinel-2 elaborati dall'AI di Latitudo 40:
* **SUHI (Surface Urban Heat Island):** Identifica con precisione (10m) le zone dove asfalto e cemento trattengono il calore.
* **HPR (Heatwave Risk):** Analisi morfologica del rischio urbano.

### 2. Layer Sanitario (Simulazione So.Re.Sa.)
Il sistema interroga l'Anagrafe Fragilità per identificare 4 cluster critici:
* 🔴 **Rischio Farmacologico:** Pazienti in cura con psicofarmaci/neurolettici (inibizione stimolo della sete).
* 🔴 **Rischio Clinico:** Cardiopatici, Nefropatici, Diabetici.
* 🔴 **Rischio Sociale:** Over-75 in nuclei monocomponente (solitudine).
* 🟠 **Rischio Anagrafico:** Over-65 generali.

---

## 💻 Dashboard Operativa

Il cuore di Helios è la **Command Room Dashboard**, che visualizza:

| Indicatore | Colore | Significato Operativo | Azione Automatica |
| :--- | :--- | :--- | :--- |
| **KILL ZONE** | 🔴 **Rosso** | Paziente Fragile in Zona SUHI Estrema | **Dispatch Ambulanza / Volontari** |
| **WATCHLIST** | 🟠 **Arancio** | Paziente Fragile in Zona Sicura | **Monitoraggio Attivo (SMS/Call)** |
| **SAFE ZONE** | 🟢 **Verde** | Paziente non a rischio / Zona Fresca | Nessuna azione (Risparmio Risorse) |

*(Inserire qui screenshot della mappa generata dallo script)*

---

# 🔒 Privacy & GDPR Compliance

Helios è progettato secondo i principi di **Privacy by Design** per garantire la protezione dei dati sensibili (So.Re.Sa.):

- **Separazione dei Dati**:  
  Il layer ambientale (Latitudo 40) è pubblico/anonimo. Il layer sanitario resta confinato nei server sicuri regionali.

- **Pseudo-Anonimizzazione**:  
  L'algoritmo di incrocio lavora su ID numerici criptati, non su nominativi in chiaro.

- **Last Mile Decryption**:  
  L'identità del paziente e l'indirizzo esatto vengono decriptati solo sul tablet dell'operatore di soccorso nel momento in cui scatta un intervento effettivo.

## 👥 Team AEGIS
- **Beniamino Nardone**   
- **Enrico Madonna**   
- **Lorenzo Mazza**   
- **Maria Carmela Vitale**   


---

Developed with ❤️ for **AI4PURPOSE Hackathon 2026 – Napoli**

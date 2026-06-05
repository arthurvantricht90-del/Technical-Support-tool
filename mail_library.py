# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:33:55 2026

@author: arthur.vantricht
"""


TEMPLATES = {

# ─────────────────────────────
# INTRO
# ─────────────────────────────


"intro.Mobile.General.English": """Dear customer,

Thank you for contacting DIGI Support. You told us you were experiencing issues with your mobile phone number {phone_no}.""",

"intro.Mobile.General.Dutch": """Beste klant,

Bedankt om contact op te nemen met DIGI Support. Je vertelde ons dat je problemen ondervond op je mobiele telefoonnummer {phone_no}.""",

"intro.Mobile.General.French": """Cher(e) client(e),

Merci d'avoir contacté DIGI Support. Vous nous avez signalé des problèmes avec votre numéro de téléphone mobile {phone_no}.""",



"intro.Mobile.APN.English": """We have investigated the cause of this problem and it appears to be due to an APN session that has become stuck, so to speak, meaning that you can now connect to the internet but cannot make any traffic.
To resolve this, please reset the current APN settings and then afterwards add a new one. You can do so as follows. It is important to note that some of these settings may not be accessible while a voice call is active.""",

"intro.Mobile.APN.Dutch": """We hebben gezocht naar de oorzaak van dit probleem en momenteel lijkt het erop dat dit te wijten is aan een APN sessie die als het ware vast is komen te zitten, waardoor je nu wel een internetverbinding kan maken, maar geen data kan verkrijgen.
Om dit op te lossen, gelieve de huidige APN instellingen te resetten/herstellen en daarna een nieuwe APN toe te voegen. Je kan dit doen door de onderstaande stappen te volgen. Het is belangrijk hierbij te vermelden dat sommige van deze instellingen niet beschikbaar zijn wanneer je tegelijkertijd een spraakoproep voert.""",

"intro.Mobile.APN.French": """Nous avons recherché la cause de ce problème et il semble actuellement qu'il soit dû à une session APN qui s'est en quelque sorte bloquée, ce qui vous permet de vous connecter à Internet, mais pas d'obtenir des données.
Pour résoudre ce problème, veuillez réinitialiser/restaurer les paramètres APN actuels, puis ajouter un nouvel APN. Pour ce faire, suivez les étapes ci-dessous. Il est important de noter que certains de ces paramètres ne sont pas disponibles lorsque vous passez un appel vocal.""",


"intro.Mobile.STK.English": """We have looked into your issue and have found that your phone is not properly registered on the network. To fix this, please follow the steps below.
The goal here is to reconnect your phone to the network, and, in doing so, clear any anomalies in the connection between your phone and the network.""",

"intro.Mobile.STK.Dutch": """We hebben uw probleem onderzocht en hebben vastgesteld dat uw telefoon momenteel niet correct is geregistreerd op het netwerk.
Het doel hiervan is om je telefoon weer met het netwerk te verbinden en zo eventuele storingen in de verbinding tussen je telefoon en het netwerk te verhelpen.""",

"intro.Mobile.STK.French": """Nous avons examiné votre problème et avons constaté que votre téléphone n'est pas correctement enregistré sur le réseau. 
L'objectif ici est de reconnecter votre téléphone au réseau et, ce faisant, de résoudre tout problème de connexion entre votre téléphone et le réseau.""",


"intro.Mobile.Roaming.English": """You informed us that you were unable to use your mobile phone while abroad.
We have looked into your case and would like the offer the following solution.
Please first make sure your SIM is configured correctly. Then, if needed, manually connect to the right operator. Finally, if necessary, reset your APN settings to make sure you can use mobile data.""",

"intro.Mobile.Roaming.Dutch": """Je vertelde ons dat je je mobiele telefoon niet kon gebruiken in het buitenland.
We hebben uw situatie bekeken en stellen u graag de volgende oplossing voor.
Controleer eerst of uw simkaart correct is geconfigureerd. Maak vervolgens, indien nodig, handmatig verbinding met de juiste provider. Reset ten slotte, indien nodig, uw APN-instellingen om ervoor te zorgen dat u mobiele data kunt gebruiken.""",

"intro.Mobile.Roaming.French": """Vous nous avez signalé que vous ne pouviez pas utiliser votre téléphone portable à l'étranger.
Nous avons examiné votre cas et souhaitons vous proposer la solution suivante.
Veuillez d'abord vous assurer que votre carte SIM est correctement configurée. Ensuite, si nécessaire, connectez-vous manuellement à l'opérateur approprié. Enfin, si besoin, réinitialisez vos paramètres APN pour vous assurer que vous pouvez utiliser les données mobiles.""",



"intro.Fix.English": """Dear customer,

Thank you for contacting Digi Support.
You told us you were experiencing fiber issues at home.""",

"intro.Fix.Dutch": """Beste klant,

Bedankt om contact op te nemen met Digi Support.
U vertelde ons dat je problemen ondervindt met uw fiber installatie.""",

"intro.Fix.French": """Cher client,

Merci d'avoir contacté le service d'assistance Digi.
Vous nous avez signalé que vous rencontrez des problèmes avec votre installation fibre optique.""",



"intro.OnlineServices.English": """Dear customer,

Thank you for contacting Digi Support.
You told us you were experiencing login issues on your MyDigi platform.""",

"intro.OnlineServices.Dutch": """Beste klant,

Bedankt om contact op te nemen met Digi Support.
Je vertelde ons dat je moeite ondervond bij het inloggen op je MyDigi platform.""",

"intro.OnlineServices.French": """Cher client,

Merci d'avoir contacté le service d'assistance Digi.
Vous nous avez signalé que vous rencontriez des problèmes de connexion sur votre plateforme MyDigi.""",


# ─────────────────────────────
# MIDDLE
# ─────────────────────────────


# Mobile
"middle.Mobile.IssueSolved.English": """We have investigated your issue and believe we were able to solve it.
You should therefore no longer experiences issues with your mobile phone number.""",

"middle.Mobile.IssueSolved.Dutch": """We hebben uw probleem onderzocht en denken dat we het hebben kunnen oplossen.
U zou dus geen problemen meer moeten ondervinden met uw mobiele nummer """,

"middle.Mobile.IssueSolved.French": """Nous avons examiné votre problème et pensons l'avoir résolu.
Vous ne devriez donc plus rencontrer de problèmes avec votre numéro de téléphone portable.""",


"middle.Mobile.Android.STK.header.English": """RECONFIGURE DIGI STK
    - On your Android device, look for the DIGI STK application
    - This application is automatically installed on your mobile phone the moment you insert the DIGI BE SIM in your mobile phone
    - Once located, open the application""",
    
"middle.Mobile.Android.STK.Idemia.English": """        - Select RBroker -> Account Selection -> Manual
        - Then, select RBroker again -> Country Menu -> DIGI Sponsor. Now wait until you have lost all service
        - Once service is gone, select RBroker once more -> Country Menu -> DIGI BE
        - Reboot your phone""",
        
 "middle.Mobile.Android.STK.Valid.English":"""       - Select Multi IMSI -> Select Mode -> Manual -> Select Roaming Broker. Now wait until you have lost all service
        - Then, select Multi IMSI again -> Select Mode -> Manual -> Select DIGI BE
        - Reboot your phone""",
        
    
        
"middle.Mobile.Android.STK.header.Dutch": """DIGI STK OPNIEUW CONFIGUREREN
    - Zoek op uw Android-apparaat naar de DIGI STK-applicatie
    - Deze applicatie wordt automatisch op uw mobiele telefoon geïnstalleerd zodra u de DIGI BE SIM in uw mobiele telefoon plaatst
    - Open de applicatie zodra u deze hebt gevonden""",
    
"middle.Mobile.Android.STK.Idemia.Dutch": """        - Selecteer RBroker -> Account Selection -> Country Menu
        - Selecteer vervolgens opnieuw RBroker -> Account Selection -> DIGI Sponsor. Wacht nu tot u alle service kwijt bent
        - Zodra de service weg is, selecteert u nogmaals RBroker -> Country Menu -> DIGI BE
        - Start uw telefoon opnieuw op""",
        
"middle.Mobile.Android.STK.Valid.Dutch": """        - Selecteer Multi IMSI -> Select Mode -> Manual -> Selecteer Roaming Broker. Wacht nu tot u geen service meer hebt
        - Selecteer vervolgens opnieuw Multi IMSI -> Select Mode -> Manual -> Selecteer DIGI BE
        - Activeer de vliegtuigstand gedurende enkele seconden""",
        
        
        
"middle.Mobile.Android.STK.header.French": """RECONFIGURER DIGI STK
    - Sur votre appareil Android, recherchez l'application DIGI STK
    - Cette application est automatiquement installée sur votre téléphone portable dès que vous insérez la carte SIM DIGI BE dans votre téléphone portable
    - Une fois localisée, ouvrez l'application""",
    
"middle.Mobile.Android.STK.Idemia.French": """        - Sélectionnez RBroker -> Sélection du compte -> Manuel
        - Ensuite, sélectionnez à nouveau RBroker -> Menu Pays -> DIGI Sponsor. Attendez maintenant jusqu'à ce que vous ayez perdu tout service
        - Une fois le service perdu, sélectionnez à nouveau RBroker -> Menu Pays -> DIGI BE
        - Redémarrez votre téléphone""",
        
"middle.Mobile.Android.STK.Valid.French": """        - Sélectionnez Multi IMSI -> Sélectionner le mode -> Manuel -> Sélectionner le courtier d'itinérance. Attendez maintenant jusqu'à ce que vous ayez perdu tout service
        - Ensuite, sélectionnez à nouveau Multi IMSI -> Sélectionner le mode -> Manuel -> Sélectionner DIGI BE
        - Activez le mode avion pendant quelques secondes""",
    


"middle.Mobile.Android.APN.English": """RESET APN SETTINGS    
    - On your Android device, go to Settings
    (- Connections)
    - Mobile Network
    - Access Point Names
    - Press 'Options' in the top right corner (the three dots)
    - Reset Access Points -> Reset
    - Press the '+' sign or Add APN
    - In the Name field, fill in 'DIGI BE'. In the APN field, fill in 'web'
    - Save the APN by selecting the check sign or by selecting Save APN
    - Now, select this newly created APN by colouring the circle next to it""",
    
"middle.Mobile.Android.APN.Dutch": """APN-INSTELLINGEN OPNIEUW INSTELLEN    
   - Ga op uw Android-apparaat naar Instellingen
   (- Verbindingen)
   - Mobiel netwerk
   - Toegangspuntnamen / Access Point Names / APN
   - Druk op 'Opties' in de rechterbovenhoek (de drie puntjes)
   - Toegangspunten resetten -> Resetten
   - Druk op het ‘+’-teken of 'APN toevoegen'
   - Vul in het veld Naam ‘DIGI BE’ in. Vul in het veld APN ‘web’ in
   - Sla de APN op door het vinkje te selecteren of door 'APN opslaan' te selecteren
   - Selecteer nu deze nieuw aangemaakte APN door het cirkeltje ernaast in te kleuren""",
   
"middle.Mobile.Android.APN.French": """RECONFIGURER LES PARAMÈTRES APN    
   - Sur votre appareil Android, accédez à Paramètres
   (- Connexions)
   - Réseau mobile
   - Noms des points d'accès / Access Point Names / APN
   - Appuyez sur 'Options' dans le coin supérieur droit (les trois points)
   - Réinitialiser les points d'accès -> Réinitialiser
   - Appuyez sur le signe « + » ou « Ajouter un APN »
   - Dans le champ Nom, saisissez « DIGI BE ». Dans le champ APN, saisissez « web »
   - Enregistrez l'APN en cochant la case ou en sélectionnant « Enregistrer l'APN »
   - Sélectionnez maintenant cet APN nouvellement créé en cochant la case à côté""",
   

"middle.Mobile.Android.Register.English": """MANUALLY SELECT OPERATOR
    - On your Android device, go to Settings
    (- Connections)
    - Mobile Network
    - Select Operator / Select Network 
    - Switch off Auto-select and search for the available operators
    - Once found, select DIGI BE and register on the network
    - Reboot your mobile phone  """,
    
"middle.Mobile.Android.Register.Dutch": """OPERATOR HANDMATIG SELECTEREN
    - Ga op uw Android-apparaat naar Instellingen
    (- Verbindingen)
    - Mobiel netwerk
    - Operator selecteren / Netwerk selecteren 
    - Schakel Automatisch selecteren uit en zoek naar de beschikbare operators
    - Selecteer DIGI BE zodra u deze hebt gevonden en registreer u op het netwerk
    - Start uw mobiele telefoon opnieuw op""",
    
"middle.Mobile.Android.Register.French": """SÉLECTION MANUELLE DE L'OPÉRATEUR
    - Sur votre appareil Android, allez dans Paramètres
    (- Connexions)
    - Réseau mobile
    - Sélectionner l'opérateur / Sélectionner le réseau 
    - Désactivez la sélection automatique et recherchez les opérateurs disponibles
    - Une fois trouvé, sélectionnez DIGI BE et enregistrez-vous sur le réseau
    - Redémarrez votre téléphone mobile""",
    


"middle.Mobile.Android.Roaming.header.English": """RECONFIGURE DIGI STK
    - On your Android device, look for the DIGI STK application
    - This application is automatically installed on your mobile phone the moment you insert the DIGI BE SIM in your mobile phone
    - Once located, open the application""",

"middle.Mobile.Android.Roaming.Idemia.English": """        - Select RBroker -> Account Selection -> Manual
        - Then, select RBroker again -> Country Menu -> DIGI BE
        - Reboot your phone

MANUALLY SELECT THE CORRECT OPERATOR (in case your phone doesn't automatically connect with a network after rebooting)
    - On your Android device, go to Settings
    (- Connections)
    - Mobile Network
    - Select Operator / Select Network 
    - Switch off Auto-select and search for the available operators
    - Select the operator that is compatible with DIGI BE. In XXX that would be XXX.
    - Once registered, toggle airplane mode

RESET APN SETTINGS (in case you can't use mobile data after manually selecting the operator')
    - On your Android device, go to Settings
    (- Connections)
    - Mobile Network
    - Access Point Names
    - Press 'Options' in the top right corner (the three dots)
    - Reset Access Points -> Reset
    - Press the '+' sign or Add APN
    - In the Name field, fill in 'DIGI BE'. In the APN field, fill in 'web'
    - Save the APN by selecting the check sign or by selecting Save APN
    - Now, select this newly created APN by colouring the circle next to it""",
    
"middle.Mobile.Android.Roaming.Valid.English": """        - Select Multi IMSI -> Select Mode -> Manual -> Select DIGI BE
        - Reboot your phone

MANUALLY SELECT THE CORRECT OPERATOR (in case your phone doesn't automatically connect with a network after rebooting)
    - On your Android device, go to Settings
    (- Connections)
    - Mobile Network
    - Select Operator / Select Network 
    - Switch off Auto-select and search for the available operators
    - Select the operator that is compatible with DIGI BE. In XXX that would be XXX.
    - Once registered, toggle airplane mode
    
RESET APN SETTINGS (in case you can't use mobile data after manually selecting the operator')
    - On your Android device, go to Settings
    (- Connections)
    - Mobile Network
    - Access Point Names
    - Press 'Options' in the top right corner (the three dots)
    - Reset Access Points -> Reset
    - Press the '+' sign or Add APN
    - In the Name field, fill in 'DIGI BE'. In the APN field, fill in 'web'
    - Save the APN by selecting the check sign or by selecting Save APN
    - Now, select this newly created APN by colouring the circle next to it""",
       

    
"middle.Mobile.Android.Roaming.header.Dutch": """DIGI STK OPNIEUW CONFIGUREREN
    - Zoek op uw Android-apparaat naar de DIGI STK-applicatie
    - Deze applicatie wordt automatisch op uw mobiele telefoon geïnstalleerd zodra u de DIGI BE SIM in uw mobiele telefoon plaatst
    - Open de applicatie zodra u deze hebt gevonden""",


"middle.Mobile.Android.Roaming.Idemia.Dutch": """        - Selecteer RBroker -> Account Selection -> Country Menu
        - Selecteer vervolgens opnieuw RBroker -> Account Selection -> DIGI BE
        - Start uw telefoon opnieuw op

SELECTEER HANDMATIG DE JUISTE OPERATOR (voor het geval je telefoon na het opnieuw opstarten niet automatisch verbinding maakt met een netwerk)
    - Ga op uw Android-apparaat naar Instellingen
    (- Verbindingen)
    - Mobiel netwerk
    - Selecteer Operator / Selecteer netwerk 
    - Schakel Automatisch selecteren uit en zoek naar de beschikbare operators
    - Selecteer de operator die compatibel is met DIGI BE. In XXX is dat XXX.
    - Schakel de vliegtuigmodus in zodra u bent geregistreerd

APN-INSTELLINGEN OPNIEUW INSTELLEN (in het geval dat je geen mobiele data kan gebruiken na het manueel selecteren van de juiste operator)    
   - Ga op uw Android-apparaat naar Instellingen
   (- Verbindingen)
   - Mobiel netwerk
   - Toegangspuntnamen / Access Point Names / APN
   - Druk op 'Opties' in de rechterbovenhoek (de drie puntjes)
   - Toegangspunten resetten -> Resetten
   - Druk op het ‘+’-teken of 'APN toevoegen'
   - Vul in het veld Naam ‘DIGI BE’ in. Vul in het veld APN ‘web’ in
   - Sla de APN op door het vinkje te selecteren of door 'APN opslaan' te selecteren
   - Selecteer nu deze nieuw aangemaakte APN door het cirkeltje ernaast in te kleuren""",

        
"middle.Mobile.Android.Roaming.Valid.Dutch": """        - Selecteer Multi IMSI -> Select Mode -> Manual -> Selecteer DIGI BE
        - Activeer de vliegtuigstand gedurende enkele seconden
        
SELECTEER HANDMATIG DE JUISTE OPERATOR (voor het geval je telefoon na het opnieuw opstarten niet automatisch verbinding maakt met een netwerk)
    - Ga op uw Android-apparaat naar Instellingen
    (- Verbindingen)
    - Mobiel netwerk
    - Selecteer Operator / Selecteer netwerk 
    - Schakel Automatisch selecteren uit en zoek naar de beschikbare operators
    - Selecteer de operator die compatibel is met DIGI BE. In XXX is dat XXX.
    - Schakel de vliegtuigmodus in zodra u bent geregistreerd

APN-INSTELLINGEN OPNIEUW INSTELLEN (in het geval dat je geen mobiele data kan gebruiken na het manueel selecteren van de juiste operator)    
   - Ga op uw Android-apparaat naar Instellingen
   (- Verbindingen)
   - Mobiel netwerk
   - Toegangspuntnamen / Access Point Names / APN
   - Druk op 'Opties' in de rechterbovenhoek (de drie puntjes)
   - Toegangspunten resetten -> Resetten
   - Druk op het ‘+’-teken of 'APN toevoegen'
   - Vul in het veld Naam ‘DIGI BE’ in. Vul in het veld APN ‘web’ in
   - Sla de APN op door het vinkje te selecteren of door 'APN opslaan' te selecteren
   - Selecteer nu deze nieuw aangemaakte APN door het cirkeltje ernaast in te kleuren""",   
        

    
"middle.Mobile.Android.Roaming.header.French": """RECONFIGURER DIGI STK
    - Sur votre appareil Android, recherchez l'application DIGI STK
    - Cette application est automatiquement installée sur votre téléphone portable dès que vous insérez la carte SIM DIGI BE dans votre téléphone portable
    - Une fois localisée, ouvrez l'application""",
    
"middle.Mobile.Android.Roaming.Idemia.French": """        - Sélectionnez RBroker -> Sélection du compte -> Manuel
        - Ensuite, sélectionnez à nouveau RBroker -> Menu Pays -> DIGI BE
        - Redémarrez votre téléphone
        
SÉLECTIONNEZ MANUELLEMENT L'OPÉRATEUR ADÉQUAT (au cas où votre téléphone ne se connecterait pas automatiquement à un réseau après le redémarrage)
    - Sur votre appareil Android, accédez à Paramètres
    (- Connexions)
    - Réseau mobile
    - Sélectionnez Opérateur / Sélectionner un réseau 
    - Désactivez la sélection automatique et recherchez les opérateurs disponibles
    - Sélectionnez l'opérateur compatible avec DIGI BE. Dans XXX, il s'agit de XXX.
    - Une fois enregistré, activez le mode avion
    
RECONFIGURER LES PARAMÈTRES APN (si vous ne parvenez pas à utiliser vos données mobiles après avoir sélectionné manuellement l'opérateur approprié)
   - Sur votre appareil Android, accédez à Paramètres
   (- Connexions)
   - Réseau mobile
   - Noms des points d'accès / Access Point Names / APN
   - Appuyez sur 'Options' dans le coin supérieur droit (les trois points)
   - Réinitialiser les points d'accès -> Réinitialiser
   - Appuyez sur le signe « + » ou « Ajouter un APN »
   - Dans le champ Nom, saisissez « DIGI BE ». Dans le champ APN, saisissez « web »
   - Enregistrez l'APN en cochant la case ou en sélectionnant « Enregistrer l'APN »
   - Sélectionnez maintenant cet APN nouvellement créé en cochant la case à côté""",    
   
"middle.Mobile.Android.Roaming.Valid.French": """        - Sélectionnez Multi IMSI -> Sélectionner le mode -> Manuel -> Sélectionner DIGI BE
        - Redémarrez votre téléphone
        
SÉLECTIONNEZ MANUELLEMENT L'OPÉRATEUR ADÉQUAT (au cas où votre téléphone ne se connecterait pas automatiquement à un réseau après le redémarrage)
    - Sur votre appareil Android, accédez à Paramètres
    (- Connexions)
    - Réseau mobile
    - Sélectionnez Opérateur / Sélectionner un réseau 
    - Désactivez la sélection automatique et recherchez les opérateurs disponibles
    - Sélectionnez l'opérateur compatible avec DIGI BE. Dans XXX, il s'agit de XXX.
    - Une fois enregistré, activez le mode avion
    
RECONFIGURER LES PARAMÈTRES APN (si vous ne parvenez pas à utiliser vos données mobiles après avoir sélectionné manuellement l'opérateur approprié)
   - Sur votre appareil Android, accédez à Paramètres
   (- Connexions)
   - Réseau mobile
   - Noms des points d'accès / Access Point Names / APN
   - Appuyez sur 'Options' dans le coin supérieur droit (les trois points)
   - Réinitialiser les points d'accès -> Réinitialiser
   - Appuyez sur le signe « + » ou « Ajouter un APN »
   - Dans le champ Nom, saisissez « DIGI BE ». Dans le champ APN, saisissez « web »
   - Enregistrez l'APN en cochant la case ou en sélectionnant « Enregistrer l'APN »
   - Sélectionnez maintenant cet APN nouvellement créé en cochant la case à côté""",

    


"middle.Mobile.iPhone.STK.header.English": """RECONFIGURE DIGI STK
    - On your iPhone device, go to Settings
    - Mobile Network
    (- Select your Digi BE SIM)
    - Simapps""",
    
"middle.Mobile.iPhone.STK.Idemia.English":"""        - Select RBroker -> Account Selection -> Manual
        - Then, select RBroker again -> Country Menu -> DIGI Sponsor. Now wait until you have lost all service
        - Once service is gone, select RBroker once more -> Country Menu -> DIGI BE
        - Reboot your phone""",
    
"middle.Mobile.iPhone.STK.Valid.English":"""        - Select Multi IMSI -> Select Mode -> Manual -> Select Roaming Broker. Now wait until you have lost all service
        - Then, select Multi IMSI again -> Select Mode -> Manual -> Select DIGI BE
        - Reboot your phone""",
        
        
"middle.Mobile.iPhone.STK.header.Dutch": """DIGI STK HERCONFIGUREREN
    - Ga op uw iPhone naar Instellingen.
    (- Selecteer je Digi BE-simkaart)
    - Mobiel netwerk
    - Simapps""",
    
"middle.Mobile.iPhone.STK.Idemia.Dutch": """        - Selecteer RBroker -> Account Selection -> Manual
        - Selecteer vervolgens opnieuw RBroker -> Country Menu -> DIGI Sponsor. Wacht nu tot u geen service meer hebt
        - Zodra de service weg is, selecteert u nogmaals RBroker -> Country Menu -> DIGI BE
        - Start uw telefoon opnieuw op""",
        
"middle.Mobile.iPhone.STK.Valid.Dutch": """        - Selecteer Multi IMSI -> Select Mode -> Manual -> Selecteer Roaming Broker. Wacht nu tot u alle service kwijt bent
        - Selecteer vervolgens opnieuw Multi IMSI -> Select Mode -> Manual -> Selecteer DIGI BE
        - Start uw telefoon opnieuw op""",
        
        
"middle.Mobile.iPhone.STK.header.French": """RECONFIGURER DIGI STK
    - Sur votre iPhone, allez dans Réglages.
    - Réseau mobile
    (- Sélectionnez votre carte SIM Digi BE)
    - Simapps""",
    
"middle.Mobile.iPhone.STK.Idemia.French": """        - Sélectionnez RBroker -> Account Selection -> Manual
        - Sélectionnez à nouveau RBroker -> Country Menu -> DIGI Sponsor. Attendez que vous n'ayez plus de service
        - Une fois le service interrompu, sélectionnez à nouveau RBroker -> Country Menu -> DIGI BE
        - Redémarrez votre téléphone""",
        
"middle.Mobile.iPhone.STK.Valid.French": """        - Sélectionnez Multi IMSI -> Select Mode -> Manual -> Sélectionner Roaming Broker. Attendez que vous n'ayez plus de service
        - Sélectionnez à nouveau Multi IMSI -> Select Mode -> Manual -> Sélectionner DIGI BE
        - Redémarrez votre téléphone""",
        

"middle.Mobile.iPhone.APN.English": """RESET APN SETTINGS
    - On your iPhone device, go to Setting.
    - Mobile Network
    - Mobile data network
    - Scroll down to Reset -> Reset
    - Next, in the MOBILE DATA section, fill in 'web' in the APN field. Leave the other fields empty
    - In the PERSONAL HOTSPOT section, fill in 'web' in the APN field. Leave the other fields empty
    - Switch on airplane mode for a couple of seconds to ensure the changes apply""",
    
"middle.Mobile.iPhone.APN.Dutch": """APN-INSTELLINGEN OPNIEUW INSTELLEN
    - Ga op je iPhone naar Instellingen
    - Mobiel netwerk
    - Mobiele datanetwerk
    - Scroll naar beneden tot aan 'Stel opnieuw in' -> Stel opnieuw in
    - Daarna, vul in de sectie MOBIELE DATA het veld APN in met 'web'. Laat de andere velden leeg
    - Vul in de sectie PERSOONLIJKE HOTSPOT het veld APN in met 'web'. Laat de andere velden leeg
    - Schakel vliegtuigmodus enkele seconden in om de wijzigingen toe te passen""",
    
"middle.Mobile.iPhone.APN.French": """RECONFIGURER LES PARAMÈTRES APN
    - Sur votre iPhone, allez dans Réglages
    - Réseau mobile
    - Réseau de données mobiles
    - Faites défiler vers le bas jusqu’à 'Réinitialiser' -> Réinitialiser
    - Apès, dans la section DONNÉES MOBILES, remplissez le champ APN avec 'web'. Laissez les autres champs vides
    - Dans la section PARTAGE DE CONNEXION, remplissez également le champ APN avec 'web'. Laissez les autres champs vides
    - Activez le mode avion pendant quelques secondes pour appliquer les modifications""",
    

"middle.Mobile.iPhone.Register.English": """MANUALLY SELECT OPERATOR
    - On your iPhone device, go to Settings
    - Mobile Network
    - Choose operator 
    - Switch off Auto-select and search for operators
    - Once found, select DIGI BE and register on the network
    - Reboot your mobile phone """,
    
"middle.Mobile.iPhone.Register.Dutch": """OPERATOR HANDMATIG SELECTEREN
    - Ga op je iPhone naar Instellingen
    - Mobiel netwerk
    - Kies Operator / Netwerkselectie
    - Schakel Automatisch selecteren uit en zoek handmatig naar netwerken
    - Zodra je DIGI BE ziet, selecteer dit en registreer op het netwerk
    - Herstart je mobiele telefoon""",
    
"middle.Mobile.iPhone.Register.French": """SÉLECTIONNER MANUELLEMENT L’OPÉRATEUR
    - Sur votre iPhone, allez dans Réglages
    - Réseau mobile
    - Choisissez Opérateur
    - Désactivez la sélection automatique et recherchez les opérateurs disponibles
    - Une fois DIGI BE trouvé, sélectionnez-le et enregistrez-vous sur le réseau
    - Redémarrez votre téléphone portable""",
    

"middle.Mobile.iPhone.Roaming.header.English": """RECONFIGURE DIGI STK
    - On your iPhone device, go to Settings
    - Mobile Network
    - Simapps""",
    
"middle.Mobile.iPhone.Roaming.Idemia.English":  """        - Select RBroker -> Account Selection -> Manual
        - Then, select RBroker again -> Country Menu -> DIGI BE
        - Reboot your phone

MANUALLY REGISTER ON THE CORRECT NETWORK (in case your phone doesn't automatically connect with a network after rebooting)
    - Settings
    - Mobile Network
    - Network Selection
    - Disable Automatic
    - Select the network that is most compatible with DIGI BE. In XXX, this is XXX.
    
RESET APN SETTINGS (in case you can't use mobile data after manually selecting the operator')
    - On your iPhone device, go to Setting.
    - Mobile Network
    - Mobile data network
    - Scroll down to Reset -> Reset
    - Next, in the MOBILE DATA section, fill in 'web' in the APN field. Leave the other fields empty
    - In the PERSONAL HOTSPOT section, fill in 'web' in the APN field. Leave the other fields empty
    - Switch on airplane mode for a couple of seconds to ensure the changes apply""",
        
        
"middle.Mobile.iPhone.Roaming.Valid.English": """        - Select Multi IMSI -> Select Mode -> Manual -> Select DIGI BE
        - Reboot your phone

MANUALLY REGISTER ON THE CORRECT NETWORK (in case your phone doesn't automatically connect with a network after rebooting)
    - Settings
    - Mobile Network
    - Network Selection
    - Disable Automatic
    - Select the network that is most compatible with DIGI BE. In XXX, this is XXX.
    
RESET APN SETTINGS (in case you can't use mobile data after manually selecting the operator')
    - On your iPhone device, go to Setting.
    - Mobile Network
    - Mobile data network
    - Scroll down to Reset -> Reset
    - Next, in the MOBILE DATA section, fill in 'web' in the APN field. Leave the other fields empty
    - In the PERSONAL HOTSPOT section, fill in 'web' in the APN field. Leave the other fields empty
    - Switch on airplane mode for a couple of seconds to ensure the changes apply""",

    

"middle.Mobile.iPhone.Roaming.header.Dutch": """DIGI STK HERCONFIGUREREN
    - Ga op uw iPhone naar Instellingen.
    - Mobiel netwerk
    - Simapps""",
    
    
"middle.Mobile.iPhone.Roaming.Idemia.Dutch": """        - Selecteer RBroker -> Account Selection -> Manual
        - Selecteer vervolgens opnieuw RBroker -> Country Menu -> DIGI Sponsor. Wacht nu tot u geen service meer hebt
        - Zodra de service weg is, selecteert u nogmaals RBroker -> Country Menu -> DIGI BE
        - Start uw telefoon opnieuw op
        
REGISTREER HANDMATIG OP HET JUISTE NETWERK (voor het geval je telefoon na het opnieuw opstarten niet automatisch verbinding maakt met een netwerk)
    - Instellingen
    - Mobiel netwerk
    - Netwerkselectie
    - Automatisch uitschakelen
    - Selecteer het netwerk dat het meest compatibel is met DIGI BE. In XXX is dit XXX.
    
APN-INSTELLINGEN OPNIEUW INSTELLEN (voor het geval je telefoon na het opnieuw opstarten niet automatisch verbinding maakt met een netwerk)
    - Ga op je iPhone naar Instellingen
    - Mobiel netwerk
    - Mobiele datanetwerk
    - Scroll naar beneden tot aan 'Stel opnieuw in' -> Stel opnieuw in
    - Daarna, vul in de sectie MOBIELE DATA het veld APN in met 'web'. Laat de andere velden leeg
    - Vul in de sectie PERSOONLIJKE HOTSPOT het veld APN in met 'web'. Laat de andere velden leeg
    - Schakel vliegtuigmodus enkele seconden in om de wijzigingen toe te passen""",
        

        
"middle.Mobile.iPhone.Roaming.Valid.Dutch": """        - Selecteer Multi IMSI -> Select Mode -> Manual -> Selecteer DIGI BE
        - Start uw telefoon opnieuw op
        
 REGISTREER HANDMATIG OP HET JUISTE NETWERK (voor het geval je telefoon na het opnieuw opstarten niet automatisch verbinding maakt met een netwerk)
     - Instellingen
     - Mobiel netwerk
     - Netwerkselectie
     - Automatisch uitschakelen
     - Selecteer het netwerk dat het meest compatibel is met DIGI BE. In XXX is dit XXX.
     
 APN-INSTELLINGEN OPNIEUW INSTELLEN (voor het geval je telefoon na het opnieuw opstarten niet automatisch verbinding maakt met een netwerk)
     - Ga op je iPhone naar Instellingen
     - Mobiel netwerk
     - Mobiele datanetwerk
     - Scroll naar beneden tot aan 'Stel opnieuw in' -> Stel opnieuw in
     - Daarna, vul in de sectie MOBIELE DATA het veld APN in met 'web'. Laat de andere velden leeg
     - Vul in de sectie PERSOONLIJKE HOTSPOT het veld APN in met 'web'. Laat de andere velden leeg
     - Schakel vliegtuigmodus enkele seconden in om de wijzigingen toe te passen""", 
        

    
"middle.Mobile.iPhone.Roaming.header.French": """RECONFIGURER DIGI STK
    - Sur votre iPhone, allez dans Réglages.
    - Réseau mobile
    - Simapps""",
    
"middle.Mobile.iPhone.Roaming.Idemia.French": """        - Sélectionnez RBroker -> Account Selection -> Manual
        - Sélectionnez à nouveau RBroker -> Country Menu -> DIGI BE
        - Redémarrez votre téléphone
        
INSCRIVEZ-VOUS MANUELLEMENT SUR LE RÉSEAU CORRECT (au cas où votre téléphone ne se connecterait pas automatiquement à un réseau après le redémarrage)
    - Paramètres
    - Réseau mobile
    - Sélection du réseau
    - Désactivez la sélection automatique
    - Sélectionnez le réseau le plus compatible avec DIGI BE. En XXX, il s'agit de XXX.
    
RECONFIGURER LES PARAMÈTRES APN (au cas où votre téléphone ne se connecterait pas automatiquement à un réseau après le redémarrage)
    - Sur votre iPhone, allez dans Réglages
    - Réseau mobile
    - Réseau de données mobiles
    - Faites défiler vers le bas jusqu’à 'Réinitialiser' -> Réinitialiser
    - Apès, dans la section DONNÉES MOBILES, remplissez le champ APN avec 'web'. Laissez les autres champs vides
    - Dans la section PARTAGE DE CONNEXION, remplissez également le champ APN avec 'web'. Laissez les autres champs vides
    - Activez le mode avion pendant quelques secondes pour appliquer les modifications""",
    
    
"middle.Mobile.iPhone.Roaming.Valid.French": """        - Sélectionnez Multi IMSI -> Select Mode -> Manual -> Sélectionner DIGI BE
        - Redémarrez votre téléphone
        
INSCRIVEZ-VOUS MANUELLEMENT SUR LE RÉSEAU CORRECT (au cas où votre téléphone ne se connecterait pas automatiquement à un réseau après le redémarrage)
    - Paramètres
    - Réseau mobile
    - Sélection du réseau
    - Désactivez la sélection automatique
    - Sélectionnez le réseau le plus compatible avec DIGI BE. En XXX, il s'agit de XXX.
    
RECONFIGURER LES PARAMÈTRES APN (au cas où votre téléphone ne se connecterait pas automatiquement à un réseau après le redémarrage)
    - Sur votre iPhone, allez dans Réglages
    - Réseau mobile
    - Réseau de données mobiles
    - Faites défiler vers le bas jusqu’à 'Réinitialiser' -> Réinitialiser
    - Apès, dans la section DONNÉES MOBILES, remplissez le champ APN avec 'web'. Laissez les autres champs vides
    - Dans la section PARTAGE DE CONNEXION, remplissez également le champ APN avec 'web'. Laissez les autres champs vides
    - Activez le mode avion pendant quelques secondes pour appliquer les modifications""",
        



# Fix
"middle.Fix.IssueSolved.English": """We have investigated your issue and believe we were able to solve it.
You should therefore no longer experience issues with your fibre internet.""",

"middle.Fix.IssueSolved.Dutch": """We hebben uw probleem onderzocht en denken dat we het hebben kunnen oplossen.
U zou dus geen problemen meer moeten ondervinden met uw fiber internet.""",

"middle.Fix.IssueSolved.French": """Nous avons examiné votre problème et pensons l'avoir résolu.
Vous ne devriez donc plus rencontrer de problèmes avec votre internet fibre.""",


"middle.Fix.SlowSpeedsChangesMade.English": """We've made a few changes to your network that should improve your connection speed.
Therefore, you should start seeing faster speeds from now on.""",

"middle.Fix.SlowSpeedsChangesMade.Dutch": """We hebben een aantal aanpasssingen gemaakt aan je netwerk die de snelheid zouden moeten optimaliseren.
Je zou dus vanaf nu hogere snelheden moeten ervaren.""",

"middle.Fix.SlowSpeedsChangesMade.French": """Nous avons apporté quelques modifications à votre réseau qui devraient permettre d'optimiser la vitesse.
Vous devriez donc bénéficier dès à présent d'une connexion plus rapide.""",


"middle.Fix.PoorCoverageChangesMade.English": """We've made some changes to your network that should improve coverage.
Therefore, you should start experiencing better coverage from now on.""",

"middle.Fix.PoorCoverageChangesMade.Dutch": """We hebben een aantal aanpasssingen gemaakt aan je netwerk die de netwerkdekking zouden moeten optimaliseren.
Je zou dus vanaf nu een betere dekking moeten ervaren.""",

"middle.Fix.PoorCoverageChangesMade.French": """Nous avons apporté quelques modifications à votre réseau qui devraient permettre d'optimiser la couverture.
Vous devriez donc bénéficier d'une meilleure couverture dès à présent.""",


"middle.Fix.TempOutageOngoing.English": """We have investigated your situation and, unfortunately, there is an ongoing outage on the fiber network, which has left you without internet.
We will do everything we can to resolve this issue as quickly as possible and restore your internet connection.""",

"middle.Fix.TempOutageOngoing.Dutch": """We hebben uw situatie onderzocht en helaas is er momenteel een storing op het glasvezelnetwerk waardoor u tijdelijk geen internetverbinding heeft.
We doen er alles aan om dit probleem zo snel mogelijk op te lossen en zo uw internetverbinding te herstellen.""",

"middle.Fix.TempOutageOngoing.French": """Nous avons examiné votre situation et, malheureusement, une panne est actuellement en cours sur le réseau fibre optique, ce qui vous prive d'accès à Internet.
Nous ferons tout notre possible pour résoudre ce problème dans les meilleurs délais et rétablir votre connexion Internet.""",


"middle.Fix.TempOutageSolved.English": """We have investigated your situation and found that there was a temporary network outage, which caused you to lose your internet connection for a short time.
However, this issue should have been resolved by now.""",

"middle.Fix.TempOutageSolved.Dutch": """We hebben uw situatie onderzocht en vonden dat er zich een tijdelijke storing heeft voorgedaan op het netwerk waardoor je even zonder internet bent gevallen.
Deze zou echter ondertussen opgelost moeten zijn.""",

"middle.Fix.TempOutageSolved.French": """Nous avons examiné votre situation et avons constaté qu'une panne temporaire s'était produite sur le réseau, ce qui vous a privé d'accès à Internet pendant un court instant.
Ce problème devrait toutefois être résolu à présent.""",


# Online services
"middle.OnlineServices.MailInSpam.English": """We’ve noticed that you’ve created an active MyDigi account using the email address XXX.
Normally, you should be able to log in to your MyDigi account using this email address and the password you chose.
However, you may need to go through the “Forgot Password” process. This is for security reasons. In that case, you should receive an email at the aforementioned email address. If you can’t find this email right away, be sure to check your spam and promotions folders. If you don’t find it there either, please let us know by replying to this email and including the date and time you last tried to receive a “Forgot Password” email—we’ll then see how we can help you further.
Even if you don’t receive the verification email, we’d like to ask you to try again and check to make sure the email hasn’t ended up in your spam or another folder. You may need to try a few times to receive the email, but it should definitely work.""",

"middle.OnlineServices.MailInSpam.Dutch": """We hebben gemerkt dat je een actief MyDigi account hebt aangemaakt met het mail adres XXX.
Normaal gezien zou je dus gewoon in staat moeten zijn om door gebruik te maken van dit mail adres en het wachtwoord dat je hebt gekozen in te loggen op je MyDigi account.
Wel is het mogelijk dat je de 'Wachtwoord Vergeten' procedure moet doorlopen. Dit is omwille van veiligheidsredenen. Je zou in dat geval een mail opgestuurd moeten krijgen naar het eerder vernoemde mail adres. Vind je deze mail niet meteen terug, kijk dan ook zeker in je spam en promoties folder. Vind je hem ook daar niet terug, laat ons dit dan zeker weten door te antwoorden op deze mail met daarin de datum en het tijdstip waarop je voor het laatst probeerde een 'Wachtwoord Vergeten' mail opgestuurd te krijgen - dan bekijken we zo hoe we je verder kunnen helpen.
Ook in het geval dat je de verificatiemail niet aankrijgt, zouden we je willen vragen nogmaals te proberen en te controleren of de mail zeker niet in je spam of in een andere folder is terechtgekomen. Het kan zijn dat je een aantal keer moet proberen de mail aan te krijgen, maar het zou zeker moeten werken.""",

"middle.OnlineServices.MailInSpam.French": """Nous avons constaté que vous avez créé un compte MyDigi actif avec l'adresse e-mail XXX.
Normalement, vous devriez donc pouvoir vous connecter à votre compte MyDigi en utilisant cette adresse e-mail et le mot de passe que vous avez choisi.
Il est toutefois possible que vous deviez suivre la procédure « Mot de passe oublié ». Cette mesure est prise pour des raisons de sécurité. Dans ce cas, vous devriez recevoir un e-mail à l'adresse mentionnée ci-dessus. Si vous ne trouvez pas cet e-mail immédiatement, pensez à vérifier vos dossiers de spam et de promotions. Si vous ne le trouvez pas non plus là-bas, veuillez nous en informer en répondant à cet e-mail en indiquant la date et l'heure auxquelles vous avez tenté pour la dernière fois de recevoir un e-mail « Mot de passe oublié » ; nous examinerons alors comment nous pouvons vous aider.
Si vous ne recevez pas l'e-mail de vérification, nous vous demandons de réessayer et de vérifier que l'e-mail ne s'est pas retrouvé dans votre dossier spam ou dans un autre dossier. Il se peut que vous deviez essayer plusieurs fois de recevoir l'e-mail, mais cela devrait fonctionner.""",


"middle.OnlineServices.WeSentActivationMail.English": """I just sent an activation link for your account to XXX. Be sure to check your spam and promotions folders if you don’t see it right away. Please follow the steps in this link by registering via Itsme and then setting a password that meets the following criteria:

- Length: between 10 and 64 characters 
- Uppercase letters: at least one (A-Z) 
- Lowercase letters: at least one (a-z) 
- Numbers: at least one (0-9) 
- Special characters: at least one (e.g., !, @, #, $…)

Once the account is activated, you can go to the MyDigi login page to log in. You may receive the message “Authentication failed - Invalid credentials” on your first login attempt; in that case, you must go through the “Forgot your password?” procedure to access your account. 
To do this, an email will be sent to the same email address you just used to create your account. If you can’t find this email right away, be sure to check your spam and promotions folders.""",

"middle.OnlineServices.WeSentActivationMail.Dutch": """Ik stuurde zonet een activatielink voor je account naar XXX. Kijk zeker ook in je spam en of promoties folder als je deze niet meteen terugvindt. Gelieve de stappen te volgen in deze link door je te registeren via Itsme en daarna een wachtwoord in te stellen dat voldoet aan onderstaande criteria:

- Lengte: tussen 10 en 64 tekens 
- Hoofdletters: minstens één (A-Z) 
- Kleine letters: minstens één (a-z) 
- Cijfers: minstens één (0-9) 
- Speciale tekens: minstens één (bijv. !, @, #, $…)

Zodra het account is geactiveerd kunt u naar de MyDigi loginpagina gaan om je in te loggen. Het is mogelijk dat je bij je eerste login poging de melding "Authentication failed - Invalid credentials" krijgt; in dat geval moet je de "Wachtwoord vergeten?" procedure doorlopen om toegang te krijgen tot je account. 
Hiervoor krijg je een mail toegestuurd naar hetzelfde mail adres waarmee je net je account hebt aangemaakt. Vind je deze mail niet meteen terug, kijk dan zeker in je spam en promoties folder.""",

"middle.OnlineServices.WeSentActivationMail.French": """Je viens d'envoyer un lien d'activation pour votre compte à XXX. N'oubliez pas de vérifier vos dossiers de courrier indésirable et de promotions si vous ne le trouvez pas immédiatement. Veuillez suivre les étapes indiquées dans ce lien en vous inscrivant via Itsme, puis en définissant un mot de passe qui répond aux critères suivants :

- Longueur : entre 10 et 64 caractères 
- Majuscules : au moins une (A-Z) 
- Minuscules : au moins une (a-z) 
- Chiffres : au moins un (0-9) 
- Caractères spéciaux : au moins un (par ex. !, @, #, $…)

Une fois le compte activé, vous pouvez vous rendre sur la page de connexion MyDigi pour vous connecter. Il est possible que lors de votre première tentative de connexion, le message « Authentication failed - Invalid credentials » s'affiche ; dans ce cas, vous devez suivre la procédure « Mot de passe oublié ? » pour accéder à votre compte. 
À cette fin, un e-mail vous sera envoyé à l'adresse e-mail que vous venez d'utiliser pour créer votre compte. Si vous ne trouvez pas cet e-mail immédiatement, pensez à vérifier vos dossiers de courrier indésirable et de promotions.""",


"middle.OnlineServices.ResetPassword.English": """I see in our system that you already have an active account associated with the email address XXX. To successfully log in to this account, go to the MyDigi website and enter your email address and password.

You may receive the message “Authentication failed - Invalid credentials” on your first attempt to log in.  
If that happens, you’ll need to go through the “Forgot your password?” process to access your account.

When you do that, you’ll receive an email at the same email address you used to create your account.  
If you don’t see this email right away, be sure to check your spam and promotions folders.

Once you’ve found the email, you’ll need to choose a new password that meets the following criteria:

- Length: between 10 and 64 characters
- Uppercase letters: at least one (A-Z)
- Lowercase letters: at least one (a-z)
- Numbers: at least one (0-9)
- Special characters: at least one (e.g., !, @, #, $…)

Once you’ve done this, you should be able to log in with your email address and the new password you chose.""",

"middle.OnlineServices.ResetPassword.Dutch": """Ik zie in ons systeem dat je al een actief account hebt op het mail adres XXX. Om succesvol in te loggen op dit account, ga je naar de MyDigi-website en voer je je e-mailadres en wachtwoord in.

Het is mogelijk dat je bij je eerste poging om in te loggen de melding "Authentication failed - Invalid credentials" krijgt.  
Als dat gebeurt, moet je de "Wachtwoord vergeten?"-procedure doorlopen om toegang te krijgen tot je account.

Wanneer je dat doet, ontvang je een e-mail op hetzelfde e-mailadres dat je gebruikte om je account aan te maken.  
Als je deze e-mail niet meteen ziet, controleer dan zeker ook je spam- en promotiefolders.

Zodra je de e-mail gevonden hebt, moet je een nieuw wachtwoord kiezen dat voldoet aan de volgende criteria:

- Lengte: tussen 10 en 64 tekens
- Hoofdletters: minstens één (A-Z)
- Kleine letters: minstens één (a-z)
- Cijfers: minstens één (0-9)
- Speciale tekens: minstens één (bijv. !, @, #, $…)

Nadat je dit gedaan hebt, zou je moeten kunnen inloggen met je e-mailadres en het nieuw gekozen wachtwoord.""",

"middle.OnlineServices.ResetPassword.French": """Je constate dans notre système que vous disposez déjà d'un compte actif associé à l'adresse e-mail XXX. Pour vous connecter à ce compte, rendez-vous sur le site Web MyDigi et saisissez votre adresse e-mail et votre mot de passe.

Il est possible que, lors de votre première tentative de connexion, le message « Authentication failed - Invalid credentials » s'affiche.  
Si c'est le cas, vous devez suivre la procédure « Mot de passe oublié ? » pour accéder à votre compte.

Une fois cette procédure effectuée, vous recevrez un e-mail à l'adresse que vous avez utilisée pour créer votre compte.  
Si vous ne voyez pas cet e-mail immédiatement, pensez à vérifier vos dossiers de courrier indésirable et de promotions.

Une fois que vous avez trouvé l'e-mail, vous devez choisir un nouveau mot de passe qui répond aux critères suivants :

- Longueur : entre 10 et 64 caractères
- Majuscules : au moins une (A-Z)
- Lettres minuscules : au moins une (a-z)
- Chiffres : au moins un (0-9)
- Caractères spéciaux : au moins un (par ex. !, @, #, $…)

Une fois ces étapes effectuées, vous devriez pouvoir vous connecter à l'aide de votre adresse e-mail et du nouveau mot de passe choisi.""",


"middle.OnlineServices.WeSentChangeMailRequest.English": """We have just sent an email to XXX containing a request to change your email address.  
Please follow the steps in this email to change your email address. We would also like to ask you to log in to your MyDigi account immediately after this to check if the change has been successfully made.""",

"middle.OnlineServices.WeSentChangeMailRequest.Dutch": """We stuurden zonet een mail naar XXX met daarin een verzoek om je mail adres te veranderen.
Gelieve de stappen in deze mail te volgen om de verandering door te voeren. Ook zouden we je willen vragen meteen daarna in te loggen op je MyDigi account om te controleren of de verandering goed gelukt is.""",

"middle.OnlineServices.WeSentChangeMailRequest.French": """Nous venons d'envoyer un e-mail à XXX contenant une demande pour changer votre adresse e-mail.  
Veuillez suivre les étapes dans cet e-mail pour modifier votre adresse e-mail. Nous vous demandons également de vous connecter immédiatement à votre compte MyDigi après cela pour vérifier que le changement a été effectué correctement.""",

# ─────────────────────────────
# OUTRO
# ─────────────────────────────

"outro.General.English": """If you don't notice any improvements, feel free to contact us again! We’ll be happy to help you further.


Kind regards,  
Arthur  
Technical Support  
DIGI BE""",

"outro.General.Dutch": """Als u geen verbeteringen merkt, neem dan gerust opnieuw contact met ons op! Wij helpen u graag verder.


Met vriendelijke groeten,  
Arthur
Technical Support  
DIGI BE""",

"outro.General.French": """Si vous ne constatez aucune amélioration, n'hésitez pas à nous recontacter ! Nous serons ravis de vous aider davantage.


Cordialement,  
Arthur  
Support Technique  
DIGI BE """,


# ─────────────────────────────
# NOTIFICATION MAIL
# ─────────────────────────────

"notification.English": """Dear client, 

We sent an email to XXX regarding the issue you reported to our DIGI helpdesk.
If you can't find this email right away, please be sure to check your spam and promotions folders.
If your problem has been resolved in the meantime, please don’t hesitate to let us know.

Kind regards
DIGI BE""",

"notification.Dutch": """Beste klant, 

We stuurden een e-mail naar XXX omtrent het probleem dat je hebt gemeld aan onze DIGI helpdesk.
Vind je deze mail niet meteen terug, kijk dan zeker in je spam en promoties folder.
Is je probleem ondertussen opgelost, dan mag je ons dat ook zeker weten laten.

Met vriendelijke groeten
DIGI BE""",

"notification.French": """Cher client,

Nous avons envoyé un email à XXX concernant le problème que vous avez signalé à notre service d'assistance DIGI.
Si vous ne trouvez pas cet email immédiatement, veuillez vérifier vos dossiers de spam et de promotions. Si votre problème est entre-temps résolu, n’hésitez pas à nous en informer. 


Cordialement
DIGI BE"""
}
# Définition des fonctions

def resultats():
    global resultat_transmis
    if resultat_transmis == False:
        print("\n====== R E S U L T A T S ======\n")
        for prenom in ressemblant:
            match prenom:
                case 'Kagami':
                    print("Le personnage de l'univers auquel tu ressembles le plus est  K A G A M I  (alias : Ryuko)")
                    print("Son miraculous est celui du dragon Long.\n")
                    print("Kagami est une escrimeuse hors pair, qui excelle dans tout ce qu'elle entreprend (bien qu'elle ait plus de difficultés à interagir socialement).")
                    print("Tu partages la détermination et la rigueur de Kagami. Comme elle, tu donnes toujours le meilleur de toi-même.")
                    print("Tes proches peuvent compter sur ta loyauté sans faille !")
                case 'Marinette':
                    print("Le personnage de l'univers auquel tu ressembles le plus est  M A R I N E T T E  (alias : Ladybug)")
                    print("Son miraculous est celui de la coccinelle et son kwami est Tikki.\n")
                    print("Marinette est la déléguée de classe mais aussi la gardienne des miraculous, de lourdes reponsabilités pésent sur elle.")
                    print("Comme Marinette tu es une personne responsable, créative et connectée à ses émotions.")
                    print("Même si tu peux parfois paniquer, ton ingéniosité et ta capacité à rebondir font de toi une héroïne hors pair !")
                case 'Chloe':
                    print("Le personnage de l'univers auquel tu ressembles le plus est  C H L O E  (alias : Queen Bee)")
                    print("Son miraculous est celui de l'abeille et son kwami est Pollen.\n")
                    print("Chloé est un personnage complexe, qui même si elle ne fait pas toujours les bons choix, peut être capable du meilleur à condition que quelqu'un croie en elle.")
                    print("Comme Chloé, tu sais ce que tu veux et tu n'as pas peur de le montrer. L'amour et la reconnaissance sont des choses importantes pour toi.")
                case 'Alix':
                    print("Le personnage de l'univers auquel tu ressembles le plus est  A L I X  (alias : Bunnyx)")
                    print("Son miraculous est celui du lapin et son kwami est Fluff.\n")
                    print("Alix est un personnage clé de l'univers, le pouvoir de voyager dans le temps implique de grandes responsabilités et une forte maîtrise.")
                    print("Comme Alix tu es une personne indépendante et réfléchie. Tu sais prendre du recul face aux situations les plus délicates. Malgrés tout tu restes une personne qui aime le fun et le sport, avec toi on ne s'ennuie jamais !")
                case 'Juleka':
                    print("Le personnage de l'univers auquel tu ressembles le plus est  J U L E K A  (alias : Tigresse Pourpre)")
                    print("Son miraculous est celui du tigre et son kwami est Roarr.\n")
                    print("Juleka est une personne trés timide, elle a developpé d'autres manières de s'exprimer, c'est une personne trés créative au look incroyablement stylé.")
                    print("Tu partages la douceur mystérieuse de Juleka, tu as une présence apaisante. Tes proches savent qu'ils peuvent compter sur ton écoute et ta loyauté.")
                case 'Rose':
                    print("Le personnage de l'univers auquel tu ressembles le plus est  R O S E  (alias : Pigella)")
                    print("Son miraculous est celui du cochon et son kwami est Daizzi.\n")
                    print("Tu es aussi rayonnante et optimiste que Rose. Comme elle, tu vois le beau même dans les moments difficiles, ton enthousiasme est contagieux. Ton cœur plein de douceur et ton attention envers les autres font de toi une amie irremplaçable.")
                    print("Le monde a besoin de ta lumière !")
                case 'Nino':
                    print("Le personnage de l'univers auquel tu ressembles le plus est  N I N O  (alias : Carapace)")
                    print("Son miraculous est celui de la tortue et son kwami est Wayzz.\n")
                    print("Nino c'est le meilleur pot que l'on puisse souhaiter : cool et détendu il sait mettre l'ambiance, et il n'hésitera pas une seconde à prendre la parole pour défendre ses proches.")
                    print("Comme Nino tu es à l'aise avec les autres, tu prends la vie du bon côté et fais tout pour qu'elle reste la meilleure possible !")
                case 'Luka':
                    print("Le personnage de l'univers auquel tu ressembles le plus est  L U K A  (alias : Viperion)")
                    print("Son miraculous est celui du serpent et son kwami est Sass.\n")
                    print("Luka est une personne de confiance, qui sait garder un secret. Il aide souvent ses amis à se connecter à leur 'musique intérieure', à mieux se comprendre eux-mêmes.")
                    print("Comme Luka, tu es calme, intuitif et profondément bienveillant. Tu écoutes plus que tu ne parles, mais quand tu le fais, tes mots résonnent juste.")
                    print("Ta présence est un refuge pour tes proches !")
                case 'Max':
                    print("Le personnage de l'univers auquel tu ressembles le plus est  M A X  (alias : Pégase)")
                    print("Son miraculous est celui du cheval et son kwami est Kaalki.\n")
                    print("Max c'est le geek du groupe. La technologie n'a aucun secret pour lui !")
                    print("Ton intelligence et ta soif de connaissance rappellent celles de Max. Méthodique et inventif, tu excelles à trouver des solutions originales aux problèmes.")
                    print("Ton approche stratégique et ton calme font de toi un coéquipier précieux !")
                case 'Sabrina':
                    print("Le personnage de l'univers auquel tu ressembles le plus est  S A B R I N A  (alias : Traquemoiselle)")
                    print("Son miraculous est celui du chien et son kwami est Barkk.\n")
                    print("Sabrina est un personnage qui se sous-estime et qui n'a pas encore conscience de sa grande valeur.")
                    print("Comme Sabrina tu es dévouée et gentille, toujours prête à aider.")
                    print("Sous tes airs discrets se cache un courage et une détermination qui surprennent !")
                case 'Kim':
                    print("Le personnage de l'univers auquel tu ressembles le plus est  K I M  (alias : Roi Singe)")
                    print("Son miraculous est celui du singe et son kwami est Xuppu.\n")
                    print("Kim c'est celui qui se ne prends pas au sérieux, il aime la vie, il aime le sport, et les soucis ? C'est secondaire.")
                    print("Tu partages l'enthousiasme et la détermination de Kim. Tu es toujours prêt à relever des défis.")
                    print("Ton énergie et ton humour sont contagieux !")
                case 'Mylene':
                    print("Le personnage de l'univers auquel tu ressembles le plus est  M Y L E N E  (alias : Polymouse)")
                    print("Son miraculous est celui de la souris et son kwami est Mullo.\n")
                    print("Mylène est un personnage qui fait preuve d'un courage immense en combattant ses peurs. Elle est aussi trés engagée, notamment pour protéger l'environnement.")
                    print("Comme Mylène, tu es une personne douce et courageuse, mais il ne faut pas trop te chercher, tu n'hésite pas à monter au créneau pour défendre tes convictions !")
                case 'Alya':
                    print("Le personnage de l'univers auquel tu ressembles le plus est  A L Y A  (alias : Rena Rouge)")
                    print("Son miraculous est celui du renard et son kwami est Trixx.\n")
                    print("Alya est un personnage solaire et est la meilleure alliée de ladybug. C'est quelqu'un de fiable, qui malgré son amour de la vérité, sait garder un secret.")
                    print("Comme Alya ton intelligence émotionelle est particuliérement développée. Fine stratége, tu sais analyser les situations, prendre du recul et user de ta ruse (en toute éthique) pour parvenir à tes fins !")
                case 'Zoe':
                    print("Le personnage de l'univers auquel tu ressembles le plus est  Z O E  (alias : Vesperia)")
                    print("Son miraculous est celui de l'abeille et son kwami est Pollen.\n")
                    print("Zoé est un personnage qui brille par sa bienveillance. Elle n'aime pas se faire remarquer mais apprends petit à petit à placer ses limites.")
                    print("Comme Zoé, tu sais faire preuve d'assertivité. Tu inspires les autres par ta force tranquille !")
                case 'Nathaniel':
                    print("Le personnage de l'univers auquel tu ressembles le plus est  N A T H A N I E L  (alias : Caprikid)")
                    print("Son miraculous est celui de la chèvre et son kwami est Ziggy.\n")
                    print("Nathaniel est un personnage timide qui s'exprime à travers les bandes dessinées qu'il créé avec son ami Marc.")
                    print("Comme Nathaniel tu as l'âme d'un artiste et une imagination débordante !")
                case 'Adrien':
                    print("Le personnage de l'univers auquel tu ressembles le plus est  A D R I E N  (alias : Chat Noir)")
                    print("Son miraculous est celui du chat et son kwami est Plagg.\n")
                    print("Adrien est une personne sincère et gentille, qui aspire à la liberté et à la simplicité. Lorsqu'il se transforme en Chat Noir il a enfin l'impression de respirer !")
                    print("Comme Adrien tu es une personne responsable et fiable. Tu apprécies de lâcher prise lorsque tu peux te le permettre ! Tes proches peuvent compter sur écoute et sur ton sens de l'humour.")
                case 'Ivan':
                    print("Le personnage de l'univers auquel tu ressembles le plus est  I V A N  (alias : Minotaurox)")
                    print("Son miraculous est celui du boeuf et son kwami est Stompp.\n")
                    print("Ivan est un personnage profondément gentil, il est doté d'une force morale et physique incroyable.")
                    print("Comme Ivan, tu combines force et douceur. Tes proches peuvent compter sur toi, tu es le pilier sur lequel ils savent pouvoir toujours s'appuyer.")
                case 'Marc':
                    print("Le personnage de l'univers auquel tu ressembles le plus est  M A R C  (alias : Coq Courage)")
                    print("Son miraculous est celui du COQ  et son kwami est Orikko.\n")
                    print("Marc est un personnage qui est entravé par sa grande timidité au quotidien, lorsqu'il se transforme en Coq Courage il apprends l'acceptation de soi et peut faire preuve de son plein potentiel.")
                    print("Comme Marc tu as l'âme d'un artiste. Bien que timide, tu sais faire preuve de courage pour défendre tes convictions.")
        resultat_transmis = True


def question(texte_question, r1, r2, r3=None, r4=None, r5=None, r6=None):
    """Pose une question à choix multiples (jusqu'à 6 possibilités de réponse). Vérifie que l'entrée utilisateur correspond à une réponse valide.
        Arguments:
    1 (str) : texte de la question
    2 à 3 (str) : complétion obligatoire de l'argument. Texte de chaque réponse
    4 à 7 (str) : complétion non obligatoire de l'argument. Texte de chaque réponse
        Return : 
    '1', '2', ..., selon la réponse choisie
    """
    # Création dynamique de la liste des réponses (gestion des réponses optionnelles)
    liste_reponses_possibles = [r1, r2]
    for rep in [r3, r4, r5, r6]:
        if rep is not None:
            liste_reponses_possibles.append(rep)
    # Construction du texte à afficher à l'utilisateur (question + réponses possibles)
    texte_complet_qr = f"{texte_question}\n"
    for rep in liste_reponses_possibles:
        texte_complet_qr += f"{rep}\n"
    # Comptage du nombre de réponses possibles pour cette question
    nombre_reponses = len(liste_reponses_possibles)
    # Affichage de la question et recueil de la réponse de l'utilisateur
    reponse_utilisateur = input(f"{texte_complet_qr} ...")
    # Check de la validité de la réponse utilisateur
    while reponse_utilisateur not in [str(i) for i in range(1, nombre_reponses + 1)]:
        reponse_utilisateur = input(f"Il y a une erreur dans la réponse transmise... Veuillez entrer un nombre entre 1 et {nombre_reponses} puis appuyez sur 'Entrée'...")
    return reponse_utilisateur.strip()


def ifresult_elsebonus(q, r1, r2, r3, r4, r5, r6):
    if len(ressemblant) != 1:
        reponse_bonus = question(q, r1, r2, r3, r4, r5, r6)
        return reponse_bonus
    else:
        resultats()


def maj_ressemblant():
    """MAJ liste des personnages contenus dans la liste [ressemblant]
    1 - Nettoyage de la liste en supprimant tout son contenu
    2 - Y ajoute chaque personnage de la liste personnage avec le score maximal"""
    ressemblant.clear()
    max_score = max(personnages.values())
    for prenom, score in personnages.items():
        if score == max_score:
            ressemblant.append(prenom)

# Variable globale initialisée à False : statut des résultats transmis vs non transmis, sur non transmis
resultat_transmis = False

# Début des questions à user

# Message introductif
input("Bonjour et bienvenue dans ce programme !\nExplorons ensembles l'univers de Miraculous Ladybug : ce test propose de découvrir à quel personnage héroïque de cet univers tu ressembles le plus :)\nUne courte série de questions sur tes goûts et ta personnalité va t'être posée. Il te suffit de répondre à chaque question par le chiffre correspondant à ta réponse (par exemple '1) puis d'appuyer sur 'Entrée'.\nIl s'agit bien entendu d'un programme à but ludique ne prétendant aucunement refléter une quelconque vérité.\nAppuie sur Entrée pour continuer...")

# Question 1 : défini le groupe de genre (masculin (m), féminin (f), neutre (n))
print("C'est parti ! Première question :")
q = "Tu te sens plutôt un héros ou une héroïne ?"
r1 = "1) Un héros"
r2 = "2) Une héroïne"
r3 = "3) Je préfère ne pas choisir"
rep_1 = question(q, r1, r2, r3)

# Question 1 : Création du dictionnaire personnage en fonction du groupe de genre (m vs f vs n). Clé : nom du personnage ; valeur : score associé. Ce score est initialisé à 0
match rep_1:
    case '1':
        personnages = {
        "Nino" : 0,
        "Luka" : 0,
        "Max" : 0,
        "Kim" : 0,
        "Nathaniel" : 0,
        "Adrien" : 0,
        "Ivan" : 0,
        "Marc" : 0,
        }
    case '2':
        personnages = {
        "Kagami" : 0,
        "Marinette" : 0,
        "Chloe" : 0,
        "Alix" : 0,
        "Juleka" : 0,
        "Rose" : 0,
        "Sabrina" : 0,
        "Mylene" : 0,
        "Alya" : 0,
        "Zoe" : 0,
        }
    case '3':
       personnages = {
        "Kagami" : 0,
        "Marinette" : 0,
        "Chloe" : 0,
        "Alix" : 0,
        "Juleka" : 0,
        "Rose" : 0,
        "Nino" : 0,
        "Luka" : 0,
        "Max" : 0,
        "Sabrina" : 0,
        "Kim" : 0,
        "Mylene" : 0,
        "Alya" : 0,
        "Zoe" : 0,
        "Nathaniel" : 0,
        "Adrien" : 0,
        "Ivan" : 0,
        "Marc" : 0,
        } 

# Question 2
print("Question 2 :")
q = "Si tu était une saison tu serais...?"
r1 = "1) l'hiver : concentration, force brute, élégance"
r2 = "2) le printemps : pétillant et créatif"
r3 = "3) l'été : solaire et énergique"
r4 = "4) l'automne : mélancolie, introspection, mystère"
rep_2 = question(q, r1, r2, r3, r4)
# Question 2 : Incrémentation de 3 pour chaque personnage correspondant à la réponse choisie
match rep_2:
    case '1':
        for perso in ["Adrien", "Ivan", "Kagami", "Max"]:
           if perso in personnages:
               personnages[perso] += 2 
    case '2':
        for perso in ["Marc", "Zoe", "Marinette", "Rose", "Mylene"]:
           if perso in personnages:
               personnages[perso] += 2        
    case '3':
        for perso in ["Alya", "Chloe", "Alix", "Nino", "Kim"]:
           if perso in personnages:
               personnages[perso] += 2
    case '4':
        for perso in ["Juleka", "Luka", "Sabrina", "Nathaniel"]:
            if perso in personnages:
                personnages[perso] += 2

# Question 3
print("Question 3 :")
q = "Si tu ne devais conserver qu'un seul accessoire de mode, quel serait-il ?"
r1 = "1) Des boucles d'oreilles ou un piercing : le porter sans y penser"
r2 = "2) Une bague, un bracelet ou un tour de cheville : classique et passe-partout"
r3 = "3) Un collier / un pendentif : personnalisable à souhait"
r4 = "4) Un bijou original (bague armure, bracelet-bague) : pour te démarquer"
r5 = "5) Une paire de lunettes ou une montre à gousset : Joindre l'utile au style"
r6 = "6) Un diadème ou un peigne : pour la queen / le king que tu penses être"
rep_3 = question(q, r1, r2, r3, r4, r5, r6)
# Question 3 : Incrémentation de 1 pour chaque personnage correspondant à la réponse choisie
match rep_3:
    case '1':
        for perso in ["Marinette", "Ivan"]:
            if perso in personnages:
                personnages[perso] += 1
    case '2':
        for perso in ["Luka", "Adrien", "Rose", "Nino"]:
            if perso in personnages:
                personnages[perso] += 1
    case '3':
        for perso in ["Kagami", "Alya", "Sabrina", "Mylene"]:
            if perso in personnages:
                personnages[perso] += 1
    case '4':
        for perso in ["Juleka", "Marc"]:
            if perso in personnages:
                personnages[perso] += 1
    case '5':
        for perso in ["Alix", "Max"]:
            if perso in personnages:
                personnages[perso] += 1
    case '6':
        for perso in ["Kim", "Nathaniel", "Zoe", "Chloe"]:
            if perso in personnages:
                personnages[perso] += 1

# Question 4
q = "Si tu devais choisir un métier ?"
r1 = "1) Un métier qui te permette d'être sur le devant de la scène (DJ, musicien.ne, comédien.ne,...)"
r2 = "2) Un métier qui te permette d'exercer toute ta créativité (écrivain.ne, mangaka, luthier.e, styliste,...)"
r3 = "3) Un métier engagé (journaliste, forces de l'ordre, travail dans une ONG, ...)"
r4 = "4) Un métier intellectuel (recherche en science ou sciences humaines, ingènieur,e, ...)"
r5 = "5) Faire du sport au niveau professionnel"
r6 = "6) Honnêtement tu n'en sais rien pour le moment, tu te cherches encore"
print("Question 4 :")
rep_4 = question(q, r1, r2, r3, r4, r5, r6)
# Question 4 : Incrémentation de 1 pour chaque personnage correspondant à la réponse choisie
match rep_4:
    case '1':
        for perso in ["Nino", "Chloe", "Juleka", "Rose"]:
            if perso in personnages:
                personnages[perso] += 2
    case '2':
        for perso in ["Luka", "Marc", "Marinette", "Nathaniel"]:
            if perso in personnages:
                personnages[perso] += 2
    case '3':
        for perso in ["Mylene", "Sabrina", "Alya"]:
            if perso in personnages:
                personnages[perso] += 2
    case '4':
        for perso in ["Max", "Alix"]:
            if perso in personnages:
                personnages[perso] += 2
    case '5':
        for perso in ["Kim"]:
            if perso in personnages:
                personnages[perso] += 2
    case '6':
        for perso in ["Zoe", "Adrien", "Kagami", "Ivan"]:
            if perso in personnages:
                personnages[perso] += 2

# Question 5
q = "En combat, tu dirais que tu apportes plutôt un avantage tactique ou physique ?"
r1 = "1) Tactique"
r2 = "2) Physique"
print("Question 5 :")
rep_5 = question(q, r1, r2)
# Question 5 : Incrémentation de 2 pour chaque personnage correspondant à la réponse choisie
match rep_5:
    case '1':
        for perso in ["Marc", "Nathaniel", "Alya", "Marinette", "Alix", "Rose", "Luka", "Sabrina", "Max", "Kim"]:
            if perso in personnages:
                personnages[perso] += 2
    case '2':
        for perso in ["Adrien", "Ivan", "Zoe", "Kagami", "Chloe", "Juleka", "Nino", "Mylene"]:
            if perso in personnages:
                personnages[perso] += 2


# Résultat et / ou Questions supplémentaires

# Création de la liste des personnages ressemblant le plus à l'user et mise à jour de cette liste par l'insertion des personnages ayant le plus haut score
ressemblant = []
maj_ressemblant()

# Print Result & Gestion des ex-aequos
print("Bravo, tu as fini de répondre aux questions principales ! Nous calculons les score et, si besoin, pour affiner nos résultats nous allons te poser une ou plusieurs questions supplémentaires...\n...\n...")
q = "Quel type d'acolyte es-tu ?"
r1 = "1) Le bouclier :  la personne qui n'hésite pas à prendre publiquement la défense de ses proches"
r2 = "2) L'oreille attentive : la personne avec qui l'on a de longues discussion qui les aide à mieux se connaître eux mêmes"
r3 = "3) L'esprit scientifique : la personne avec qui on refait le monde sur des bases scientifiques entre deux parties de jeu vidéo et une série de SF"
r4 = "4) Aux petits soins : la personne qui fait tout ce qui est dans son pouvoir pour aider ses proches"
r5 = "5) L'humoriste / le bon-public : la personne qui apprécie particulièrement l'humour"
r6 = "6) L'activiste : la personne qui ne rate pas une manif' ou une raison de protester"
rep_b1 = ifresult_elsebonus(q, r1, r2, r3, r4, r5, r6)
# Question bonus 1 : Incrémentation pour chaque personnage correspondant à la réponse choisie
match rep_b1:
    case '1':
        for perso in ["Nino"]:
            if perso in ressemblant:
                personnages[perso] += 1
        for perso in ["Juleka", "Chloe"]:
            if perso in ressemblant:
                personnages[perso] -= 1
    case '2':
        for perso in ["Luka"]:
            if perso in ressemblant:
                personnages[perso] += 2
        for perso in ["Zoe", "Juleka"]:
            if perso in ressemblant:
                personnages[perso] += 1
        for perso in ["Chloe", "Kim"]:
            if perso in ressemblant:
                personnages[perso] -= 1
    case '3':
        for perso in ["Max"]:
            if perso in ressemblant:
                personnages[perso] += 2
        for perso in ["Alix", "Marinette", "Alya"]:
            if perso in ressemblant:
                personnages[perso] += 1
    case '4':
        for perso in ["Sabrina"]:
            if perso in ressemblant:
                personnages[perso] += 2
        for perso in ["Rose", "Marinette"]:
            if perso in ressemblant:
                personnages[perso] += 1
        for perso in ["Kim"]:
            if perso in ressemblant:
                personnages[perso] -= 1
        for perso in ["Chloe"]:
            if perso in ressemblant:
                personnages[perso] -= 2
    case '5':
        for perso in ["Kim"]:
            if perso in ressemblant:
                personnages[perso] += 2
        for perso in ["Adrien"]:
            if perso in ressemblant:
                personnages[perso] += 1
        for perso in ["Max", "Kagami", "Juleka"]:
            if perso in ressemblant:
                personnages[perso] -= 1
    case '6':
        for perso in ["Mylene", "Nino"]:
            if perso in ressemblant:
                personnages[perso] += 2
        for perso in ["Alix", "Chloe", "Nathaniel", "Alya"]:
            if perso in ressemblant:
                personnages[perso] += 1
        for perso in ["Juleka", "Luka"]:
            if perso in ressemblant:
                personnages[perso] -= 1
        for perso in ["Sabrina", "Max"]:
            if perso in ressemblant:
                personnages[perso] -= 2

maj_ressemblant()

# Print Result & Gestion des ex-aequos 2
q = "Tu es plutôt quelqu'un qui...?"
r1 = "1) Garde son sang-froid en toutes circonstances"
r2 = "2) Cède facilement à la panique et/ou a du mal à réprimer ses émotions"
r3 = None
r4 = None
r5 = None
r6 = None
rep_b2 = ifresult_elsebonus(q, r1, r2, r3, r4, r5, r6)
# Question bonus 2 : Incrémentation pour chaque personnage correspondant à la réponse choisie
match rep_b2:
    case '1':
        for perso in ["Kagami", "Luka"]:
            if perso in ressemblant:
                personnages[perso] += 2
        for perso in ["Adrien", "Nathaniel", "Ivan", "Zoe", "Alya", "Alix", "Juleka", "Max"]:
            if perso in ressemblant:
                personnages[perso] += 1
    case '2':
        for perso in ["Marc", "Marinette", "Chloe", "Rose", "Nino", "Sabrina", "Mylene", "Kim"]:
            if perso in ressemblant:
                personnages[perso] += 1

maj_ressemblant()

# Print Result & Gestion des ex-aequos 3
q = "Face à l'adversité, sur laquelle de tes qualités tu peux le plus compter pour parvenir à tes fins ? "
r1 = "1) Ton audace"
r2 = "2) Ta créativité"
r3 = "3) Ta gentillesse"
r4 = "4) Ta ruse"
r5 = "5) Ta stratégie"
r6 = None
rep_b3 = ifresult_elsebonus(q, r1, r2, r3, r4, r5, r6)
# Question bonus 3 : Incrémentation pour chaque personnage correspondant à la réponse choisie
match rep_b3:
    case '1':
        for perso in ["Adrien", "Chloe"]:
            if perso in ressemblant:
                personnages[perso] += 2
        for perso in ["Kim", "Kagami", "Alix", "Nino"]:
            if perso in ressemblant:
                personnages[perso] += 1
        for perso in ["Ivan"]:
            if perso in ressemblant:
                personnages[perso] -= 1
    case '2':
        for perso in ["Marc", "Nathaniel"]:
            if perso in ressemblant:
                personnages[perso] += 1
        for perso in ["Zoe", "Sabrina", "Kim"]:
            if perso in ressemblant:
                personnages[perso] -= 1
    case '3':
        for perso in ["Ivan", "Zoe"]:
            if perso in ressemblant:
                personnages[perso] += 2
        for perso in ["Mylene", "Marinette", "Adrien"]:
            if perso in ressemblant:
                personnages[perso] += 1
        for perso in ["Chloe", "Alya"]:
            if perso in ressemblant:
                personnages[perso] -= 1
    case '4':
        for perso in ["Alya"]:
            if perso in ressemblant:
                personnages[perso] += 1
        for perso in ["Marc", "Nathaniel", "Ivan", "Kim"]:
            if perso in ressemblant:
                personnages[perso] -= 1
    case '5':
        for perso in ["Alix", "Kagami"]:
            if perso in ressemblant:
                personnages[perso] += 1
        for perso in ["Ivan", "Kim"]:
            if perso in ressemblant:
                personnages[perso] -= 1

maj_ressemblant()

# Print Result & Gestion des ex-aequos 4
q = "Tu as le choix cet aprés-midi de retrouver des collégues pour une activité loisir, à coup tu choisis..."
r1 = "1) du sport !"
r2 = "2) de la musique !"
r3 = "3) jeux vidéos sinon rien !"
r4 = None
r5 = None
r6 = None
rep_b4 = ifresult_elsebonus(q, r1, r2, r3, r4, r5, r6)
# Question bonus 4 : Incrémentation pour chaque personnage correspondant à la réponse choisie
match rep_b4:
    case '1':
        for perso in ["Kim", "Kagami"]:
            if perso in ressemblant:
                personnages[perso] += 2
        for perso in ["Alix", "Adrien"]:
            if perso in ressemblant:
                personnages[perso] += 1
        for perso in ["Marinette", "Chloe", "Juleka", "Rose", "Nino", "Sabrina", "Mylene", "Ivan"]:
            if perso in ressemblant:
                personnages[perso] -= 1
    case '2':
        for perso in ["Luka"]:
            if perso in ressemblant:
                personnages[perso] += 2
        for perso in ["Rose", "Ivan", "Juleka", "Nino", "Adrien", "Mylene", "Nino"]:
            if perso in ressemblant:
                personnages[perso] += 1
    case '3':
        for perso in ["Marinette", "Max"]:
            if perso in ressemblant:
                personnages[perso] += 2
        for perso in ["Alix", "Nino"]:
            if perso in ressemblant:
                personnages[perso] += 1
        for perso in ["Chloe", "Kim"]:
            if perso in ressemblant:
                personnages[perso] -= 1

maj_ressemblant()
if len(ressemblant) != 1:
    print("...\nNos questions n'ont pas suffi à départager parfaitement les résultats, tu ressembles à plusieurs personnages !")
    resultats()

input("\n\nAppuie sur 'Entrée' pour fermer ce programme")

# Merci d'avoir consacré du temps à ce code <3
# Esliel
import os
import sys
import re


imageFolder = 'sealimgs'
sortedDirectory = 'sorted'

def guessTitle(title):
    titleGuess = title.replace("_", " ");
    titleGuess = titleGuess.split(".", 1)[0]

    patterns = [
        r'\b(?:great|state)?\s*seal\s+of\b',
        r'\b\w*px\w*\b',
        r'\b(?:small|large|medium)\b',
        r'\b\w*inch\w*\b',
        r'\b\w*logo\w*\b',
        r'\b(?:the\s+)?united\s+states\b'
    ]

    regexes = [re.compile(pattern, re.IGNORECASE) for pattern in patterns]

    for regex in regexes:
        titleGuess = regex.sub("", titleGuess)
    titleGuess = titleGuess.strip()
    return titleGuess




if (len(sys.argv) == 1):
    print(f"No folder specified, defaulting to folder {imageFolder}")
else:
    imageFolder = sys.argv[1]
    if (os.path.isdir(imageFolder)):
        print(f"Sorting seals in folder {imageFolder}")
    else:
        print(f"ERROR! Folder ${imageFolder} does not exist.")
        quit();

sealList = []

for img in os.listdir(imageFolder):

    seal = {}
    os.system(f"kitty +kitten icat {os.path.join(imageFolder, img)}");
    print(f"Filename: {img}")
    seal["path"] = os.path.join(imageFolder, img);
    guessedTitle = guessTitle(img);
    print(f"Suggested title? {guessedTitle}");
    title = input("Enter title: ") or guessedTitle
    seal["title"] = title
    id = input("Enter ID:")
    seal["id"] = id
    print(seal)
    print("Enter tags\n(F)ederal, (S)tate, (M)ilitary, (H)istorical")
    tagletters = input("Tag keys: ")
    seal["tags"] = []
    tagDict = {'f':"Federal", 's':"State", 'm':"Military", 'h':"Historical"}
    for letter in tagletters:
        letter = letter.lower()
        tag = tagDict.get(letter)
        if (tag != None):
            seal["tags"].append(tag)
        else:
            print(f"Tag {letter} not recognized!")
    sealList.append(seal)
print(sealList)


        




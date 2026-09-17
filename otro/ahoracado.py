import random
import os

IMÁGENES_AHORCADO = [""" 
  _____                         ____                 
 / ____|                       / __ \                
| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
 \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
    """,'''
  

     +---+

     |   |

         |

         |

         |

         |

  =========''', '''

 

    +---+

    |   |

    O   |

        |

        |

        |

  =========''', '''

 

    +---+

    |   |

    O   |

    |   |

        |

        |

  =========''', '''

 

    +---+

    |   |

    O   |

   /|   |

        |

        |

  =========''', '''

 

    +---+

    |   |

    O   |

   /|\  |

        |

        |

  =========''', '''

 

    +---+

    |   |

    O   |

   /|\  |

   /    |

        |

  =========''', '''

 

    +---+

    |   |

    O   |

   /|\  |

   / \  |

        |

  =========''','''                                                   /$$          
                                                  |__/          
 /$$   /$$  /$$$$$$  /$$   /$$       /$$  /$$  /$$ /$$ /$$$$$$$ 
| $$  | $$ /$$__  $$| $$  | $$      | $$ | $$ | $$| $$| $$__  $$
| $$  | $$| $$  \ $$| $$  | $$      | $$ | $$ | $$| $$| $$  \ $$
| $$  | $$| $$  | $$| $$  | $$      | $$ | $$ | $$| $$| $$  | $$
|  $$$$$$$|  $$$$$$/|  $$$$$$/      |  $$$$$/$$$$/| $$| $$  | $$
 \____  $$ \______/  \______/        \_____/\___/ |__/|__/  |__/
 /$$  | $$                                                      
|  $$$$$$/                                                      
 \______/                                                       
                                                                ''']

lines=['',
'_',
'_ _',
'_ _ _',
'_ _ _ _',
'_ _ _ _ _',
'_ _ _ _ _ _',
'_ _ _ _ _ _ _',
'_ _ _ _ _ _ _ _',
'_ _ _ _ _ _ _ _ _',
'_ _ _ _ _ _ _ _ _ _',
'_ _ _ _ _ _ _ _ _ _ _',
'_ _ _ _ _ _ _ _ _ _ _ _',
'_ _ _ _ _ _ _ _ _ _ _ _ _',
'_ _ _ _ _ _ _ _ _ _ _ _ _ _'
]

def run():
    word =[]
    reciper=[]
    lifes=7
    container=[]
    n=0
    letras_ingresadas = set()

    with open("./archivos/data.txt", 'r', encoding='utf-8') as f:
        for line in f:
            word.append(line)
    
    word_selected = random.choice(word)
    word_selected = word_selected.replace('\n', '')
    a,b = 'áéíóúüÁÉÍÓÚÜ','aeiouuAEIOUU'
    trans = str.maketrans(a,b)
    word_selected=word_selected.translate(trans)

    # container = {'letter'+str(i[0]): i[1] for i in enumerate(word_selected)}
    auxiliar = [container.insert(i[0],i[1]) for i in enumerate(word_selected)]
    length = len(word_selected)
    reciper= ['_']*length
    auxiliare=['_']*length
    print(auxiliar)
    print(container)


    while lifes>0:





        if '_' in reciper:
            # os.system ("cls")
            print(IMÁGENES_AHORCADO[lifes])
            #print(word_selected)
            for e in reciper:
                print(e+' ', end="")
                        
            letter = input('\n' + '\n' + 'Ingresa una letra: ').lower()

            if letter in letras_ingresadas:
                print(IMÁGENES_AHORCADO[0])
                print('Perdiste, no puedes repetir letras, intenta de nuevo.')
                raise TypeError('Perdiste, no puedes repetir letras, intenta de nuevo.')
            assert letter.isalpha(), 'Solo puedes ingresar letras.'
            letras_ingresadas.add(letter)



            print(n)
            if letter in auxiliare:
                raise TypeError('perdiste, no puedes repetir letras, intenta de nuevo.')
            assert letter.isalpha(), 'Solo puedes ingresar letras.'
            auxiliare.append(letter)
            
            if letter in container:
              
                for x in range(length):
                    k=container[x]
                    if letter == k:
                        reciper[x]=letter
        
            else:
                lifes=lifes-1
            
            if lifes ==0:
                print(IMÁGENES_AHORCADO[lifes])
                print('Perdiste!!')
            
        else:
            print(reciper)
            print((IMÁGENES_AHORCADO[8]))
            print('Ganaste!!')

            break
        

    

if __name__ == '__main__':
    run()



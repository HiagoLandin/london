from murder import *
from menu import *
from victim import *
character=menu()
if (character=='c'):
    victim()
elif (character=='j'):
    murder()
else:
    print("opção inválida!")

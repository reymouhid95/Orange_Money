class OrangeMoney:
    def __init__(self):
        self.solde = 1000000  # Solde par défaut

    def afficher_menu(self):
        print("\nMenu Orange Money:")
        print("1. Solde de mon compte")
        print("2. Transfert d'argent")
        print("3. Paiement de facture")
        print("4. Achats de crédit")
        print("5. Quitter")

    def solde_compte(self):
        print(f"Votre solde est de {self.solde} FCFA")

    def transfert_argent(self):
        print("\nTransfert d'argent:")
        print("1. Saisir le montant à transférer")
        print("2. Quitter")
        choix = input("Votre choix : ")
        if choix == '1':
            montant = float(input("Entrez le montant à transférer : "))
            if montant <= self.solde:
                self.solde -= montant
                print(f"Transfert de {montant} FCFA effectué. Nouveau solde : {self.solde} FCFA")
            else:
                print("Solde insuffisant")
        elif choix == '2':
            return
        else:
            print("Choix invalide")

    def paiement_facture(self):
        print("\nPaiement de facture:")
        print("1. Liquide")
        print("2. Chèque")
        print("3. Quitter")
        choix = input("Votre choix : ")
        if choix == '1':
            montant = int(input("Entrez le montant en liquide : "))
            print(f"Paiement de {montant} FCFA en liquide effectué")
        elif choix == '2':
            montant = input("Entrez le montant du chèque : ")
            print(f"Paiement par chèque de {montant} FCFA effectué")
        elif choix == '3':
            return
        else:
            print("Choix invalide")

    def achat_credit(self):
        numero = input("Entrez le numéro de téléphone : ")
        montant = float(input("Entrez le montant du crédit : "))
        if montant <= self.solde:
            self.solde -= montant
            print(f"Achat de crédit de {montant} FCFA pour le numéro {numero} effectué")
            print(f"Nouveau solde : {self.solde} FCFA")
        else:
            print("Solde insuffisant")

    def run(self):
        while True:
            self.afficher_menu()
            choix = input("Votre choix : ")
            if choix == '1':
                self.solde_compte()
            elif choix == '2':
                self.transfert_argent()
            elif choix == '3':
                self.paiement_facture()
            elif choix == '4':
                self.achat_credit()
            elif choix == '5':
                print("Merci d'avoir utilisé Orange Money. Au revoir!")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

# Utilisation de la classe
if __name__ == "__main__":
    orange_money = OrangeMoney()
    orange_money.run()
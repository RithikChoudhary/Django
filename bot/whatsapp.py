
from first.models import medicine



def start(search):
    medic = medicine.objects.all()
    for i in medic:
        if(search == i.name):
            print("founnd")
        else:
            print("not found")

    












if __name__ == "__main__":
    search = input()
    start(search)

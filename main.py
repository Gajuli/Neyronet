import neyro as nr
import argparse


def main():
    path=parse_arguments().path
    neyron_0=nr.neyron("vesa_0.txt")
    neyron_0.arbeit(path)
    neyron_1=nr.neyron("vesa_1.txt")
    neyron_1.arbeit(path)
    neyron_2=nr.neyron("vesa_2.txt")
    neyron_2.arbeit(path)
    neyron_3=nr.neyron("vesa_3.txt")
    neyron_3.arbeit(path)
    neyron_4=nr.neyron("vesa_4.txt")
    neyron_4.arbeit(path)
    neyron_5=nr.neyron("vesa_5.txt")
    neyron_5.arbeit(path)
    neyron_6=nr.neyron("vesa_6.txt")
    neyron_6.arbeit(path)
    neyron_7=nr.neyron("vesa_7.txt")
    neyron_7.arbeit(path)
    neyron_8=nr.neyron("vesa_8.txt")
    neyron_8.arbeit(path)
    neyron_9=nr.neyron("vesa_9.txt")
    neyron_9.arbeit(path)
    
    
    n_max=0
    mas=[neyron_0.suma,neyron_1.suma,neyron_2.suma,neyron_3.suma,neyron_4.suma,neyron_5.suma,neyron_6.suma,neyron_7.suma,neyron_8.suma,neyron_9.suma]
    i=0
    while (i<10):
        if mas[i]>mas[n_max]:
            n_max=i
        i+=1
    print("Proga reshila, chto eto - "+str(n_max))
    answer=""
    
    while answer!="True" and answer!="False":
        answer=input("True or False?:")
        if answer=="perviy tost":
            print("za holokost")
    if answer=="True":
        print("YES, kojaniy ubludok")
    if answer=="False":
        print("Tvoya vzuala, chelovek")
        r_n=""
        while r_n not in ["0","1","2","3","4","5","6","7","8","9"]:
            r_n=input("what number is it?: ")

    
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    args = parser.parse_args()
    return args


        
    
if __name__ == '__main__':
    main()
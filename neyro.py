import numpy as np
class neyron:
    def __init__(self, path):
        self.ves=[]
        self.vhod=[]
        self.mashtab=[]
        self.suma=0
        self.porog=9
        self.danet=""
        self.ves_path=path
        
    def write_ves_txt(self, path):
        txt_file = open(path, "w")
        for item in self.ves:
            txt_file.write(str(item)+"\n")
        txt_file.close()
        
    def read_ves_txt(self, path):
        self.ves=[]
        temp=np.loadtxt(path)
        i=0
        while i<len(temp):
            self.ves.append(int(temp[i]))
            i+=1
            
        
    def read_bmp(self,path):
        self.vhod=[]
        image_file = open(path, "rb")
        image_file.seek(54)
        row=[]
        while True:
            pixel_hex =image_file.read(1)
            if len(pixel_hex) == 0:
                break
            pixel_ord=ord(pixel_hex)
        
            row.insert(0,pixel_ord)

    
        image_file.close()
        j=0
        
        while j<5:
        
            a=row[j*12+3]+row[j*12+4]+row[j*12+5]
            if a>0:
                a=0
            else:
                a=1
            b=row[j*12+6]+row[j*12+7]+row[j*12+8]
            if b>0:
                b=0
            else:
                b=1
            c=row[j*12+9]+row[j*12+10]+row[j*12+11]
            if c>0:
                c=0
            else:
                c=1
            self.vhod.append(c)
            self.vhod.append(b)
            self.vhod.append(a)
            j+=1
    def hz_poka(self):
        self.mashtab=[]
        self.suma=0
        porog=9
        self.danet=""
        i=0
        while i<len(self.ves):
            self.mashtab.append(self.ves[i]*self.vhod[i])
            self.suma+=self.ves[i]*self.vhod[i]
            i+=1
        if self.suma>self.porog:
            self.danet="True"
        else:
            self.danet="False"
    def obuchenie(self, path_vhod):
        self.read_bmp(path_vhod)
        self.read_ves_txt(self.ves_path)
        self.hz_poka()
        print("Proga skazala:"+self.danet)
        pravda=input()
        if pravda==self.danet:
            print("krasivo")
        if pravda!=self.danet:
            if pravda=="False":
                i=0
                while i<len(self.ves):
                    self.ves[i]-=self.vhod[i]
                    i+=1
            if pravda=="True":
                i=0
                while i<len(self.ves):
                    self.ves[i]+=self.vhod[i]
                    i+=1
        self.write_ves_txt(self.ves_path)
    def arbeit(self, path_vhod):
        self.read_bmp(path_vhod)
        self.read_ves_txt(self.ves_path)
        self.hz_poka()
         
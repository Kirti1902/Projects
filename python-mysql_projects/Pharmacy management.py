from tkinter import *
from tkinter import ttk
#from PIL import *
import mysql.connector
from tkinter import messagebox

class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharamacy Management System")
        self.root.geometry("1550x850+0+50")


        #==============AddMed variable======
        self.addmed_var=StringVar()
        self.refMed_var=StringVar()

        #==========main variables==
        self.ref_var=StringVar()
        self.capName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideEffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()

        lbltitle=Label(self.root,text=" PHARAMACY MANAGEMENT SYSTEM",bd =15,
                      relief=RIDGE, bg='white',fg="darkblue",
                      font=("times new roman",50,"bold"),padx=2,pady=4)

        lbltitle.pack(side=TOP,fill=X)
        

        #====================DataFrame================
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1270,height=300)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="MEDICINE INFORMATION",fg="red",font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=700,height=265)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="MEDICINE ADD DEPARTMENT",fg="green",font=("times new roman",12,"bold"))
        DataFrameRight.place(x=710,y=5,width=505,height=265)

        #====================ButtonFrame================
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=420,width=1270,height=65)

        #====================Main Button================
        btnAddData=Button(ButtonFrame,command=self.add_data(),text="Medicine Add",font=("arial",13,"bold"),bg="lightblue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnUpdateMed=Button(ButtonFrame,text="Update",font=("arial",13,"bold"),bg="lightblue",fg="white")
        btnUpdateMed.grid(row=0,column=1)

        btnDeleteMed=Button(ButtonFrame,text="Delete",font=("arial",13,"bold"),bg="red",fg="white")
        btnDeleteMed.grid(row=0,column=2)

        btnResetMed=Button(ButtonFrame,text="Reset",font=("arial",13,"bold"),bg="lightblue",fg="white")
        btnResetMed.grid(row=0,column=3)

        btnExitMed=Button(ButtonFrame,text="Exit",font=("arial",13,"bold"),bg="lightblue",fg="white")
        btnExitMed.grid(row=0,column=4)

        #=============Search button =============
        lblsearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblsearch.grid(row=0,column=5,sticky=W)

        search_combo=ttk.Combobox(ButtonFrame,width=12,font=("arial",14,"bold"),state="readonly")
        search_combo["values"]=("Ref","Medname","Lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        txtSearch=Entry(ButtonFrame,bd=3,relief=RIDGE,width=12,font=("arial",14,"bold"))
        txtSearch.grid(row=0,column=7)

        serachBtn=Button(ButtonFrame,text="Search",font=("arial",13,"bold"),bg="lightblue",fg="white")
        serachBtn.grid(row=0,column=8)

        showAll=Button(ButtonFrame,text="Show All",font=("arial",13,"bold"),bg="lightblue",fg="white")
        showAll.grid(row=0,column=9)

        #=======label and entry===============
        lblrefno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Refrence No:",padx=2)
        lblrefno.grid(row=0,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="kirti1234",database="pharmacy")
        my_cursor=conn.cursor()
        my_cursor.execute("select Ref from pharma")
        row=my_cursor.fetchall()
         

        ref_combo=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var,width=27,font=("arial",12,"bold"),state="readonly")
        ref_combo["values"]=row
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)

        lblcompany=Label(DataFrameLeft,textvariable=self.capName_var,font=("arial",12,"bold"),text="Company Name:",padx=2,pady=6)
        lblcompany.grid(row=1,column=0,sticky=W)
        txtCompany=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtCompany.grid(row=1,column=1)
        
        lblTypeofMedicine=Label(DataFrameLeft,textvariable=self.typeMed_var,font=("arial",12,"bold"),text="Types of Medicines:",padx=2,pady=6)
        lblTypeofMedicine.grid(row=2,column=0,sticky=W)

        comboTypeofMedicine=ttk.Combobox(DataFrameLeft,font=("arial",12,"bold"),width=27,state="readonly")
        comboTypeofMedicine["values"]=("Tabelt","Liquid","Capsules","Topical Medicines","Drops","Inhales","Injection")
        comboTypeofMedicine.current(0)
        comboTypeofMedicine.grid(row=2,column=1)

        #===============Add Medicine=================

        lblMedicineName=Label(DataFrameLeft,textvariable=self.medName_var,font=("arial",12,"bold"),text="Medicine Name:",padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="kirti1234",database="pharmacy")
        my_cursor=conn.cursor()
        my_cursor.execute("select MedName from pharma")
        med=my_cursor.fetchall()

        comboTypeofMedicine=ttk.Combobox(DataFrameLeft,font=("arial",12,"bold"),width=27,state="readonly")
        comboTypeofMedicine["values"]=med
        comboTypeofMedicine.current(0)
        comboTypeofMedicine.grid(row=3,column=1)

        lblLotN0=Label(DataFrameLeft,textvariable=self.lot_var,font=("arial",12,"bold"),text="Lot No.:",padx=2,pady=6)
        lblLotN0.grid(row=4,column=0,sticky=W)
        txtLotN0=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtLotN0.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,textvariable=self.issuedate_var,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtIssueDate.grid(row=5,column=1)

        lblExpDate=Label(DataFrameLeft,textvariable=self.expdate_var,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=2)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtExpDate.grid(row=6,column=1)

        lblUses=Label(DataFrameLeft,textvariable=self.uses_var,font=("arial",12,"bold"),text="Uses:",padx=2,pady=6)
        lblUses.grid(row=0,column=2,sticky=W)
        txtUses=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=10)
        txtUses.grid(row=0,column=3)

        lblSideEffects=Label(DataFrameLeft,textvariable=self.sideEffect_var,font=("arial",12,"bold"),text="Side Effects:",padx=2,pady=6)
        lblSideEffects.grid(row=1,column=2,sticky=W)
        txtSideEffects=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=10)
        txtSideEffects.grid(row=1,column=3)

        lblPriceWarnings=Label(DataFrameLeft,textvariable=self.price_var,font=("arial",12,"bold"),text="Price & Warning:",padx=2,pady=6)
        lblPriceWarnings.grid(row=2,column=2,sticky=W)
        txtPriceWarnings=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=10)
        txtPriceWarnings.grid(row=2,column=3)

        lblDosage=Label(DataFrameLeft,textvariable=self.dosage_var,font=("arial",12,"bold"),text="Dosage:",padx=2,pady=6)
        lblDosage.grid(row=3,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=10)
        txtDosage.grid(row=3,column=3)

        lblTabeltsPrice=Label(DataFrameLeft,textvariable=self.price_var,font=("arial",12,"bold"),text="Tabelts Price:",padx=2,pady=6)
        lblTabeltsPrice.grid(row=4,column=2,sticky=W)
        txtTabeltsPrice=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=10)
        txtTabeltsPrice.grid(row=4,column=3)

        lblProductQT=Label(DataFrameLeft,textvariable=self.product_var,font=("arial",12,"bold"),text="Product QT:",padx=2,pady=6)
        lblProductQT.grid(row=5,column=2,sticky=W)
        txtProductQT=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=10)
        txtProductQT.grid(row=5,column=3,sticky=W)


        #================DataFrameRight==================

       

        lblrefno=Label(DataFrameRight,font=("arial",12,"bold"),text="Refrence No.:",padx=2,pady=6)
        lblrefno.place(x=0,y=0)
        txtrefno=Entry(DataFrameRight,textvariable=self.refMed_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=14)
        txtrefno.place(x=135,y=5)

        lblmedName=Label(DataFrameRight,font=("arial",12,"bold"),text="Medicine Name:",padx=2,pady=6)
        lblmedName.place(x=0,y=35)
        txtmedName=Entry(DataFrameRight,textvariable=self.addmed_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=14)
        txtmedName.place(x=135,y=40)

        #==============sideframe===================
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=80,width=250,height=140)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_x.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)

        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor())

        #=============Medicine Add Button================
        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE)
        down_frame.place(x=300,y=85,width=135,height=140)

        btnAddmed=Button(down_frame,text="Add",font=("arial",13,"bold"),bg="lightblue",fg="white",width=12)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,command=self.UpdateMed(),text="Update",font=("arial",13,"bold"),bg="lightblue",fg="white",width=12)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,command=self.DeleteMed(),text="Delete",font=("arial",13,"bold"),bg="lightblue",fg="white",width=12)
        btnDeletemed.grid(row=2,column=0)

        btnClearmed=Button(down_frame,command=self.ClearMed(),text="Clear",font=("arial",13,"bold"),bg="lightblue",fg="white",width=12)
        btnClearmed.grid(row=3,column=0)

        #===============Frame Details================
        Framedetails=Frame(self.root,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=500,width=1270,height=160)

        #==========Main Table & Scrollbar========
        Table_frame=Frame(self.root,bd=15,relief=RIDGE)
        Table_frame.place(x=10,y=510,width=1250,height=140)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.pharamacy_table=ttk.Treeview(Table_frame,column=("reg","companyname","type","tabletname","lotno","issuedate","expdate","uses","sideeffect","warning","dosage","price","productqt")
                                            , xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.pharamacy_table.xview)
        scroll_y.config(command=self.pharamacy_table.yview)

        self.pharamacy_table["show"]="headings"

        self.pharamacy_table.heading("reg",text="Reference No")
        self.pharamacy_table.heading("companyname",text="Company Name")
        self.pharamacy_table.heading("type",text="Type of Medicine")
        self.pharamacy_table.heading("tabletname",text="Tablet Name")
        self.pharamacy_table.heading("lotno",text="Lot No")
        self.pharamacy_table.heading("issuedate",text="Issue Date")
        self.pharamacy_table.heading("expdate",text="Exp Date")
        self.pharamacy_table.heading("uses",text="Uses")
        self.pharamacy_table.heading("sideeffect",text="sideeffect")
        self.pharamacy_table.heading("warning",text="Warning")
        self.pharamacy_table.heading("dosage",text="Dosage")
        self.pharamacy_table.heading("price",text="Price")
        self.pharamacy_table.heading("productqt",text="Product Quantity")
        self.pharamacy_table.pack(fill=BOTH,expand=1)
        self.fetch_dataMed()
        self.fetch_data()
        self.pharamacy_table.bind("<ButtonRelease-1",self.get_cursor)

        #==============Medicine Functionality Declaration=========

    def AddMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="kirti1234",database="pharmacy")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",(
                self.refMed_var.get(),
                self.addmed_var.get()
        ))
        conn.commit()
        self.fetch_dataMed()
        self.Medget_cursor()
        conn.close()
        messagebox.showinfo("Success","Medicine Added")

    def fetch_dataMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="kirti1234",database="pharmacy")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharma")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def Medget_cursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.refMed_var.set(row[0])
        self.addmed_var.set(row[1])
    
    def UpdateMed(self):
        if self.refMed_var.get()=="" or self.addmed_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="kirti1234",database="pharmacy")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharma set MedName=%s where Ref=%s",(
                
                self.addmed_var.get(),
                self.refMed_var.get(),
            ))
            conn.commit()
            self.fetch_dataMed()
            conn.close()

            messagebox.showinfo("Success","Medicine Updated")

        
    def DeleteMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="kirti1234",database="pharmacy")
        my_cursor=conn.cursor()

        sql="delete from pharma where Ref=%s"
        val=(self.refMed_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetchall()
        conn.close()

    def ClearMed(self):
        self.refMed_var.set("")
        self.addmed_var.set("")
        
    def add_data(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="kirti1234",database="pharmacy")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.ref_var.get(),
                    self.capName_var.get(),
                    self.typeMed_var.get(),
                    self.medName_var.get(),
                    self.lot_var.get(),
                    self.issuedate_var.get(),
                    self.expdate_var.get(),
                    self.uses_var.get(),
                    self.sideEffect_var.get(),
                    self.warning_var.get(),
                    self.dosage_var.get(),
                    self.price_var.get(),
                    self.product_var.get(),
            ))
            conn.commit()
            self.fetch_dataMed()
            self.Medget_cursor()
            conn.close()
            messagebox.showinfo("Success","Data inserted.")

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="kirti1234",database="pharmacy")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]

        self.ref_var.set(row[0]),
        self.capName_var.set(row[1]),
        self.typeMed_var.set(row[2]),
        self.medName_var.set(row[3]),
        self.lot_var.set(row[4]),
        self.issuedate_var.set(row[5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideEffect_var.set(row[8]),
        self.warning_var.set(row[9]),
        self.dosage_var.set(row[10]),
        self.price_var.set(row[11]),
        self.product_var.set(row[12])

    def Update(self):
        if self.refMed_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="kirti1234",database="pharmacy")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharmacy set ref_var=%s,capName_var=%s,typeMed_var=%s,medName_var=%s,lot_var=%s,issuedate_var=%s,expdate_var=%s,uses_var=%s,sideEffect_var=%s,warning_var=%s,dosage_var=%s,price_var=%s,product_var=%s where refno=%s",(
                
                self.ref_var.get(),
                self.capName_var.get(),
                self.typeMed_var.get(),
                self.medName_var.get(),
                self.lot_var.get(),
                self.issuedate_var.get(),
                self.expdate_var.get(),
                self.uses_var.get(),
                self.sideEffect_var.get(),
                self.warning_var.get(),
                self.dosage_var.get(),
                self.price_var.get(),
                self.product_var.get(),
            ))
            conn.commit()
            self.fetch_dataMed()
            conn.close()

            messagebox.showinfo("Success","Medicine Updated")

    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="kirti1234",database="pharmacy")
        my_cursor=conn.cursor()

        sql="delete from pharmacy where refno=%s"
        val=(self.ref_var.get(),)

        sql="delete from pharmacy where refno=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success","Medicine deleted.")

    def reset(self):
        
        self.ref_var.set(""),
        self.capName_var.set(""),
        self.typeMed_var.set(""),
        self.medName_var.set(""),
        self.lot_var.set(""),
        self.issuedate_var.set(""),
        self.expdate_var.set(""),
        self.uses_var.set(""),
        self.sideEffect_var.set(""),
        self.warning_var.set(""),
        self.dosage_var.set(""),
        self.price_var.set(""),
        self.product_var.set(""),



            
    

    

        


if __name__ == "__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()

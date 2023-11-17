import os

print("ป้อนตัวเลขเพื่อเริ่มต้นการทำงาน \n1. สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล \n2. เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์ \n3. เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล \n4. เลือกวิชาและลบไฟล์ \n0. จบการทํางาน")

try :
    select1 = input("โปรดเลือกคำสั่งที่คุณต้องการใช้งาน: ")
    if select1 not in ["0","1","2","3","4"] :
        print("*******โปรดป้อนแค่ 1,2,3,4,0 เท่านั้น*********")
        
    if select1 == "1" :
        fileName = input("ป้อนชื่อไฟล์วิชาเพื่อเก็บข้อมูลคะแนน (.txt):")

        if ".txt" not in fileName == "1":
            print(" นามสกุลไฟล์ไม่ถูกต้องโปรดป้อนใหม่ ")
            
        else :
            stuName = input("กรุณาป้อนชื้อ - นามสกุล: ")
            midScore = int(input("กรุณาป้อนคะแนนกลางภาค: "))
            finalScore = int(input("กรุณาป้อนคะแนนปลายภาค: "))
            accuScore = int(input("กรุณาป้อนคะแนนก็บ: "))
            totalScore = midScore + finalScore + accuScore

            if totalScore >= 50 :
                result = "ผ่าน"
                subjectDetail = open(f"{fileName}.txt", "w", encoding="utf-8")
                subjectDetail.write(f"\nนักศึกษา {stuName} \nคะแนนกลางภาค: {midScore} \nคะแนนปลายภาค: {finalScore} \nคะแนนเก็บ: {accuScore} \nคะแนนรวม: {totalScore} \nผลลัพธ์ :{result} \n \n")
                print("\n************************************************\nสร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว\n************************************************")

            else :
                result = "ไม่ผ่าน"
                subjectDetail = open(f"{fileName}.txt", "w", encoding="utf-8")
                subjectDetail.write(f"\nนักศึกษา {stuName} \nคะแนนกลางภาค: {midScore} \nคะแนนปลายภาค: {finalScore} \nคะแนนเก็บ: {accuScore} \nคะแนนรวม: {totalScore} \nผลลัพธ์ :{result} \n \n")
                print("\n************************************************\nสร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว\n************************************************")
    
    if select1 == "2" :

        subjectFile = os.listdir()
        if not subjectFile :
            print(" ไม่มีไฟล์ใด ๆ อยู่เลย ")
            exit    

        else :
            for i in subjectFile :
                if i.endswith(".txt"):
                    print(i)
            fileSelect = input("โปรดพิมพ์ชื่อไฟล์ที่คุณต้องการต่อท้าย (พิมพ์นามสกุลไฟล์เป็น .txt เท่านั้น): ")

            if fileSelect not in subjectFile :
                print(" คุณพิมพ์ชื่อไฟล์ผิด ")

            if not fileSelect.endswith(".txt"):
                print("ต้องเป็นไฟล์ .txt เท่านั้น")

            elif fileSelect in subjectFile :
                subjectMod = open(f"{fileSelect}", "a+", encoding="utf-8")
                stuName = input("กรุณาป้อนชื้อ - นามสกุล: ")
                midScore = int(input("กรุณาป้อนคะแนนกลางภาค: "))
                finalScore = int(input("กรุณาป้อนคะแนนปลายภาค: "))
                accuScore = int(input("กรุณาป้อนคะแนนก็บ: "))
                totalScore = midScore + finalScore + accuScore

                if totalScore >= 50 :
                    result = "ผ่าน"
                    if fileSelect.endswith(".txt"):
                        subjectMod.write(f"\nนักศึกษา {stuName} \nคะแนนกลางภาค: {midScore} \nคะแนนปลายภาค: {finalScore} \nคะแนนเก็บ: {accuScore} \nคะแนนรวม: {totalScore} \nผลลัพธ์ :{result} \n \n")
                        print("\n******************************\nเพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว\n******************************")
                        subjectMod.close()

                else : 
                    result = "ไม่ผ่าน"
                    if fileSelect.endswith(".txt"):
                        subjectMod.write(f"\nนักศึกษา {stuName} \nคะแนนกลางภาค: {midScore} \nคะแนนปลายภาค: {finalScore} \nคะแนนเก็บ: {accuScore} \nคะแนนรวม: {totalScore} \nผลลัพธ์ :{result} \n \n")
                        print("\n******************************\nเพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว\n******************************")
                        subjectMod.close

    if select1 == "3" :
        subjectFile = os.listdir()
        if not subjectFile :
            print(" ไม่มีไฟล์ใด ๆ อยู่เลย ")
            exit

        else :
            for i in subjectFile :
                if i.endswith(".txt"):
                    print(i)
            fileSelect = input("โปรดพิมพ์ชื่อไฟล์ที่คุณต้องการอ่าน (พิมพ์นามสกุลไฟล์เป็น .txt เท่านั้น): ")

            if fileSelect not in subjectFile :
                print(" คุณพิมพ์ชื่อไฟล์ผิด ")

            if not fileSelect.endswith(".txt"):
                print("ต้องเป็นไฟล์ .txt เท่านั้น")

            elif fileSelect in subjectFile :
                subjectRead = open(f"{fileSelect}", "r", encoding="utf-8")
                sRead = subjectRead.read()
                print(sRead)

    if select1 == "4" :
        subjectFile = os.listdir()       
        if not subjectFile :
            print(" ไม่มีไฟล์ใด ๆ อยู่เลย ")
            exit

        else :
            for i in subjectFile :
                if i.endswith(".txt"):
                    print(i)
            fileSelect = input(" โปรดพิมพ์ชื่อไฟล์ที่คุณต้องการลบ (พิมพ์นามสกุลไฟล์เป็น .txt เท่านั้น): ")

            if fileSelect not in subjectFile :
                print(" คุณพิมพ์ชื่อไฟล์ผิด ")

            if not fileSelect.endswith(".txt"):
                print("ต้องเป็นไฟล์ .txt เท่านั้น")

            elif fileSelect in subjectFile :
                os.remove(f"{fileSelect}")
                print(" ลบไฟล์เรียบร้อย ")

    if select1 == "0" :
        print("จบการทำงานเรียบร้อยแล้ว")
        exit



except Exception :  
    print("/n***********เกิดข้อผิดพลาด/n***************")





import os
print("ป้อนตัวเลขเพื่อเริ่มต้นการทำงาน \n1. สร้างไฟล์วิชาใหม่เพื่อเพิ่มข้อมูล \n2. เลือกวิชาและเพิ่มข้อมูลต่อท้ายไฟล์ \n3. เลือกวิชาและอ่านข้อมูลจากไฟล์มาแสดงผล \n4. เลือกวิชาและลบไฟล์ \n0. จบการทํางาน")
try :
    choice = input("เลือกคำสั่งที่คุณต้องการใช้งาน: ")
    if choice not in ["0","1","2","3","4"] :
        print("กรุณาเลือกเมนู 1, 2, 3, 4 หรือ 0 เท่านั้น")

    if choice == "1" :
        s_name = input("ป้อนชื่อไฟล์วิชาเพื่อเก็บข้อมูลคะแนน (.txt): ")

        if ".txt" not in s_name :
            print("สกุลไฟล์ไม่ถูกต้อง กรุณาป้อนใหม่")

        else :
            stu_name = input("กรุณาป้อนชื้อ - นามสกุล: ")
            mid_score = int(input("กรุณาป้อนคะแนนกลางภาค: "))
            final_score = int(input("กรุณาป้อนคะแนนปลายภาค: "))
            keep_score = int(input("กรุณาป้อนคะแนนก็บ: "))
            total_score = mid_score + final_score + keep_score

            if total_score >= 50 :
                result = "ผ่าน"
                s_detail = open(f"{s_name}", "w", encoding="utf-8")
                s_detail.write(f"\nนักศึกษา {stu_name} \nคะแนนกลางภาค: {mid_score} \nคะแนนปลายภาค: {final_score} \nคะแนนเก็บ: {keep_score} \nคะแนนรวม: {total_score} \nผลลัพธ์ :{result} \n \n")
                print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว")
                s_detail.close()

            else :
                result = "ไม่ผ่าน"
                s_detail = open(f"{s_name}", "w", encoding="utf-8")
                s_detail.write(f"\nนักศึกษา {stu_name} \nคะแนนกลางภาค: {mid_score} \nคะแนนปลายภาค: {final_score} \nคะแนนเก็บ: {keep_score} \nคะแนนรวม: {total_score} \nผลลัพธ์ :{result} \n \n")
                print("สร้างไฟล์ใหม่และเพิ่มข้อมูลลงไฟล์เรียบร้อยแล้ว")
                s_detail.close()

    if choice == "2" :
        s_file_name = os.listdir()
        if not s_file_name :
            print("ไม่มีไฟล์ใดๆ อยู่เลย")
            exit

        else :
            for i in s_file_name :
                if i.endswith(".txt") :
                    print(i)
            file_choice = input("คุณต้องการเพิ่มข้อมูลต่อท้ายไฟล์อะไร: ")

            if file_choice not in s_file_name :
                print("คุณพิมพ์ชื่อไฟล์ผิด")

            if not file_choice.endswith(".txt") :
                print("ต้องเป็นไฟล์ .txt เท่านั้น")

            elif file_choice in s_file_name :
                s_mod = open(f"{file_choice}", "a+", encoding="utf-8")
                stu_name = input("ป้อนชื้อ - นามสกุล: ")
                mid_score = int(input("กรุณาป้อนคะแนนกลางภาค: "))
                final_score = int(input("กรุณาป้อนคะแนนปลายภาค: "))
                keep_score = int(input("กรุณาป้อนคะแนนก็บ: "))
                total_score = mid_score + final_score + keep_score

                if total_score >= 50 :
                    result = "ผ่าน"
                    if file_choice.endswith(".txt") :
                        s_mod.write(f"\nนักศึกษา {stu_name} \nคะแนนกลางภาค: {mid_score} \nคะแนนปลายภาค: {final_score} \nคะแนนเก็บ: {keep_score} \nคะแนนรวม: {total_score} \nผลลัพธ์ :{result} \n \n")
                        print("เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว")
                        s_mod.close()

                else :
                    result = "ไม่ผ่าน"
                    if file_choice.endswith(".txt") :
                        s_mod.write(f"\nนักศึกษา {stu_name} \nคะแนนกลางภาค: {mid_score} \nคะแนนปลายภาค: {final_score} \nคะแนนเก็บ: {keep_score} \nคะแนนรวม: {total_score} \nผลลัพธ์ :{result} \n \n")
                        print("เพิ่มข้อมูลต่อท้ายไฟล์เรียบร้อยแล้ว")
                        s_mod.close()

    if choice == "3" :
        s_file_name = os.listdir()
        if not s_file_name :
            print("ไม่มีไฟล์ใดๆ อยู่เลย")
            exit

        else :
            for i in s_file_name :
                if i.endswith(".txt") :
                    print(i)
            file_choice = input("คุณต้องการอ่านไฟล์อะไร: ")

            if file_choice not in s_file_name :
                print("คุณพิมพ์ชื่อไฟล์ผิด")

            if not file_choice.endswith(".txt") :
                print("ต้องเป็นไฟล์ .txt เท่านั้น")

            elif file_choice in s_file_name :
                s_read = open(f"{file_choice}", "r", encoding="utf-8")
                sRead = s_read.read()
                print(sRead)

    if choice == "4" :
        s_file_name = os.listdir()
        if not s_file_name :
            print("ไม่มีไฟล์ใด ๆ อยู่เลย")
            exit

        else :
            for i in s_file_name :
                if i.endswith(".txt") :
                    print(i)
            file_choice = input("คุณต้องการลบไฟล์อะไร: ")

            if file_choice not in s_file_name :
                print("คุณพิมพ์ชื่อไฟล์ผิด")

            if not file_choice.endswith(".txt") :
                print("ต้องเป็นไฟล์ .txt เท่านั้น")

            elif file_choice in s_file_name :
                os.remove(f"{file_choice}")
                print("ลบไฟล์เรียบร้อย")

    if choice == "0" :
        print("จบการทำงานเรียบร้อยแล้ว")
        exit

except Exception :
    print("กรุณาตรวจสอบข้อมูลที่ป้อนให้ถูกต้อง")

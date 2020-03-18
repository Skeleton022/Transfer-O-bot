import os, sys, datetime, shutil

def genall(directory):
        num_chars = 1024 * 1024#1M
        with open(directory + "1M_file", 'wb') as f:
            f.write(b'0' * num_chars)

        num_chars = 1024 * 1024 * 10#10M
        with open(directory + "10M_file", 'wb') as f:
            f.write(b'0' * num_chars)
 
        num_chars = 1024 * 1024 * 100#100M
        with open(directory + "100M_file", 'wb') as f:
            f.write(b'0' * num_chars)

        num_chars = 1024 * 1024 * 500#500M
        with open(directory + "500M_file", 'wb') as f:
            f.write(b'0' * num_chars)

        num_chars = 1024 * 1024 * 1024#1G
        with open(directory + "1G_file", 'wb') as f:
            f.write(b'0' * num_chars)


def copy_test(from_directory, to_directory, repeat):
    files = ["1M_file", "10M_file", "100M_file", "500M_file", "1G_file"]
    file = open(str(from_directory) + "write.log","w+")
    file.close()
    for f in files:
        sum_times = 0
        average = 0
        try:
            file = open(str(from_directory) + "write.log","a+")
            file.write(str(f) + " 100 mérés eredménye, " + str(from_directory) + " -> " + str(to_directory) + "\n")
            for x in range(1, repeat + 1):
                start = datetime.datetime.now()
                shutil.copy(from_directory + str(f), to_directory + str(f) + str(x))
                end = datetime.datetime.now()
                file.write(str(x) + ". mérés: " + str(end-start) + "\n")
                delta = str(end-start)
                delta = delta.split(':')
                sum_times = sum_times + float(delta[2])
                if x == repeat:
                    average = sum_times / x
                    file.write("A mérések összes ideje: " + str(sum_times) + "\n")
                    file.write("A mérések átlaga: " + str(average) + "\n\n")
            print("Done! - " + str(f))
        finally:
            file.close()


def main():
    print("Üdvözöllek a MAM 3. méréssorozatának 1. mérésén!")
    print("")
    os_in = input("Milyen OS-t használsz? [W]indows/[L]inux: ")
    print("")
    print("A megadott mappákban létrehoz a script 2 extra mappát, ezekben dolgozik!")
    print("Add meg az usb betűjelét. Pl.: F:/")
    print("Ha Linux akkor egy '/' jelet illesz mögé.")
    print("Ha Windows akkor két '\\' jelet illesz mögé.")
    usb_location = input("USB Lokáció: ")
    directory = input("PC Lokáció: ")
    repeat = input("Hány ismétlést szeretnél / teszt? Csak számot adj meg: ")
    repeat = int(repeat)
    os_end = ""

    if os_in.upper() == "W" or os_in.upper() == "WINDOWS":
        os_end = "\\"

    elif os_in.upper() == "L" or os_in.upper() == "LINUX":
        os_end = "/"
    
    os.mkdir(directory + "read" + os_end)
    os.mkdir(directory + "copy" + os_end)
    os.mkdir(usb_location + "read" + os_end)
    os.mkdir(usb_location + "copy" + os_end)
    
    genall(directory + "read" + os_end)
    genall(usb_location + "read" + os_end)
    
    print("Generálás kész!")
    print("Tesztek indítása ...")
    print("Most dőlj hátra, ez sokáig fog tartani!")

    copy_test(directory + "read" + os_end, usb_location + "copy" + os_end, repeat)
    copy_test(usb_location + "read" + os_end, directory + "copy" + os_end, repeat)


if __name__ == '__main__':
    main()
def find_a(f, question):
    a = True
    ans = []
    while a:
        file_line = f.readline()
        if not file_line:
            return 0
        if question == file_line:
            file_line = f.readline()
            number, t = file_line.split()
            if len(ans) == 0:
                ans.append(t)
            lst = []
            for i in range(int(number)):
                file_line = f.readline()
                lst.append(file_line)
            ans.append(lst)
    return ans





def database():
   fn = input("Insert file name\n")
   f = open(f"C:/{fn}", "a")
   while True:
       question = input("Insert question(if You want to exit, type END)\n")
       if question == "END":
           break
       f.write(f"{question}\n")
       n = int(input("Insert amount of answers\n"))
       f.write(f"{n}\n")
       for i in range(n):
           ans = input(f"Insert answer {i + 1}\n")
           f.write(f"{ans}\n")
   f.close()
def test():
    pass

n = int(input("1. Add questions to database\n2. Complete test\n3. Quit\n"))
while n != 3:
    if n == 1:
        database()
    else:
        test()
    n = int(input("1. Add questions to database\n2. Complete test\n3. Quit\n"))

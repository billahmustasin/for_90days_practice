file_obj = open('my_file.txt','w')
file_obj.write('this is newline')
#print(file_obj.readlines(1))
file_obj.close()

try:
    file_obj_new = open('my_new_file.txt','r')
except FileNotFoundError:
    print("error handled")
    file_obj_new = open('my_new_file.txt','w+')
    file_obj_new.read()
finally:
    file_obj_new.close()
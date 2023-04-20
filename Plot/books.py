def book_prep(file_in, file_out):
    from transliterate import translit
    
    file2= open(file_out, 'w', encoding='utf-8')
    file1= open(file_in, "r", encoding='utf-8')
    
    data=file1.read()
    #data = data.replace(' ','')
    data = data.split('\n')
    file1.close
    books=[]
    for line in data:
        line = translit(line, language_code='ru', reversed=False)
        temp = line.split('.,')
        temp1=temp[1]
        temp0=temp[0]
        temp[0]= temp0[:1].upper() + temp0[1:]
        temp[1]= temp1[:1].upper() + temp1[1:]
        books.append(temp)
        
    books=sorted(books, key=lambda x: x[0], reverse=False)
    
    for book in books:
            file2.write(str(book)+'\n')
        
    return books

def compare(books1, books2):
    file1= open('e:\plus.txt', "w", encoding='utf-8')
    file2= open('e:\znica.txt', "w", encoding='utf-8')
    
    for line1 in books1:
        autor = line1[0]
        book = line1[1]
        
        for line in books2:
   
            if autor != line[0]:
                break
                
            else:
                if book == line[1] :
                    file1.write(str(line1))
                    print('+ ', str(line1))
                else:
                    file2.write('- '+str(line1)+'\n')
                    file2.write('      '+str(line)+'\n')
                    
                file1.write(str(line1)+'=='+str(line)+'\n')
    file1.close()
    file2.close()
    
    return 


books1 = book_prep('e:\FatherR.txt','e:\out_father.txt')
books2 = book_prep('e:\oldR.txt', 'e:\out_old.txt')

autors =[]
books_all=[]

for line in books1:
    books_all.append(line)
    if line[0] not in autors:
        autors.append(line[0])
for line in books2:
    books_all.append(line)
    if line[0] not in autors:
        autors.append(line[0])
autors= sorted(autors, key=lambda x: x[0])        
books_all = sorted(books_all, key = lambda x: x[0]) 
file1= open('e:\plus2.txt', "w", encoding='cp1251')
for line in books_all:
    file1.write(str(line)+'\n') 
file1.close()

#for a in autors:
#    print(a, end='\n')     
     
compare(books1, books2)


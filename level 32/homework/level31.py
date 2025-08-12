#Task 1: სტრინგის ფორმატირება
#გამოიყენეთ format() ფუნქცია, რომ ჩაანაცვლოთ {name} "Alice"-ით და {place} "Wonderland"-ით. შეინახეთ შედეგი ცვლადში სახელწოდებით formatted_string და დაბეჭდეთ იგი.

name = "format, [name]"
string_format= format( name= "alice", plaace= "wonderland" )
print(string_format)


#Task 2: სტრიქონების გაერთიანება
#შექმენით სია სახელწოდებით words, რომელიც შეიცავს შემდეგ სტრიქონებს: "apple", "banana", "cherry".
#გამოიყენეთ join() ფუნქცია, რომ გაერთიანოთ ეს სიტყვები ერთ სტრიქონში, გამოყოფილი კომითა და ცარიელი ადგილით ", ". შეინახეთ #შედეგი ცვლადში სახელწოდებით fruit_string და დაბეჭდეთ იგი.


words =["apple", "banana", "cherry"]
string_fruits= " , " .join(words)
print(string_fruits)


#Task 3: სტრინგის გაყოფა
#შექმენით სტრიქონი სახელწოდებით sentence შემდეგი შინაარსით: "The quick brown fox jumps over the lazy dog."
#გამოიყენეთ split() ფუნქცია, რომ გაიყოს სტრიქონი სიტყვების სიად. შეინახეთ შედეგი ცვლადში სახელწოდებით words_list და დაბეჭდეთ იგი.

words = "the quick brown fox jumps over the lazy dog"
words_list= words.split()
print(words_list)



#Task 4: დაბლა გარდატეხვა
#შექმენით სტრიქონი სახელწოდებით mixed_case შემდეგი შინაარსით: "PyThOn Is AwEsOmE!"
#გამოიყენეთ lower() ფუნქცია, რომ მთელი სტრიქონი გარდატეხოთ პატარა ასოებში. შეინახეთ შედეგი ცვლადში სახელწოდებით lowercase_string და დაბეჭდეთ იგი.


mixed_case= "PyThOn Is AwEsOmE!"
lowercase_string= mixed_case.lower()
print(lowercase_string)



#Task 5: ზევით გარდატეხვა
#შექმენით სტრინგი 
#სახელწოდებით greeting შემდეგი უნდა გამოიტანოს: "good morning"

greeting='good morning'
uppercase_greetig= greeting.upper()
print(uppercase_greetig)
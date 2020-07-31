def Binary_search_algo():
    
    search_list = [1, 3, 5, 30, 42, 43, 500,900]
    left_list = []
    right_list = []
    if(len(search_list) % 2 == 1):
        middle_elemet = len(search_list)/2
        result = int(middle_elemet)
        final_element = search_list[result]
        for index in range(len(search_list)):
           output = search_list[index]
           if(output < final_element):
               left_list.append(output)
           elif(output >= final_element):
               right_list.append(output)
        
        print("The list has been divided into two parts :-")
        print("The first list")
        print(left_list)
        print("******************")
        print("The second list")
        print(right_list)
        print("******************")
        print("Enter a element which is searched for :-")
        user_input = int(input())
        if(user_input <= final_element):
            if(user_input in left_list):
               print("Element exists in left list")
               print(left_list)
            else:
                print("Element doesn't exist")
        else:
            if(user_input in right_list):
                print("Element exists in right list")
                print(right_list)
            else:
                print("Element doesn't exsists")
    
           
    else:
        print("The list contains Even number of Elements")
        first_middle_ele = (len(search_list)/2 -1)
        second_middle_element = (len(search_list)/2 -1)
        user_choice = int(input("Enter 1 to seach based on first middle element and Enter 2 to search based on second middle element :-"))
        if(user_choice == 1):
            print("Option 1 is selected")
            result = int(first_middle_ele)
            final_element = search_list[result]
            for index in range(len(search_list)):
                output = search_list[index]
                if(output < final_element):
                   left_list.append(output)
                elif(output >= final_element):
                   right_list.append(output)
            print("The list has been divided into two parts :-")
            print("The first list")
            print(left_list)
            print("******************")
            print("The second list")
            print(right_list)
            print("******************")
            print("Enter a element which is searched for :-")
            user_input = int(input())
            if(user_input <= final_element):
                if(user_input in left_list):
                   print("Element exists in left list")
                   print(left_list)
                else:
                   print("Element doesn't exist")
            else:
                if(user_input in right_list):
                   print("Element exists in right list")
                   print(right_list)
                else:
                   print("Element doesn't exist")
        
        else:
            print("Option  2 is selected")
            result = int(second_middle_element)
            final_element = search_list[result]
            for index in range(len(search_list)):
                output = search_list[index]
                if(output < final_element):
                   left_list.append(output)
                elif(output >= final_element):
                   right_list.append(output)
            
            print("The list has been divided into two parts :-")
            print("The first list")
            print(left_list)
            print("******************")
            print("The second list")
            print(right_list)
            print("******************")
            print("Enter a element which is searched for :-")
            user_input = int(input())
            if(user_input <= final_element):
                if(user_input in left_list):
                   print("Element exists in left list")
                   print(left_list)
                else:
                   print("Element doesn't exist")
            else:
                if(user_input in right_list):
                   print("Element exists in right list")
                   print(right_list)
                else:
                   print("Element doesn't exist")
            
    
    
    
Binary_search_algo()


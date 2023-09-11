s = "  hello world  "


        s_list = list(s)
        print(s_list)
        words = []
        output = ""
        s_list2 = list(s)

        print(len(s_list))

        x = 0

        start = 0
        last = len(s_list) - 1
        while start < last:
            for i in range(len(s_list)):
                print(i)
                print(s_list[i])
                if s_list[i] == ' ':
                    if i < last:
                        if s_list[i+1] == ' ':
                            s_list2.pop(x+1)
                            x -= 1
                x += 1
                            


            if s_list2[0] == ' ':
                s_list2.pop(0)

            if s_list2[len(s_list2) - 1] == ' ':
                s_list2.pop(len(s_list2) - 1)

            s_list2.append(' ')

            print(s_list2)

            for i in range(len(s_list2)):
                if s_list2[i] == ' ':
                    new_word = "".join(s_list2[start:i])
                    words.append(new_word)
                    start = i+1

            print(words)


            words.reverse()

            print(words)

            for i in words:
                output += i + ' '

            output = output[0:len(output)-1]

            print(output)
                        
                
                        


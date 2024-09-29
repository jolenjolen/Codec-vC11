
counter=50
ans=''
first_input=input('------------C11------------ \n1 to encrypt    2 to decrypt\n> ')
if first_input=='1':
    value=input('\nEnter your message: ')
    for i in value:
        temp1=ord(i)
        answer=temp1-counter
        if(answer<32):
            variab=32-answer
            answer=126-variab
        counter-=1
        if counter==1:
            counter=50
        temp2=chr(answer)
        ans+=temp2
    print(ans)
elif first_input == '2':
    value=input('\nEnter your message: ')
    for i in value:
        temp1=ord(i)
        answer=temp1+counter
        if(answer>126):
            variab=answer-126
            answer=32+variab
        counter-=1
        if counter==1:
            counter=50
        temp2=chr(answer)
        ans+=temp2
    print(ans)
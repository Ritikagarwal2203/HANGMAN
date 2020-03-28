
def REDO():
    import random                                               #TO USE THE RANDOM FUNTION OF LIBRARY.
    listofguess=['lagaan','highway','thor','dangal','newton']   #DECLARATION OF THE LIST OF MOVIES

        
    random.shuffle(listofguess)                                 #TO SELECT A RANDOM OF THE LIST.
    selected=list(listofguess[3])                               #TO SELECT THE 4TH ELEMENT FROM THE LIST FROM THE SHUFFLED LIST,HERE WE CAN TAKE ANY ELEMENT AS AN INPUT NO ISSUES.
    new_list=[]                                                 #HERE IS A NEW LIST TO STORE THE LETTERS OF A RANDOM DELECTED MOVIE.
    new_list.extend(selected)                                   #HERE EACH LETTERS OF THE SELECTED WORD IS CONVERTED TO THE ELEMENTS OF THE NEW_LIST.
    score=10                                                    #SO AS TO USE IT AS STARTING SCORE.
    length=len(new_list)
    length1=len(selected)
    #NOW IT'S THE TIME FOR LOOPING.
    for i in range(length):
        new_list[i]='*'
    print('  '.join(new_list))                                  #HERE THE SAME NO. OF STARS ARE DISPLAYED AS THE NO. OFCHARATERS IN THE SELECTED MOVIE.
    print("score:{}".format(score))

    for j in range(15):                                         #TO TAKE INPUT FROM USER.
        
        guess=input('guess a letter:')                          #INPUT IS TAKEN HERE.
        guess=guess.lower()                                     #SECURITY.
        print()
        if(guess==''or guess==' '):
            print('no character recieved')
            score=score-2                                       #AS PER THE GUIDANCE IT WAS TOLD TO DEDUCT MARKS FOR NO INPUT.
            print('score:{}'.format(score))
            continue                                            #IF THE ABOVE CASE OCCUR THEN IT WOULD MOCE BACK TO FOR LOOP. 

            
        if(guess in listofguess[3]):                            #IT WOULD CHECK THAT ENTERED CHARACTER IS IN SELECTED MOVIE OR NOT.
            
            print('correct guess')
            score=score+3                                       #SCORE WILL BE INCREASED.
            for k in range(length1):                            #IT WILL ITERATE THE NO. OF TIMES THE LENGTH OF THE SLECTED MOVIE TO CHECK ITS LETTER.
            
                if selected[k]==guess:                          #IF USER ENTERS A CHARACTER FOR THE FIRST TIME.
                    if new_list[k]!=guess:
                        new_list[k]=guess                       #OVERLAPPING .
                    else:                                       #HERE IF A CHARACTER IS REPEATED, MARKS IS DEDUCTED FOR THIS ALSO IF WE DON'T WANT THEN ONE STEP NEED TO CHANGE.
                        print('already received character')
                        score=score-5
                        break                                   #TAKES US OUT OF THE LOOP.
        else:                                                   #TO SPECIFY INCORRECT GUESS.
            print('incorrect guess')
            score=score-2                
                    
        
            
        print('  '.join(new_list))                              #HERE AFTER THE ENTRY THR MOVIE NAME WILL BE PRINTED.
        print("score:{}".format(score))                         #PRINT CURRENT SCORE.
        if score<=0:                                            # TO SPECIFY THAT THE SHOULD NOT GET LESS THAN 0.
            break
        elif new_list==selected:                                #IF THE WHOLE STRING OF MOVIE IS GUESSED THE GAME IS OVER.
            break
    if new_list==selected:                                      #END DECISION CHECKING IS DONE HERE.
        print('you win')
    else:
        print('you lose')                                       #END DECISION CHECKING IS DONE HERE.
    u=input('DO YOU WANT TO PLAY AGAIN  ' )                       #CHOICE OF USER TO PLAY AGAIN.
    if 'yes' in u:                                              # TO CHAECK WHETHER THE USER SAY YES OR NO.
        REDO()                                #RECURSION.
REDO()                                        #CALLING OF THE FUNCION TO BEGIN THE GAME.
        

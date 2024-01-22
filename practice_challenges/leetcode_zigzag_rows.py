


#zigzag
#leet code: place letters in row, at the end of row place next letter(s) endofrow-1 column
            # until beginning of row is reached, make full row, place backwards

[ ]   [ ]    [ ] 
 0     1      2  # start i+1 = 0, 0+1  -> 0+2, trigger: i-1     end: i = 1
       3         # start i-1: = 1 -> 1-1, trigger: i+1          end :i = 0
 4     5      6  # start i+1 = 0, 0+1 -> 0+2, trigger: i-1      end: i = 1
       7         # start i-1: = 1 -> 1-1, trigger: i+1          end: i = 0
 8     9      10 


 [ ] [ ] [ ] [ ]
  1   2   3   4  #start i = 0, +1, +2 -> +3, trigger: i-1   end: i = +2
          5      #start i = +2 ->+1,
      6          #start i = +1 ->0, trigger i+1
  7   8   9   10 #start i = 0, +1, +2 -> +3, trigger: i-1 end i = +2













#zig num
def solution(numbers):
    i = 0
    res = []
    while i == 0:
        if numbers[i] < numbers[i+1] and numbers[i+1] > numbers[i+2] or  numbers[i] > numbers[i+1] and numbers[i+1] < numbers[i+2]:
            res.append(1)
        else:
            res.append(0)
        i+=2
    while i < len(numbers)-1 and i > 0:
        if numbers[i] > numbers[i-1] and numbers[i+1] < numbers[i] or numbers[i] < numbers[i-1] and numbers[i] < numbers[i+1]:
            res.append(1)
        else:
            res.append(0)
        i+=1
    print(res)
    return res
    

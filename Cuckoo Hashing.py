
class CuckooHashing: 
    def __init__(self, size): # 
        self.M = size
        self.h = [[None, None] for x in range(size+1)]  # h-table
        self.d = [[None, None] for x in range(size+1)]  # d-table
        

    def hash(self, key):        # h-hash function, h(key)
        return key % self.M      
    
    def hash2(self, key):       # d-hash function, d(key)
        return (key*key % 17) *11 % self.M  
    
    def put(self, key, data): # item (key,data)을 넣기 위한 매소드
        #### 구현하시오. 
        key_h = self.hash(key) #키의 h 해시값
        print("i = "+str(key_h))
        if self.h[key_h][0] == None: # h테이블에 해당 값이 비어있는 경우
            self.h[key_h] = [key, data] # h 테이블에 입력
            print("h-table:[",key_h,"] [",str(key)+", '"+ data+"']")
        else: # h 테이블에 다른 값이 있는 경우
            key_d = self.hash2(key) #해당 값의 d 테이블 해시값
            if self.d[key_d][0]==key: # 해당 값이 데이터만 바뀐 경우
                self.d[key_d][1] = data #데이터만 변경해줌
                return 100
            
            h_value = self.h[key_h] # 기존 h 테이블 값
            print("[",str(h_value[0])+", '"+ \
            self.h[key_h][1]+"' ] : h[",key_h,"]  [",str(key)+", '"+ data+"'] : h[",key_h,"]")
            d_or_h = 100 # d테이블 먼저 판단
            E = [h_value[0], h_value[1]] #기존 테이블 값 불러옴
            self.h[key_h] = [key, data] #h 테이블에 입력한 데이터 삽입
            key_d2 = self.hash2(h_value[0]) # d테이블 기존 값 해시 함수
            while True: # none을 만날때까지 반복
                if self.d[key_d2][0] == None: #해당 값이 비어있는 경우
                    print("d-table:[",key_d2,"] [",str(E[0])+", '"+ E[1]+"' ]")
                    self.h[key_h] = key, data # 입력한 데이터 삽입
                    self.d[key_d2] = E
                    break #반복 종료
                
                if d_or_h == 100: # d 테이블 판단
                    renew = self.d[key_d2]
                    print("[",str(renew[0])+", '"+ \
                    renew[1]+"' ] : d[",key_d2,"]  [",str(E[0])+", '"+ E[1]+"' ] : d[",key_d2,"]")
                    
                    self.d[key_d2] = E # 기존 테이블 값 d 테이블에 저장
                    E = renew # 기존 테이블 값 갱신
                    key_h = self.hash(E[0]) # 기존 값 해시 함수
                    d_or_h = 1 # 다음 h 테이블 판단
                    h_hash = self.hash(E[0])
                    if self.h[ h_hash ][0] == None: # 해당 값이 비어있으면 
                        self.h[h_hash] = E #해당 테이블에 값 입력
                        print("h-table:[",h_hash,"] [",str(E[0])+", '"+ E[1]+"' ]")
                        break #반복 종료
                else: # h 테이블 판단
                    key_h = self.hash(E[0])
                    renew = self.h[key_h]
                    print("[",str(renew[0])+", '"+ \
                    renew[1]+"' ] : h[",key_h,"]  [",str(E[0])+", '"+ E[1]+"'] : h[",key_h,"]")
                    
                    self.h[key_h] = E # 기존 테이블 값 h 테이블에 저장
                    E = renew # 기존 테이블 값 갱신
                    key_d2 = self.hash2(E[0]) # 기존 값 해시 함수
                    d_or_h = 100 # 다음  d테이블 판단
                    d_hash = self.hash2(E[0])
                    if self.d[d_hash][0]==None:# 해당 값이 비어있으면 
                        self.d[d_hash] = E#해당 테이블에 값 입력
                        print("d-table:[",d_hash,"] [",str(E[0])+", '"+ E[1]+"' ]")
                        break#반복 종료
                
                                 
    def get(self, key): # key 값에 해당하는 value 값을 return 
        #### 구현하시오.
        for a in range(self.M):
            if self.d[a][0] == key: # data 일치하면 반환
                return self.d[a][1]
            if self.h[a][0] == key:
                return self.h[a][1]
        

    def delete(self, key): # key를 가지는 item 삭제 
        #### 구현하시오. 
        for r in range(self.M):
            if self.d[r][0] == key: # key 일치하면 none으로 갱신
                self.d[r]=[None,None]
                return 0
            if self.h[r][0] == key:
                self.h[r]=[None,None]
                return 0
                
        

    def print_table(self):
        print('********* Print Tables ************')
        print('h-table:')
        for a in range(self.M): print(a,"\t",end="")
        print('')
        for a in range(self.M): print(self.h[a][0], "\t", end="")
        print('')
        print('d-table:')
        for a in range(self.M):  print(a,"\t",end="")
        print('')
        for a in range(self.M): print(self.d[a][0], "\t", end="")
            
            
if __name__ == '__main__':
    t = CuckooHashing(13)
    t.put(25, 'grape')      # 25:  12,   0
    t.put(43, 'apple')      # 43:   4,   0
    t.put(13, 'banana')     # 13:   0,   7
    t.put(26, 'cherry')     # 26:   0,   0
    t.put(39, 'mango')      # 39:   0,  10
    t.put(71, 'lime')       # 71:   9,   8
    t.put(50, 'orange')     # 50:  11,  11
    t.put(64, 'watermelon') # 64:  12,   7
    print()
    print('--- Get data using keys:')
    print('key 50 data = ', t.get(50))
    print('key 64 data = ', t.get(64))
    print()
    t.print_table() 
    print()
    print('-----  after deleting key 50 : ---------------')
    t.delete(50)
    t.print_table() 
    print()
    print('key 64 data = ', t.get(64))
    print('-----  after adding key 91 with data berry:---------------')
    t.put(91, 'berry')
    t.print_table()
    print()
    print('-----  after changing data with key 91 from berry to kiwi:---------------')
    t.put(91, 'kiwi')       # 91:  0,   9
    print('key 91 data = ', t.get(91))    
    t.print_table()
    
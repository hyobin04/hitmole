__전체 코드의 대략적 설명__  
=====================
__'''  
        전체 게임 진행  
        튜토리얼 - 1라운드 - 점수출력, 판별 (- 2라운드 - 점수 - 3라운드 - 점수) - 랭킹출력  
        '''__  
__hitmole_board() : 게임 시작 화면 출력 -  tutorial(): 먼저 튜토리얼을 진행 - start_board() : 게임 시작과 카운트다운 출력 - play_round() : 한 라운드를 진행 - play() : 게임진행__
        
__보드판 코드 설명__  
================
# 1. HIT MOLE 글자판을 한 번 깜박이는 함수.
-------------------------------
    def hitmole_board():
    os.system("clear")  # 터미널 화면을 지우는 역할.  
    print(HIT_MOLE)  # HIT_MOLE이라는 변수에 저장된 문자열을 출력.
    time.sleep(1.5)  # 프로그램을 1.5초 동안 일시 중지. "HIT MOLE"이라는 텍스트를 화면에 표시. 
    os.system("clear") # 다시 화면을 지우고, 이전에 출력된 "HIT MOLE" 텍스트를 지우고 깨끗한 화면을 만듦.  
    print("\n"*20) # 20번의 줄 바꿈(\n)을 통해 20개의 빈 줄을 출력. 화면이 추가적으로 깨끗하게 정리.
    time.sleep(0.5) # 0.5초 동안 프로그램을 일시 중지. 빈 화면을 화면에 표시.
# 2. 튜토리얼 시작을 알리는 함수.
---------------------
    def tutorial_board():    
    os.system("clear") # 터미널 화면을 지우는 역할.
    print(TUTORIAL) # TUTORIAL이라는 변수에 문자열을 출력. "TUTORIAL"이라는 텍스트를 화면에 표시하는 역할. 
    time.sleep(1.5) # 프로그램을 1.5초 동안 일시 중지. 이로써 "TUTORIAL"이라는 텍스트가 1.5초 동안 화면에 표시.
    os.system("clear") # 다시 화면을 지움.  
    print("\n"*20)
    time.sleep(0.5) # 0.5초 동안 프로그램을 일시 중지. 빈 화면을 화면에 표시.
# 3. 게임 시작 전 카운트다운과 함께 시작을 알리는 함수.  
(3,2,1 후에 "GAME START" 텍스트를 출력.)
-------------------------------------
    def start_board():        
    os.system("clear") # 터미널 화면을 지우는 역할.  
    for i in range(3): # 3번 반복하는 루프를 시작.(이는 3, 2, 1의 카운트 다운)  
        print('\n'*8,end='') # 8번의 줄 바꿈을 통해 화면을 정리.  
        index = (3-i)*5 # 현재 카운트 값에 따라 숫자를 가져오기 위한 인덱스를 계산.  
        for l in range(5):  
            print(' '*26, NUMS[l][index:index+5]) # 26칸의 공백을 출력한 후, `NUMS` 리스트에서 해당 인덱스 범위의 숫자를 출력  
        print("\n"*8) # 숫자를 출력한 후 8번의 줄 바꿈을 통해 화면을 정리.   
        time.sleep(0.5)  
        os.system("clear") # 화면을 지움.   
        print("\n"*21) # 21번의 줄 바꿈을 통해 화면을 정리.  
        time.sleep(0.5)  
        os.system("clear")  
    print(START) # "GAME START" 텍스트를 출력.   
    time.sleep(1.0)  
# 4. 현재 랜덤으로 튀어나온 두더지를 출력하는 함수.
_____________________________________________________ 
    ''' pop = [0 0 0 0 0 0 0 0 0]  
    랜덤으로 두더지가 들어갈 인덱스만 1인 상태로 변수 pop을 넘겨받을 것.  
    pop에서의 인덱스와 매칭되는 키보드값은 다음과 같음.'''  
    q w e   0 1 2  
    a s d   3 4 5  
    z x c   6 7 8  
    def print_board(pop):  
    os.system("clear")
    for i in range(3): __# 세로로 3개의 행을 나타냄.
        for r in range(len(HOLE)): # HOLE의 길이만큼 반복하는 루프.
            for ii in range(3): # 가로로 3개의 열을 나타냄.
                index = 3*i + ii # 현재의 행과 열을 기반으로 `pop` 리스트에서 가져올 인덱스를 계산.
                if pop[index] == 1: # 현재 인덱스가 1인 경우 (즉, 해당 위치에 두더지가 나타난 경우)
                    print(MOLE[r], end='') # 두더지를 출력
                else: # (인덱스가 0인 경우, 즉, 해당 위치에 두더지가 나타나지 않은 경우)
                    print(HOLE[r], end='') # 구멍을 출력.
            print()     
# 5. 사용자가 두더지를 잡은 경우에 해당 인덱스만 찌그러진 두더지, 나머지 구멍를 출력하는 함수.
______________________________________________________________________
    def hit_board(pop):  '
    os.system("clear")
    for i in range(3): # 세로로 3개의 행을 나타냄.
        for r in range(len(HOLE)): # # HOLE의 길이만큼 반복하는 루프.
            for ii in range(3): # 가로로 3개의 열을 나타냄.
                index = 3*i + ii # 현재의 행과 열을 기반으로 `pop` 리스트에서 가져올 인덱스를 계산.
                if pop[index] == 1: # 현재 인덱스가 1인 경우 (즉, 해당 위치에 두더지가 나타난 경우)
                    print(HIT[r], end='') # 찌그러진 두더지를 출력.
                else:
                    print(HOLE[r], end='') # 구멍을 출력.
            print()
# 6. SCORE 글자판과 최종 점수를 출력하는 함수
-----------------------------------
    def score_board(points):
    os.system("clear")
    points = str(points) # 점수를 문자열로 변환.
    print('\n'*8) #  8번의 줄 바꿈을 통해 화면을 정리.
    for i in range(5): #  점수를 나타내는 각 숫자의 행을 나타냄.
        print(SCORE[i],end='') #  "SCORE" 텍스트를 출력.
        for n in range(len(points)): # points의 길이만큼 반복하는 루프를 시작. 이는 각 숫자를 나타냄.
            index = int(points[n])*5 # 현재 숫자에 대한 인덱스를 계산.
            # 문자열 points에서 n번째 자리의 숫자를 가져오고, 가져온 숫자를 정수로 변환함.
            # 숫자를 5배로 곱하는데, 이렇게 하는 이유는 각 숫자가 NUMS 리스트에서 5행으로 이루어져 있기 때문에.
            print(NUMS[i][index:index+5],end='') # NUMS 리스트에서 특정 숫자에 대한 행을 출력.
        print()                                  # index부터 index+5까지의 범위를 사용하여 해당 숫자에 대한 부분을 선택.
    print('\n'*10,end='')
# 7. 게임 라운드를 출력하는 함수.
사용자가 일정 점수를 넘겨 다음 라운드로 진입할 경우 라운드를 출력.
---------------------------------------------------
    def round_board(round):
    os.system("clear")
    print('\n'*8)
    for i in range(5): # 각 숫자를 나타내는 행을 나타냄.
        print(ROUND[i],end='') # "ROUND" 텍스트를 출력.
        index = round*5 # round는 현재 게임 라운드를 나타내는 변수, NUMS 리스트에 있는 각 숫자는 5개의 행으로 이루어져 있으며,
                        # 따라서 현재 라운드에 해당하는 인덱스를 구하기 위해서는 round에 5를 곱해야 함.
        print(NUMS[i][index:index+5],end='') # 해당 라운드 숫자에 대한 행을 출력.
        print()
    print('\n'*10,end='')
# 8. 게임이 끝났음을 알리는 함수.
GAME OVER 글자판을 세 번 깜박인다.
------------------------------
    def over_board():
    for _ in range(3): # GAME OVER" 텍스트를 세 번 깜박이게 하기 위함.
        os.system("clear") # 터미널 화면 지움
        print(OVER) # "GAME OVER" 텍스트를 출력.
        time.sleep(0.5)
        os.system("clear") # 터미널 화면 지움
        print("\n"*20)
        time.sleep(0.5)
hitmole2.py 함수의 설명.
============================
# 1. init 함수
점수 카운팅,사용자 입력키를 판별,게임 라운드 진행을 저장하는 속성
----------------------------------------------------------------------------
    def __init__(self):
        self.points = 0
        self.click = None
        self.cnt_round = 1
# 2. 랜덤으로 두더지가 나올 구멍 뽑는 함수  
0부터 8까지의 숫자 중 하나를 뽑아 그 수만 1이고 나머지는 0인 일차원 숫자 행렬 반환
-------------------------------------
    def pop_up(self,mole=None): # mole 매개변수는 두더지가 나올 구멍의 인덱스를 나타낸다.
                                # 이 매개변수는 기본값으로 None을 가지고 있으며, 호출 시 구멍의 인덱스를 제공하지 않으면 None으로 설정
        self.holes = np.zeros(9) # holes라는 클래스 속성을 만들어 0으로 초기화된 길이가 9인 numpy 배열로 설정하며, 이 배열은 두더지가 나올 구멍을 나타내는데 사용.
        self.holes[mole] = 1 # 만약 mole이 None이 아닌 경우, 해당 인덱스의 원소를 1로 설정하며, 이것이 두더지가 나올 구멍이 된다.
                             # 그 외의 경우(즉, mole이 None인 경우)에는 모든 원소가 0인 상태로 유지.
        return self.holes # 최종적으로 업데이트된 holes 배열을 반환. 이 배열은 두더지가 나온 구멍은 1로, 그 외의 구멍은 0으로 표시된 배열.
# 3. 사용자로 부터 키보드 값을 입력받는 함수.
----------------------------------------
    def wait_keyboard(self, timeout=None):
        def on_press(key): # 이 함수는 키가 눌렸을 때 실행되며, 눌린 키에 따라 self.click 변수에 특정 값이 할당.
            try:  # key.char 는 입력된 키보드값이 문자열이 아니면 오류가 남.
                if key == kb.Key.space: # 키의 문자 값을 얻어오기 위해 key.char를 사용
                                        # 그러나 만약 키가 문자가 아니라면 key.char를 사용할 수 없기 때문에 예외 처리를 함.
                    self.click = "space"
                    return False
                if key.char == 'q': # self.click에 다양한 값을 할당. 예를 들어, 'q' 키가 눌리면 self.click에 0을 할당하고,'w' 키가 눌리면 1을 할당.
                    self.click = 0
                    return False
                elif key.char == 'w':
                    self.click = 1
                    return False
                elif key.char == 'e':
                    self.click = 2
                    return False
                elif key.char == 'a':
                    self.click = 3
                    return False
                elif key.char == 's':
                    self.click = 4
                    return False
                elif key.char == 'd':
                    self.click = 5
                    return False
                elif key.char == 'z':
                    self.click = 6
                    return False
                elif key.char == 'x':
                    self.click = 7
                    return False
                elif key.char == 'c':
                    self.click = 8
                    return False
                else:
                    self.click = "Wrong Key"
                    return False
            except:
                self.click = "Wrong Key"
                return False

        with kb.Listener(on_press=on_press) as listener: # keyboard.Listener를 사용하여 키보드 입력을 감지하는 객체를 생성.
            self.click = None # 키보드 입력을 기다리기 전에 self.click을 초기화.
            if timeout: #  타임아웃이 설정되어 있다면, 입력을 기다리는 동안에 타이머를 시작하고, 타이머가 만료되면 listener.stop을 호출하여 키보드 리스너를 종료.
                timer = Timer(timeout, listener.stop)
                timer.start()
            listener.join() # 키보드 입력을 계속해서 기다리는데 사용자가 특정 키를 누를 때까지 기다리며, 타임아웃이 설정된 경우 타이머가 만료되면 종료.
        return self.click # 최종적으로 self.click 값을 반환.
# 4. 조작키를 알려주고 연습하는 튜토리얼 함수.  
랜덤으로 나타난 두더지가 사용자가 올바른 키를 입력할 때까지 사라지지 않고,  
튜토리얼을 멈추고 게임을 시작하고 싶으면 스페이스바를 누르도록 안내한다.
-------------------------------------------------------------
      def tutorial(self):
        boards.tutorial_board() # boards 객체의 tutorial_board 메서드를 호출하여 튜토리얼 보드를 출력. 이는 게임 화면을 보여주는 부분으로, 게임의 튜토리얼을 시각적으로 보여줌.
        while True:
            start_game = False
            mole = rd.choice(range(9)) # 0부터 8까지의 숫자 중에서 랜덤으로 하나를 선택하여 mole 변수에 저장. 이는 나타난 두더지의 위치를 나타냄.
            pop = self.pop_up(mole) # pop_up 메서드를 호출하여 두더지가 나타난 구멍을 나타내는 배열을 얻음.
            boards.print_board(pop) # 현재 게임 보드를 출력. pop 배열은 어떤 구멍에 두더지가 나타났는지 나타냄.
            print('''두더지 위치에 해당하는 키를 눌러 두더지를 잡으세요!    space를 누르면 게임시작


                    q      w      e

                    a      s      d

                    z      x      c

                  ''')
            while True:
                hit = False
                if self.click == "space": #사용자가 스페이스바를 누르면, 게임을 시작하는 신호로 start_game을 True로 설정하고 두 번째 무한 루프를 탈출.
                    start_game = True
                    break
                try:  # self.click = "wrong key"인 경우가 있기 때문에 리스트 인덱싱 오류를 피해야 함.
                    key = self.wait_keyboard() # 사용자로부터 키보드 입력 받음.
                    if self.holes[key] == 1: # : 만약 사용자가 입력한 키에 해당하는 구멍에 두더지가 있다면 (self.holes[key]가 1이라면),
                        boards.hit_board(pop) # boards.hit_board(pop)을 호출하여 두더지가 맞았음을 나타내는 화면을 출력하고,
                        time.sleep(0.25) # (time.sleep(0.25))동안 기다린후  hit 변수를 True로 설정합니다.
                        hit = True # hit 변수를 True로 설정.
                    else:
                        print(f'잘못된 키를 입력했습니다. {self.click}')
                except:
                    if self.click != "space":
                        print(f'잘못된 키를 입력했습니다. {self.click}')
                if hit: # 만약 두더지를 맞췄다면 내부 무한 루프를 탈출하여 다음 두더지의 나타남을 처리.
                    break
            if start_game: # : 만약 start_game이 True라면 외부 무한 루프를 탈출하여 게임을 시작.
                break
# 5. 한 라운드 안에서의 플레이 함수.
사용자가 두더지가 사라지기 전에 해당 키를 누르면, 두더지가 찌그러지는 효과와 함께 사용자 점수를 +10을 주고,
지정된 9개의 키 외의 키를 누르면 기회를 조금 더 줌.
----------------------------------------
        def play_round(self):
        for _ in range(10): # 각 라운드에서는 10번의 시도가 주어지고, 두더지가 랜덤으로 10번 나타남.
            mole = rd.choice(range(9)) #  0부터 8까지의 숫자 중에서 랜덤으로 하나를 선택하여 mole 변수에 저장.이는 나타난 두더지의 위치를 나타냄.
            pop = self.pop_up(mole) # pop_up 메서드를 호출하여 두더지가 나타난 구멍을 나타내는 배열을 얻음.
            boards.print_board(pop) # 현재 게임 보드를 출력. pop 배열은 어떤 구멍에 두더지가 나타났는지 나타냄.
            time_by_level = 1.0 - (0.2 * self.cnt_round) # 레벨에 따라 두더지가 나타나는 시간을 결정. 레벨이 높아질수록 두더지가 나타나는 시간이 짧아짐.
            key = self.wait_keyboard(time_by_level) # wait_keyboard 메서드를 호출하여 사용자로부터 키보드 입력을 받음.
            try:  # self.click = "wrong key"인 경우가 있기 때문에 리스트 인덱싱 오류를 피해야 함.
                if self.holes[key] == 1: # 사용자가 입력한 키에 해당하는 구멍에 두더지가 있다면,
                    self.points += 10 # 사용자의 점수를 10점 증가시키고
                    boards.hit_board(pop) # 두더지가 맞았음을 나타내는 화면을 출력.
                    time.sleep(0.15)
                else:
                    time.sleep(0.15)
            except: # try 에서 예외가 발생하면
                key = self.wait_keyboard(0.35-(0.05*self.cnt_round)) # 두더지가 나타나는 시간이 더 길어지도록 설정
                try:
                    if self.holes[key] == 1:
                        self.points += 10
                        boards.hit_board(pop)
                        time.sleep(0.15)
                except:
                    pass
            pop = np.zeros(9) # 두더지가 나타난 구멍을 다시 초기화하여 숨김 상태로 만듦.
            boards.print_board(pop) # 두더지가 사라진 상태의 게임 보드를 출력.
            time.sleep(0.1)
# 6. 전체 게임 진행 함수.
        def play(self, user):
        self.tutorial() # 먼저 튜토리얼을 진행.
        boards.start_board() # 게임을 시작할 때 보여지는 시작 화면을 출력.
        while True: # 게임 라운드를 반복.
            self.play_round() # play_round 메서드를 호출하여 한 라운드를 플레이함.
            boards.score_board(self.points) # 현재까지의 점수를 출력하는 화면을 보여줌.
            time.sleep(2.0) # 2초 동안 대기. 사용자가 점수를 확인할 시간을 주는 용도.
            self.cnt_round += 1 # 라운드 수를 증가.
            if (self.points != 100*(self.cnt_round-1)) and ((self.points < 100*(self.cnt_round-1)*0.8) or (self.cnt_round > 3)):
              # 현재 라운드에서의 점수를 판별하여 게임을 계속 진행할지를 결정. 만약 이 조건을 만족하지 않으면 게임이 종료.
              # 플레이어의 점수가 해당 라운드의 최대 가능 점수의 80% 미만이거나, 라운드 횟수가 3보다 큰 경우.
                boards.over_board() # 게임이 종료되면 종료 화면을 출력하고 루프를 탈출.
                break
            boards.round_board(self.cnt_round) # 게임 보드를 출력하는데, 현재 라운드 번호(self.cnt_round)에 해당하는 화면을 출력하는 역할.
            time.sleep(1.0)
        HitMole.rank[user] = self.points # 현재 사용자의 점수를 랭킹에 저장.
        HitMole.rank = dict(sorted(HitMole.rank.items(), key=lambda x:x[1], reverse=True)) # 랭킹을 점수에 따라 내림차순으로 정렬.
        rank=1
        for name,score in HitMole.rank.items():
            print('', rank, name + ':', score, sep='\t')
            print()
            rank+=1
        time.sleep(1.0)

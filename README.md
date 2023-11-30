__전체 코드의 대략적 설명__  
def play(self, user):   
        __전체 게임 진행__
        __튜토리얼 - 1라운드 - 점수출력, 판별 (- 2라운드 - 점수 - 3라운드 - 점수) - 랭킹출력__      
        self.tutorial() __# 먼저 튜토리얼 실행함__  
        boards.start_board() __# 게임을 시작할 때 보여지는 시작 화면을 출력함__  
        while True:      
            self.play_round()  __# 게임을 시작할 때 보여지는 시작 화면을 출력함__  
            boards.score_board(self.points) __# 현재까지의 점수를 출력함__  
            time.sleep(2.0) __# 2초동안 멈추어 사용자에게 점수화면을 보여줌__  
            self.cnt_round += 1 __# 라운드 수를 증가__  
            if (self.points != 100*(self.cnt_round-1)) and ((self.points < 100*(self.cnt_round-1)*0.8) or (self.cnt_round > 3)):   
            __# 현재 라운드에서의 점수를 판별하여 게임을 계속 진행할지를 결정, 만약 이 조건을 만족하지 않으면 게임 종료__  
            __# 플레이어의 점수가 해당 라운드의 최대 가능 점수의 80% 미만이거나, 라운드 횟수가 3보다 큰 경우에도 종료__   
                boards.over_board() __# 게임이 종료되면 종료화면을 출력하고 루프를 탈출.__    
                break  
            boards.round_board(self.cnt_round) __# 현재 라운드 번호를 화면에 출력하는 화면__  
            time.sleep(1.0)  
        HitMole.rank[user] = self.points __# 사용자의 점수를 랭크에 저장.__    
        HitMole.rank = dict(sorted(HitMole.rank.items(), key=lambda x:x[1], reverse=True)) __# 렝크를 점수에 따라 내림차순으로 정렬__    
        rank=1  
        for name,score in HitMole.rank.items():  
            print('', rank, name + ':', score, sep='\t')  
            print()  
            rank+=1  
        time.sleep(1.0)  
__보드판 코드 설명__  
def hitmole_board():  
    __게임 시작을 알림  
    HIT MOLE 글자판을 한 번 깜박이도록 한다.__
    os.system("clear")  __# 터미널 화면을 지우는 역할.__  
    print(HIT_MOLE)  __# HIT_MOLE이라는 변수에 저장된 문자열을 출력.__  
    time.sleep(1.5)  __# 프로그램을 1.5초 동안 일시 중지. "HIT MOLE"이라는 텍스트를 화면에 표시.__  
    os.system("clear") __# 다시 화면을 지우고, 이전에 출력된 "HIT MOLE" 텍스트를 지우고 깨끗한 화면을 만듦__  
    print("\n"*20) __# 20번의 줄 바꿈(\n)을 통해 20개의 빈 줄을 출력. 화면이 추가적으로 깨끗하게 정리__  
    time.sleep(0.5) __# 0.5초 동안 프로그램을 일시 중지. 빈 화면을 화면에 표시.__  
def tutorial_board():  
    __튜토리얼 시작을 알림  
    TUTORIAL 글자판을 한 번 깜박이도록 한다.__  
    os.system("clear") __# 터미널 화면을 지우는 역할.__  
    print(TUTORIAL) __# TUTORIAL이라는 변수에 문자열을 출력. "TUTORIAL"이라는 텍스트를 화면에 표시하는 역할.__  
    time.sleep(1.5) __# 프로그램을 1.5초 동안 일시 중지. 이로써 "TUTORIAL"이라는 텍스트가 1.5초 동안 화면에 표시.__  
    os.system("clear") __# 다시 화면을 지움.__  
    print("\n"*20)
    time.sleep(0.5) __# 0.5초 동안 프로그램을 일시 중지. 빈 화면을 화면에 표시.__  
def start_board():    
    __게임 시작 전 카운트 다운과 함께 시작을 알림  
    3,2,1의 카운트 후 GAME START 글자판을 깜박이도록 한다.__    
    os.system("clear") __# 터미널 화면을 지우는 역할.__  
    for i in range(3): __# 3번 반복하는 루프를 시작.(이는 3, 2, 1의 카운트 다운)__  
        print('\n'*8,end='') __# 8번의 줄 바꿈을 통해 화면을 정리.__  
        index = (3-i)*5 __# 현재 카운트 값에 따라 숫자를 가져오기 위한 인덱스를 계산.__  
        for l in range(5):
            print(' '*26, NUMS[l][index:index+5]) __# 26칸의 공백을 출력한 후, `NUMS` 리스트에서 해당 인덱스 범위의 숫자를 출력__  
        print("\n"*8) __# 숫자를 출력한 후 8번의 줄 바꿈을 통해 화면을 정리.__  
        time.sleep(0.5)
        os.system("clear") __# 화면을 지움.__  
        print("\n"*21) __# 21번의 줄 바꿈을 통해 화면을 정리.__  
        time.sleep(0.5)
        os.system("clear")
    print(START) __# "GAME START" 텍스트를 출력.__  
    time.sleep(1.0)  
def print_board(pop):   
    __현재 랜덤으로 튀어나온 두더지를 출력  
    랜덤으로 숫자를 뽑아둔 pop_up을 받아 해당 인덱스만 두더지를 출력하고  
    나머지는 구멍을 출력하도록 한다.__

    ''' pop = [0 0 0 0 0 0 0 0 0]
    랜덤으로 두더지가 들어갈 인덱스만 1인 상태로 변수 pop을 넘겨받을 것.
    pop에서의 인덱스와 매칭되는 키보드값은 다음과 같음.'''
    q w e   0 1 2
    a s d   3 4 5
    z x c   6 7 8
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
    def hit_board(pop):  
    '''사용자가 두더지를 잡은 경우에
    랜덤으로 숫자를 뽑아둔 pop_up을 받아 해당 인덱스만 찌그러진 두더지를 출력하고
    나머지는 구멍을 출력하도록 한다.'''
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

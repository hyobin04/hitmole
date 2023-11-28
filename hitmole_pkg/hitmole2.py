import numpy as np
import random as rd
import time
from pynput import keyboard as kb
from threading import Timer
import hitmole_pkg.hitmole_boards as boards

class LengthError(Exception):
    def __init__(self):
        super().__init__('6자 이내로 작성')

class AlphabetError(Exception):
    def __init__(self):
        super().__init__('영어 소문자로 작성')

class HitMole:
    '''
    두더지 게임 클래스

    여러 사용자로부터 이름을 입력받고 게임을 시켜 랭킹을 띄워준다.
    이름을 입력하면 튜토리얼을 진행할 수 있으며,
    게임은 총 3라운드 구성으로 라운드를 올라갈수록 두더지가 빨리 숨는다.
    각 라운드에서 10마리의 두더지가 무작위로 나타나며, 한 마리 당 10점씩 오른다.
    라운드를 진행하며 누적 두더지 수의 80% 이상을 잡았으면 다음 라운드로 넘어간다.
    ex) 1라운드에 9마리, 2라운드에 7마리 잡아도 전체 20마리 중 80%를 잡았으므로 3라운드를 진행할 수 있다.
    기본적으로 3라운드까지 할 수 있지만, 만점(300점)을 달성한다면 숨겨진 4라운드로 넘어간다.
    '''
    
    rank = {}

    def __init__(self):
        '''
        점수 카운팅을 위한 속성과, 사용자 입력키를 판별하기 위한 속성, 그리고 게임 라운드 진행을 저장하는 속성
        '''
        self.points = 0
        self.click = None
        self.cnt_round = 1
        
    def pop_up(self,mole=None):
        '''
        랜덤으로 두더지가 나올 구멍 뽑기
        0부터 8까지의 숫자 중 하나를 뽑아 그 수만 1이고 나머지는 0인 일차원 숫자 행렬 반환
        '''
        self.holes = np.zeros(9)
        self.holes[mole] = 1
        return self.holes

    def wait_keyboard(self, timeout=None):
        '''사용자로부터 키보드 입력'''
        def on_press(key):
            try:  # key.char 는 입력된 키보드값이 문자열이 아니면 오류가 남.
                if key == kb.Key.space:
                    self.click = "space"
                    return False
                if key.char == 'q':
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

        with kb.Listener(on_press=on_press) as listener:
            self.click = None
            if timeout:
                timer = Timer(timeout, listener.stop)
                timer.start()
            listener.join()
        return self.click
    
    def tutorial(self):
        '''
        조작 키를 알려주고 연습하는 튜토리얼 메소드
        랜덤으로 나타난 두더지가 사용자가 올바른 키를 입력할 때까지 사라지지 않는다.
        튜토리얼을 멈추고 게임을 시작하고 싶으면 스페이스바를 누르도록 안내한다.
        '''

        boards.tutorial_board()
        while True:
            start_game = False
            mole = rd.choice(range(9))
            pop = self.pop_up(mole)
            boards.print_board(pop)
            print('''두더지 위치에 해당하는 키를 눌러 두더지를 잡으세요!    space를 누르면 게임시작
                  

                    q      w      e
                  
                    a      s      d
                  
                    z      x      c
                  
                  ''')
            while True:
                hit = False
                if self.click == "space":
                    start_game = True
                    break
                try:  # self.click = "wrong key"인 경우가 있기 때문에 리스트 인덱싱 오류를 피해야 함.
                    key = self.wait_keyboard()
                    if self.holes[key] == 1:
                        boards.hit_board(pop)
                        time.sleep(0.25)
                        hit = True
                    else:
                        print(f'잘못된 키를 입력했습니다. {self.click}')
                except:
                    if self.click != "space":
                        print(f'잘못된 키를 입력했습니다. {self.click}')
                if hit:
                    break
            if start_game:
                break

    def play_round(self):
        '''
        한 라운드 안에서의 플레이
        사용자가 두더지가 사라지기 전에 해당 키를 누르면
        두더지가 찌그러지는 효과와 함께 사용자 점수를 +10
        지정된 9개의 키 외의 키를 누르면 기회를 조금 더 줌.
        '''
        for _ in range(10):
            mole = rd.choice(range(9))
            pop = self.pop_up(mole)
            boards.print_board(pop)
            time_by_level = 1.0 - (0.2 * self.cnt_round)
            key = self.wait_keyboard(time_by_level)
            try:  # self.click = "wrong key"인 경우가 있기 때문에 리스트 인덱싱 오류를 피해야 함.
                if self.holes[key] == 1:
                    self.points += 10
                    boards.hit_board(pop)
                    time.sleep(0.15)
                else:
                    time.sleep(0.15)
            except:
                key = self.wait_keyboard(0.35-(0.05*self.cnt_round))
                try:
                    if self.holes[key] == 1:
                        self.points += 10
                        boards.hit_board(pop)
                        time.sleep(0.15)
                except:
                    pass
            pop = np.zeros(9)
            boards.print_board(pop)
            time.sleep(0.1)

    def play(self, user):
        '''
        전체 게임 진행
        튜토리얼 - 1라운드 - 점수출력, 판별 (- 2라운드 - 점수 - 3라운드 - 점수) - 랭킹출력
        '''
        self.tutorial()
        boards.start_board()
        while True:
            self.play_round()
            boards.score_board(self.points)
            time.sleep(2.0)
            self.cnt_round += 1
            if (self.points != 100*(self.cnt_round-1)) and ((self.points < 100*(self.cnt_round-1)*0.8) or (self.cnt_round > 3)):
                boards.over_board()
                break
            boards.round_board(self.cnt_round)
            time.sleep(1.0)
        HitMole.rank[user] = self.points
        HitMole.rank = dict(sorted(HitMole.rank.items(), key=lambda x:x[1], reverse=True))
        rank=1
        for name,score in HitMole.rank.items():
            print('', rank, name + ':', score, sep='\t')
            print()
            rank+=1
        time.sleep(1.0)

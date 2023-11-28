from hitmole_pkg.hitmole2 import *
import hitmole_pkg.hitmole_boards as boards

if __name__ == '__main__':
    boards.hitmole_board()
    while True:
        user = input('닉네임을 입력하세요(enter 시 게임 종료): ')
        try:
            if not user:
                break
            elif len(user) > 6:
                raise LengthError
            elif set(user)&set('abcdefghijklmnopqrstuvwxyz') != set(user):
                raise AlphabetError
            HitMole().play(user)
        except Exception as e :
            print('Error raised:', e)

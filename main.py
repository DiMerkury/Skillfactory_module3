from board import Boards
from ai import Ai
from user import User


player1_board = Boards()
player2_board = Boards()

player1 = Ai()
#player2 = Ai()
player2 = User()

player1.build_ship(player1_board)
player1_board.print_board()

player2.build_ship(player2_board)
player2_board.print_board()

nom_player = 1
step_player1 = 1
step_player2 = 1
end_ship = False
while step_player1 < 37 and step_player2 < 37 and not end_ship: #стоит ограничене на кол-во ходов для каждого игрока до тестирования
    if nom_player == 1:
        print('\nСейчас ход игрока номер 1\n')
        print('Вот корабли соперника:') #возможно лучше не показывать, отличная подсказка
        player2.display_ship() #возможно лучше не показывать, отличная подсказка
        print(f'Вот поле игрока номер 2:')
        player2_board.print_board(True)
#        player2_board.print_board()
        print('Стреляем по кораблям игрока 2')
        if player1.fire(player2_board, player2.get_arr_ship) == 'miss':
                nom_player = 2
        print('Шаг:', step_player1)
        step_player1 += 1
        end_ship = player2.end_ship()
        print('Вот корабли соперника:') #возможно лучше не показывать, отличная подсказка
        player2.display_ship() #возможно лучше не показывать, отличная подсказка
    else:
        print('\nСейчас ход игрока номер 2\n')
        print('Вот корабли соперника:') #возможно лучше не показывать, отличная подсказка
        player1.display_ship() #возможно лучше не показывать, отличная подсказка
        print(f'Вот поле игрока номер 1:')
        player1_board.print_board(True)
#        player1_board.print_board()
        print('Стреляем по кораблям игрока 1')
        if player2.fire(player1_board, player1.get_arr_ship) == 'miss':
                nom_player = 1
        print('Шаг:', step_player2)
        step_player2 += 1
        end_ship = player1.end_ship()
        print('Вот корабли соперника:') #возможно лучше не показывать, отличная подсказка
        player1.display_ship() #возможно лучше не показывать, отличная подсказка    
         
print('Игра окончена \nИтоги:')
print('Корабли игрока 1:')
player1.display_ship()
print('Корабли игрока 2:')
player2.display_ship()
print('Выиграл игрок:', '1' if nom_player != 1 else '2')

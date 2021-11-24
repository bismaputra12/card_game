'''
Card drinking game
Author: Emerald Bismaputra
'''

# put all of your import statements below this line and then delete this comment
import random
import os
# put all of your function definitions below this line and then delete this comment

def game():
    one = 'suit jepang sama orang sebelah kanan lo! yang kalah minum'
    two = 'dare or drink pilih 1 orang'
    three = 'bikin lawakan, minum kalo gaada yg ketawa'
    four = 'handstand! kalo gamau minum'
    five = 'pilih 2 teman! mereka minum!'
    six = '13 x 13 berapa? jawab tanpa kalkulator. kalo salah minum!'
    seven = 'telfon contact random, kalo gamau, minum'
    eight = 'apa warna kesukaan orang di sebelah kanan lo? kalo salah minum'
    nine = 'abc 5 dasar: pilih kategori. yang kalah minum!'
    ten = 'ping pong pang! yang kalah minum'
    eleven = 'staring contest. yang kedip pertama minum!'
    twelve = 'yang paling pendek minum'
    thirteen = 'yang berdiri pertama minum'
    fourteen = 'ceritakan hal memalukan di hidupmu'
    fifteen = 'Teman lawan jenis yang terakhir kamu chat selain pacar? dan tentang apa?'
    sixteen = 'yang cowo minum'
    seventeen = 'yang cewe minum'
    eighteen = 'cium ketek orang sebelah kanan lo kalo skip minum'
    nineteen = 'swap attack card! boleh kasi tantangan yang lo dapet ke temen lo'
    twenty = 'minum setengah gelas. boleh pake mixer.'
    twenty_one = 'setiap pertanyaan harus dimulai dengan angka yang berurutan'
    twenty_two = '12 x 12 berapa? jawab tanpa kalkulator. kalo salah minum!'
    twenty_three = 'semuanya minum'
    twenty_four = 'yang pernah berantem minum'
    twenty_five = 'truth or drink! yang dapet kartu ini pilih orang dan kasi pertanyaan'
    twenty_six = 'Apa hal paling kejam yang pernah kamu lakukan pada seseorang?'
    twenty_seven = 'kirim pesen ke orang dan ajak dia kencan (harus random)'
    twenty_eight = 'cium kaki orang di sebelah kiri'
    twemty_nine = 'muter 8x dan lari 10m'
    thirty = 'cabut rambut 1 helai'
    thirty_three = 'sebut 1 mantan yg kamu paling sayang'
    pick_a_card = random.randint(1, 33)
    if pick_a_card == 1:
        return one
    elif pick_a_card == 2:
        return two
    elif pick_a_card == 3:
        return three
    elif pick_a_card == 4:
        return four
    elif pick_a_card == 5:
        return five
    elif pick_a_card == 6:
        return six
    elif pick_a_card == 7:
        return seven
    elif pick_a_card == 8:
        return eight
    elif pick_a_card == 9:
        return nine
    elif pick_a_card == 10:
        return ten
    elif pick_a_card == 11:
        return eleven
    elif pick_a_card == 12:
        return twelve
    elif pick_a_card == 13:
        return thirteen
    elif pick_a_card == 14:
        return fourteen
    elif pick_a_card == 15:
        return fifteen
    elif pick_a_card == 16:
        return sixteen
    elif pick_a_card == 17:
        return seventeen
    elif pick_a_card == 18:
        return eighteen
    elif pick_a_card == 19:
        return nineteen
    elif pick_a_card == 20:
        return twenty
    elif pick_a_card == 21:
        return twenty_one
    elif pick_a_card == 22:
        return twenty_two
    elif pick_a_card == 23:
        return twenty_three
    elif pick_a_card == 24:
        return twenty_four
    elif pick_a_card == 25:
        return twenty_five
    elif pick_a_card == 26:
        return twenty_six
    elif pick_a_card == 27:
        return twenty_seven
    elif pick_a_card == 28:
        return twenty_eight
    elif pick_a_card == 29:
        return twenty_nine
    elif pick_a_card == 30:
        return thirty
    elif pick_a_card == 31:
        return twenty_one
    elif pick_a_card == 32:
        return twenty_two
    elif pick_a_card == 33:
        return twenty_three

#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    print('\n')
    players = input('Enter the number of players (2, 4 or 6): ')
    if players == '2':
        print('\n')
        player_one = input('Enter player one name: ')
        player_two = input('Enter player two name: ')
        print('\n')
        print('2 players ready to play!')
        print(player_one + ' and ' + player_two)
        print('\n')
        for i in range(1000):
            players = [player_one, player_two, player_one, player_two, player_one, player_two, player_one, 
                    player_two, player_one, player_two, player_one, player_two, player_one, player_two,
                    player_one, player_two, player_one, player_two, player_one, player_two, player_one, player_two, 
                    player_one, player_two, player_one, player_two, player_one, player_two, player_one, player_two,
                    player_one, player_two, player_one, player_two, player_one, player_two, player_one, player_two, 
                    player_one, player_two, player_one, player_two, player_one, player_two, player_one, player_two, 
                    player_one, player_two, player_one, player_two, player_one, player_two, player_one, player_two, 
                    player_one, player_two, player_one, player_two, player_one, player_two, player_one, player_two, 
                    player_one, player_two, player_one, player_two, player_one, player_two, player_one, player_two, 
                    player_one, player_two, player_one, player_two, player_one, player_two, player_one, player_two, 
                    player_one, player_two, player_one, player_two, player_one, player_two, player_one, player_two, 
                    player_one, player_two, player_one, player_two, player_one, player_two, player_one, player_two, 
                    player_one, player_two, player_one, player_two]
            player_turn = print('==============================', players[i] + '\'s' , 'turn!', '==============================')
            print('\n')
            os.system("say 'Press enter to get your card'")
            start = input('Press <enter> to start!') 
            print('\n')
            print(str(game()))
            print('\n')
            os.system("say 'Press enter to continue or type no to stop playing'")
            continue_or_close = input('Press <enter> to continue or write \'NO\' to stop playing: ')
            print('\n')
            if continue_or_close == '':
                continue
            elif continue_or_close == 'NO' or continue_or_close == 'no':
                os.system("say 'Thank you for playing'")
                print('Thank you for playing')
                break

    elif players == '4':
        print('\n')
        player_one = input('Enter player one name: ')
        player_two = input('Enter player two name: ')
        player_three = input('Enter player three name: ')
        player_four = input('Enter player four name: ')
        print('\n')
        print('4 players ready to play!')
        print(player_one + ', ' + player_two + ', ' + player_three + ' and ' + player_four)
        print('\n')
        for i in range(1000):
            players = [player_one, player_two, player_three, player_four, player_one, player_two, 
                    player_three, player_four, player_one, player_two, player_three, player_four, 
                    player_one, player_two, player_three, player_four, player_one, player_two, 
                    player_three, player_four, player_one, player_two, player_three, player_four, 
                    player_one, player_two, player_three, player_four, player_one, player_two, 
                    player_three, player_four, player_one, player_two, player_three, player_four, 
                    player_one, player_two, player_three, player_four, player_one, player_two, 
                    player_three, player_four, player_one, player_two, player_three, player_four, 
                    player_one, player_two, player_three, player_four, player_one, player_two, 
                    player_three, player_four]
            player_turn = print('==============================', players[i] + '\'s' , 'turn!' , '==============================')
            print('\n')
            os.system("say 'Press enter to get your card'")
            start = input('Press <enter> to start!')
            print('\n')
            print(str(game()))
            print('\n')
            os.system("say 'Press enter to continue or type no to stop playing'")
            continue_or_close = input('Press <enter> to continue or write \'NO\' to stop playing: ')
            print('\n')
            if continue_or_close == '':
                continue
            elif continue_or_close == 'NO' or continue_or_close == 'no':
                os.system("say 'Thank you for playing'")
                print('Thank you for playing')
                break

    elif players == '6':
        print('\n')
        player_one = input('Enter player one name: ')
        player_two = input('Enter player two name: ')
        player_three = input('Enter player three name: ')
        player_four = input('Enter player four name: ')
        player_five = input('Enter player five name: ')
        player_six = input('Enter player six name: ')
        print('\n')
        print('6 players ready to play!')
        print(player_one + ', ' + player_two + ', ' + player_three + ', ' + player_four + ', ' + player_five + ' and ' + player_six)
        print('\n')
        for i in range(1000):
            players = [player_one, player_two, player_three, player_four, player_five, player_six, player_one, player_two, 
                    player_three, player_four, player_five, player_six, player_one, player_two, player_three, player_four, 
                    player_five, player_six, player_one, player_two, player_three, player_four, player_five, player_six, 
                    player_one, player_two, player_three, player_four, player_five, player_six, player_one, player_two, 
                    player_three, player_four, player_five, player_six, player_one, player_two, player_three, player_four, 
                    player_five, player_six, player_one, player_two, player_three, player_four, player_five, player_six, player_one, 
                    player_two, player_three, player_four, player_five, player_six, player_one, player_two, player_three, player_four, 
                    player_five, player_six, player_one, player_two, player_three, player_four, player_five, player_six, player_one, 
                    player_two, player_three, player_four, player_five, player_six]
            player_turn = print('==============================', players[i] + '\'s' , 'turn!', '==============================')
            print('\n')
            os.system("say 'Press enter to get your card'")
            start = input('Press <enter> to start!')
            print('\n')
            print(str(game()))
            print('\n')
            os.system("say 'Press enter to continue or type no to stop playing'")
            continue_or_close = input('Press <enter> to continue or write \'NO\' to stop playing: ')
            print('\n')
            if continue_or_close == '':
                continue
            elif continue_or_close == 'NO' or continue_or_close == 'no':
                os.system("say 'Thank you for playing'")
                print('Thank you for playing')
                break



if __name__ == '__main__':
    main()

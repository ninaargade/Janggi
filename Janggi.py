# Author: Nina Argade
# Date: 3/11/2021
# Description: The following program contains a class that executes the game Janggi, which is the Korean version of
# chess. The program represents the backend of the game, where there is a way for keeping track of the game board,
# game pieces, player turns, and game state. There is a method to make a move which takes in algebraic notation
# coordinates representing spaces on the board. There are many various helper functions that execute game play, and
# finally, there are methods to verify if a player is in check or checkmate, which indicate if the game has been won.

# noinspection PyUnreachableCode
class JanggiGame:
    """Class represents the Korean chess game Janggi. This class contains an init method to initialize the game board,
    turn taking and game state. The class contains many methods to execute game play for the various pieces, as well as
    a method to check if a player is in check or checkmate."""

    def __init__(self):
        """Initializes all data members for class JanggiGame, including a board representation in a 2D array, a
        dictionary to convert algebraic notation to numbered coordinates, a turn keeper, and game state."""

        # initialize board as 2-D array containing game pieces at coordinates
        self._board_space = [
            ["RChariot", "RElephant", "RHorse", "RGuard", " ", "RGuard", "RElephant", "RHorse", "RChariot"],
            [" ", " ", " ", " ", "RGeneral", " ", " ", " ", " "],
            [" ", "RCannon", " ", " ", " ", " ", " ", "RCannon", " "],
            ["RSoldier", " ", "RSoldier", " ", "RSoldier", " ", "RSoldier", " ", "RSoldier"],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            ["BSoldier", " ", "BSoldier", " ", "BSoldier", " ", "BSoldier", " ", "BSoldier"],
            [" ", "BCannon", " ", " ", " "," ", " ", "BCannon", " "],
            [" ", " ", " ", " ", "BGeneral", " ", " ", " ", " "],
            ["BChariot", "BElephant", "BHorse", "BGuard", " ", "BGuard", "BElephant", "BHorse", "BChariot"],
        ]

        # initialize a dictionary to convert algebraic board notation into coordinates to access game pieces
        self._board_dict = {"a1": "00", "b1": "01", "c1": "02", "d1": "03", "e1": "04", "f1": "05", "g1": "06",
                            "h1": "07", "i1": "08", "a2": "10", "b2": "11", "c2": "12", "d2": "13", "e2": "14",
                            "f2": "15", "g2": "16", "h2": "17", "i2": "18", "a3": "20", "b3": "21", "c3": "22",
                            "d3": "23", "e3": "24", "f3": "25", "g3": "26", "h3": "27", "i3": "28", "a4": "30",
                            "b4": "31", "c4": "32", "d4": "33", "e4": "34", "f4": "35", "g4": "36", "h4": "37",
                            "i4": "38", "a5": "40", "b5": "41", "c5": "42", "d5": "43", "e5": "44", "f5": "45",
                            "g5": "46", "h5": "47", "i5": "48", "a6": "50", "b6": "51", "c6": "52", "d6": "53",
                            "e6": "54", "f6": "55", "g6": "56", "h6": "57", "i6": "58", "a7": "60", "b7": "61",
                            "c7": "62", "d7": "63", "e7": "64", "f7": "65", "g7": "66", "h7": "67", "i7": "68",
                            "a8": "70", "b8": "71", "c8": "72", "d8": "73", "e8": "74", "f8": "75", "g8": "76",
                            "h8": "77", "i8": "78", "a9": "80", "b9": "81", "c9": "82", "d9": "83", "e9": "84",
                            "f9": "85", "g9": "86", "h9": "87", "i9": "88", "a10": "90", "b10": "91", "c10": "92",
                            "d10": "93", "e10": "94", "f10": "95", "g10": "96", "h10": "97", "i10": "98"}

        self._turn = "Blue"  # Blue player starts the game

        self._game_state = "UNFINISHED"  # default game state; can change to RED_WON or BLUE_WON

    def get_turn(self):
        """Method to get whose turn it is."""
        return self._turn

    def set_turn(self, team):
        """Method to set whose turn it is. Can alternate between team Blue and team Red."""
        self._turn = team
        return self._turn

    def get_game_state(self):
        """Method to get game state. Default status is UNFINISHED."""
        return self._game_state

    def set_game_state(self, state):
        """Method to set the game state to the player who has won. If a team has been checkmated, the game state will
        be set the opposite team having won."""
        self._game_state = state  # can be RED_WON or BLUE_WON
        return self._game_state

    def is_in_check(self, team):
        """Method to check if the passed parameter team color is in check. This method is called at the end
        of every turn, which means it is called at the end of the make_move method. Method will return True if the
        player is in check and False if the player is not"""

        if team == "red":
            for i in range(10):  # iterate through game board rows
                for j in range(9):  # iterate through game board columns
                    if self._board_space[i][j] == "RGeneral":
                        red_general_coordinate = str(i) + str(j)  # find 2D array coordinate of red general

                        for algebraic_space, coordinate in self._board_dict.items():
                            if coordinate == red_general_coordinate:
                                red_general_space = algebraic_space   # find key space corresponding to red general

                                key_list = []
                                for key in self._board_dict:
                                    key_list.append(key)
                                key_list.remove(red_general_space)  # all potential piece spaces (minus king space)
                                for key in key_list:  # check if any piece can kill king
                                    board_space_piece = self._board_dict[key]  # convert dict key to board space
                                    key_row = int(board_space_piece[0])
                                    key_column = int(board_space_piece[1])

                                    if self._board_space[key_row][key_column] == "BSoldier":
                                        status = self.blue_soldier_validate_move(key, red_general_space)
                                        if status is True:  # if piece can kill king
                                            return True
                                    if self._board_space[key_row][key_column] == "BCannon":
                                        status = self.blue_cannon_validate_move(key, red_general_space)
                                        if status is True:
                                            return True
                                    if self._board_space[key_row][key_column] == "BChariot":
                                        status = self.blue_chariot_validate_move(key, red_general_space)
                                        if status is True:
                                            return True
                                    if self._board_space[key_row][key_column] == "BElephant":
                                        status = self.blue_elephant_validate_move(key, red_general_space)
                                        if status is True:
                                            return True
                                    if self._board_space[key_row][key_column] == "BHorse":
                                        status = self.blue_horse_validate_move(key, red_general_space)
                                        if status is True:
                                            return True
                                    if self._board_space[key_row][key_column] == "BGuard":
                                        status = self.blue_guard_validate_move(key, red_general_space)
                                        if status is True:
                                            return True
                                    if self._board_space[key_row][key_column] == "BGeneral":
                                        status = self.blue_general_validate_move(key, red_general_space)
                                        if status is True:
                                            return True

                                # if none of the above is true, then king cannot be killed by opposing team piece
                                # which means check status is False
                                return False

        if team == "blue":
            for i in range(10):  # iterate through game board rows
                for j in range(9):  # iterate through game board columns
                    if self._board_space[i][j] == "BGeneral":
                        blue_general_coordinate = str(i) + str(j)  # find 2D array coordinate of blue general

                        for algebraic_space, coordinate in self._board_dict.items():
                            if coordinate == blue_general_coordinate:
                                blue_general_space = algebraic_space  # find key space corresponding to blue general

                                key_list = []
                                for key in self._board_dict:
                                    key_list.append(key)
                                key_list.remove(blue_general_space)  # all potential piece spaces (minus king space)
                                for key in key_list:  # check if any piece can kill king
                                    board_space_piece = self._board_dict[key]  # convert dict key to board space
                                    key_row = int(board_space_piece[0])
                                    key_column = int(board_space_piece[1])

                                    if self._board_space[key_row][key_column] == "RSoldier":
                                        status = self.red_soldier_validate_move(key, blue_general_space)
                                        if status is True:  # if piece can kill king
                                            return True
                                    if self._board_space[key_row][key_column] == "RCannon":
                                        status = self.red_cannon_validate_move(key, blue_general_space)
                                        if status is True:
                                            return True
                                    if self._board_space[key_row][key_column] == "RChariot":
                                        status = self.red_chariot_validate_move(key, blue_general_space)
                                        if status is True:
                                            return True
                                    if self._board_space[key_row][key_column] == "RElephant":
                                        status = self.red_elephant_validate_move(key, blue_general_space)
                                        if status is True:
                                            return True
                                    if self._board_space[key_row][key_column] == "RHorse":
                                        status = self.red_horse_validate_move(key, blue_general_space)
                                        if status is True:
                                            return True
                                    if self._board_space[key_row][key_column] == "RGuard":
                                        status = self.red_guard_validate_move(key, blue_general_space)
                                        if status is True:
                                            return True
                                    if self._board_space[key_row][key_column] == "RGeneral":
                                        status = self.red_general_validate_move(key, blue_general_space)
                                        if status is True:
                                            return True

                                # if none of the above is true, then king cannot be killed by opposing team piece
                                # which means check status is False
                                return False

    def is_in_checkmate_blue(self):
        """Method to check if the Blue team has been checkmated. This method is called at the end of every turn, which
        means it is called at the end of the make_move method, after the is_in_check method is called. Method will
        return True if the player has been checkmated and False if the player is not."""

        for i in range(10):  # iterate through game board rows
            for j in range(9):  # iterate through game board columns
                if self._board_space[i][j] == "BGeneral":
                    blue_general_coordinate = str(i) + str(j)  # find 2D array coordinate of blue general

                    for algebraic_space, coordinate in self._board_dict.items():
                        if coordinate == blue_general_coordinate:
                            blue_general_space = algebraic_space  # find key space corresponding to blue general

                    # list of coordinate spaces blue king could move to to get out of check
                    coordinate_list = [str(i)+str(j-1), str(i)+str(j+1), str(i-1)+str(j-1), str(i-1)+str(j),
                                       str(i-1)+str(j+1), str(i+1)+str(j-1), str(i+1)+str(j), str(i+1)+str(j+1)]

                    # list of board dictionary key spaces blue king could move to to get out of check
                    potential_king_space_key_list = []
                    for key, value in self._board_dict.items():
                        for coordinate in coordinate_list:
                            if value == coordinate in coordinate_list:
                                potential_king_space_key_list.append(key)

                                any_piece_key_list = []
                                for piece_key in self._board_dict:
                                    any_piece_key_list.append(piece_key)  # list of all piece locations
                                any_piece_key_list.remove(blue_general_space)  # remove king location
                                for piece_key in any_piece_key_list:  # check if any piece can kill king
                                    board_space_piece = self._board_dict[piece_key]  # convert dict key to board coord
                                    piece_key_row = int(board_space_piece[0])  # convert dict key to board coord row
                                    piece_key_column = int(board_space_piece[1])  # convert dict key to coord column

                                    # check if any potential king space will cause check (again)
                                    for king_space in potential_king_space_key_list:
                                        if self._board_space[piece_key_row][piece_key_column] == "RSoldier":
                                            status = self.red_soldier_validate_move(piece_key, king_space)
                                            if status is True:  # if piece can kill king
                                                self.set_game_state("RED_WON")  # checkmate of blue king, so red wins
                                                return True
                                        if self._board_space[piece_key_row][piece_key_column] == "RCannon":
                                            status = self.red_cannon_validate_move(piece_key, king_space)
                                            if status is True:
                                                self.set_game_state("RED_WON")
                                                return True
                                        if self._board_space[piece_key_row][piece_key_column] == "RChariot":
                                            status = self.red_chariot_validate_move(piece_key, king_space)
                                            if status is True:
                                                self.set_game_state("RED_WON")
                                                return True
                                        if self._board_space[piece_key_row][piece_key_column] == "RElephant":
                                            status = self.red_elephant_validate_move(piece_key, king_space)
                                            if status is True:
                                                self.set_game_state("RED_WON")
                                                return True
                                        if self._board_space[piece_key_row][piece_key_column] == "RHorse":
                                            status = self.red_horse_validate_move(piece_key, king_space)
                                            if status is True:
                                                self.set_game_state("RED_WON")
                                                return True
                                        if self._board_space[piece_key_row][piece_key_column] == "RGuard":
                                            status = self.red_guard_validate_move(piece_key, king_space)
                                            if status is True:
                                                self.set_game_state("RED_WON")
                                                return True
                                        if self._board_space[piece_key_row][piece_key_column] == "RGeneral":
                                            status = self.red_general_validate_move(piece_key, king_space)
                                            if status is True:
                                                self.set_game_state("RED_WON")
                                                return True

                                # if none of the above is true, then king can move to a space to not be in check
                                # which means checkmate status is False
                                return False

    def is_in_checkmate_red(self):
        """Method to check if the Red team has been checkmated. This method is called at the end of every turn, which
        means it is called at the end of the make_move method, after the is_in_check method is called. Method will
        return True if the player has been checkmated and False if the player is not."""

        for i in range(10):  # iterate through game board rows
            for j in range(9):  # iterate through game board columns
                if self._board_space[i][j] == "RGeneral":
                    red_general_coordinate = str(i) + str(j)  # find 2D array coordinate of red general

                    for algebraic_space, coordinate in self._board_dict.items():
                        if coordinate == red_general_coordinate:
                            red_general_space = algebraic_space  # find key space corresponding to red general

                    # list of coordinate spaces blue king could move to to get out of check
                    coordinate_list = [str(i)+str(j-1), str(i)+str(j+1), str(i-1)+str(j-1), str(i-1)+str(j),
                                       str(i-1)+str(j+1), str(i+1)+str(j-1), str(i+1)+str(j), str(i+1)+str(j+1)]

                    # list of board dictionary key spaces blue king could move to to get out of check
                    potential_king_space_key_list = []
                    for key, value in self._board_dict.items():
                        for coordinate in coordinate_list:
                            if value == coordinate in coordinate_list:
                                potential_king_space_key_list.append(key)

                                any_piece_key_list = []
                                for piece_key in self._board_dict:
                                    any_piece_key_list.append(piece_key)  # list of all piece locations
                                any_piece_key_list.remove(red_general_space)  # remove king location

                                for piece_key in any_piece_key_list:  # check if any piece can kill king
                                    board_space_piece = self._board_dict[piece_key]  # convert dict key to board coord
                                    piece_key_row = int(board_space_piece[0])  # convert dict key to board coord row
                                    piece_key_column = int(board_space_piece[1])  # convert dict key to coord column

                                    # check if any potential king space will cause check (again)
                                    for king_space in potential_king_space_key_list:
                                        if self._board_space[piece_key_row][piece_key_column] == "BSoldier":
                                            status = self.red_soldier_validate_move(piece_key, king_space)
                                            if status is True:  # if piece can kill king
                                                self.set_game_state("BLUE_WON")  # checkmate of red king, so blue wins
                                                return True
                                        if self._board_space[piece_key_row][piece_key_column] == "BCannon":
                                            status = self.red_cannon_validate_move(piece_key, king_space)
                                            if status is True:
                                                self.set_game_state("BLUE_WON")
                                                return True
                                        if self._board_space[piece_key_row][piece_key_column] == "BChariot":
                                            status = self.red_chariot_validate_move(piece_key, king_space)
                                            if status is True:
                                                self.set_game_state("BLUE_WON")
                                                return True
                                        if self._board_space[piece_key_row][piece_key_column] == "BElephant":
                                            status = self.red_elephant_validate_move(piece_key, king_space)
                                            if status is True:
                                                self.set_game_state("BLUE_WON")
                                                return True
                                        if self._board_space[piece_key_row][piece_key_column] == "BHorse":
                                            status = self.red_horse_validate_move(piece_key, king_space)
                                            if status is True:
                                                self.set_game_state("BLUE_WON")
                                                return True
                                        if self._board_space[piece_key_row][piece_key_column] == "BGuard":
                                            status = self.red_guard_validate_move(piece_key, king_space)
                                            if status is True:
                                                self.set_game_state("BLUE_WON")
                                                return True
                                        if self._board_space[piece_key_row][piece_key_column] == "BGeneral":
                                            status = self.red_general_validate_move(piece_key, king_space)
                                            if status is True:
                                                self.set_game_state("BLUE_WON")
                                                return True

                                # if none of the above is true, then king can move to a space to not be in check
                                # which means checkmate status is False
                                return False

    def make_move(self, from_location, to_location):
        """Method that is called to move pieces on the board. The two parameters represent the square from which to
        move the piece and the square to which the piece will be moved. If the square from_location does not contain a
        piece belonging to the player whose turn it is, the method will return False. False will also be returned if the
        proposed move is not legal or if the game has already been won. If the proposed move is valid, the indicated
        piece will be moved, any captured piece will be removed, the game state and turn will be updated and the
        function will return True. After identifying the piece that is being moved, this method relies on many helper
        functions to verify the board functionality of each piece."""

        if self.get_game_state() != "UNFINISHED":  # if the game has already been won
            return False

        if from_location not in self._board_dict:  # if from_location is not on the board
            return False

        if to_location not in self._board_dict:  # if to_location is not on the board
            return False

        board_space = self._board_dict[from_location]  # convert from_location to coordinate to identify piece
        row = int(board_space[0])
        column = int(board_space[1])

        piece = self._board_space[row][column]  # find piece based on from_location coordinate

        if self.get_turn()[0] != piece[0]:  # if the piece being moved does not belong to the player whose turn it is
            return False  # or if there is no piece at the specified space

        if from_location == to_location:  # player is passing their turn
            if self.get_turn() == "Red":
                self.set_turn("Blue")  # switch turn to other player
                return True
            if self.get_turn() == "Blue":
                self.set_turn("Red")  # switch turn to other player
                return True

        if "RChariot" in piece:  # if piece to be moved is red chariot

            move_status = self.red_chariot_validate_move(from_location, to_location)

            if move_status is True:  # if legal move can be made
                self.red_update_board("RChariot", from_location, to_location)  # update board in memory

                check_red_status = self.is_in_check("red")  # check if player whose turn it is put themselves in check

                if check_red_status is False:  # if legal move does not put player in check

                    check_blue_status = self.is_in_check("blue")  # check if other player was put in check

                    if check_blue_status is False:  # if other player was not put in check
                        return True  # board has been updated, as well as turn status. It is now other player's turn.

                    else:  # if other player was put in check
                        if self.is_in_checkmate_blue() is True:  # check if other player was put in checkmate
                            return True  # main purpose of this is to update game state if a player has won
                        else:
                            return True

                else:  # if legal move puts player in check
                    return self.red_reverse_board("RChariot", from_location, to_location)  # reverse board in memory
                    # return False and it is still the same player's turn

            else:  # if legal move cannot be made
                return False

        if "BChariot" in piece:  # if piece to be moved is blue chariot

            move_status = self.blue_chariot_validate_move(from_location, to_location)

            if move_status is True:  # if legal move can be made
                self.blue_update_board("BChariot", from_location, to_location)  # update board in memory

                check_blue_status = self.is_in_check("blue")  # check if player whose turn it is put themselves in check

                if check_blue_status is False:  # if legal move does not put player in check

                    check_red_status = self.is_in_check("red")  # check if other player was put in check

                    if check_red_status is False:  # if other player was not put in check
                        return True  # board has been updated, as well as turn status. It is now other player's turn.

                    else:  # if other player was put in check
                        if self.is_in_checkmate_red() is True:  # check if other player was put in checkmate
                            return True  # main purpose of this is to update game state if a player has won
                        else:
                            return True

                else:  # if legal move puts player in check
                    return self.blue_reverse_board("BChariot", from_location, to_location)  # reverse board in memory
                    # return False and it is still the same player's turn

            else:  # if legal move cannot be made
                return False

        if "RElephant" in piece:  # if piece to be moved is red elephant

            move_status = self.red_elephant_validate_move(from_location, to_location)

            if move_status is True:  # if legal move can be made
                self.red_update_board("RElephant", from_location, to_location)  # update board in memory

                check_red_status = self.is_in_check("red")  # check if player whose turn it is put themselves in check

                if check_red_status is False:  # if legal move does not put player in check

                    check_blue_status = self.is_in_check("blue")  # check if other player was put in check

                    if check_blue_status is False:  # if other player was not put in check
                        return True  # board has been updated, as well as turn status. It is now other player's turn.

                    else:  # if other player was put in check
                        if self.is_in_checkmate_blue() is True:  # check if other player was put in checkmate
                            return True  # main purpose of this is to update game state if a player has won
                        else:
                            return True

                else:  # if legal move puts player in check
                    return self.red_reverse_board("RElephant", from_location, to_location)  # reverse board in memory
                    # return False and it is still the same player's turn

            else:  # if legal move cannot be made
                return False

        if "BElephant" in piece:  # if piece to be moved is blue elephant

            move_status = self.blue_elephant_validate_move(from_location, to_location)

            if move_status is True:  # if legal move can be made
                self.blue_update_board("BElephant", from_location, to_location)  # update board in memory

                check_blue_status = self.is_in_check("blue")  # check if player whose turn it is put themselves in check

                if check_blue_status is False:  # if legal move does not put player in check

                    check_red_status = self.is_in_check("red")  # check if other player was put in check

                    if check_red_status is False:  # if other player was not put in check
                        return True  # board has been updated, as well as turn status. It is now other player's turn.

                    else:  # if other player was put in check
                        if self.is_in_checkmate_red() is True:  # check if other player was put in checkmate
                            return True  # main purpose of this is to update game state if a player has won
                        else:
                            return True

                else:  # if legal move puts player in check
                    return self.blue_reverse_board("BElephant", from_location, to_location)  # reverse board in memory
                    # return False and it is still the same player's turn

            else:  # if legal move cannot be made
                return False

        if "RHorse" in piece:  # if piece to be moved is red horse

            move_status = self.red_horse_validate_move(from_location, to_location)

            if move_status is True:  # if legal move can be made
                self.red_update_board("RHorse", from_location, to_location)  # update board in memory

                check_red_status = self.is_in_check("red")  # check if player whose turn it is put themselves in check

                if check_red_status is False:  # if legal move does not put player in check

                    check_blue_status = self.is_in_check("blue")  # check if other player was put in check

                    if check_blue_status is False:  # if other player was not put in check
                        return True  # board has been updated, as well as turn status. It is now other player's turn.

                    else:  # if other player was put in check
                        if self.is_in_checkmate_blue() is True:  # check if other player was put in checkmate
                            return True  # main purpose of this is to update game state if a player has won
                        else:
                            return True

                else:  # if legal move puts player in check
                    return self.red_reverse_board("RHorse", from_location, to_location)  # reverse board in memory
                    # return False and it is still the same player's turn

            else:  # if legal move cannot be made
                return False

        if "BHorse" in piece:  # if piece to be moved is blue horse

            move_status = self.blue_horse_validate_move(from_location, to_location)

            if move_status is True:  # if legal move can be made
                self.blue_update_board("BHorse", from_location, to_location)  # update board in memory

                check_blue_status = self.is_in_check("blue")  # check if player whose turn it is put themselves in check

                if check_blue_status is False:  # if legal move does not put player in check

                    check_red_status = self.is_in_check("red")  # check if other player was put in check

                    if check_red_status is False:  # if other player was not put in check
                        return True  # board has been updated, as well as turn status. It is now other player's turn.

                    else:  # if other player was put in check
                        if self.is_in_checkmate_red() is True:  # check if other player was put in checkmate
                            return True  # main purpose of this is to update game state if a player has won
                        else:
                            return True

                else:  # if legal move puts player in check
                    return self.blue_reverse_board("BHorse", from_location, to_location)  # reverse board in memory
                    # return False and it is still the same player's turn

            else:  # if legal move cannot be made
                return False

        if "RCannon" in piece:  # if piece to be moved is red cannon

            move_status = self.red_cannon_validate_move(from_location, to_location)

            if move_status is True:  # if legal move can be made
                self.red_update_board("RCannon", from_location, to_location)  # update board in memory

                check_red_status = self.is_in_check("red")  # check if player whose turn it is put themselves in check

                if check_red_status is False:  # if legal move does not put player in check

                    check_blue_status = self.is_in_check("blue")  # check if other player was put in check

                    if check_blue_status is False:  # if other player was not put in check
                        return True  # board has been updated, as well as turn status. It is now other player's turn.

                    else:  # if other player was put in check
                        if self.is_in_checkmate_blue() is True:  # check if other player was put in checkmate
                            return True  # main purpose of this is to update game state if a player has won
                        else:
                            return True

                else:  # if legal move puts player in check
                    return self.red_reverse_board("RCannon", from_location, to_location)  # reverse board in memory
                    # return False and it is still the same player's turn

            else:  # if legal move cannot be made
                return False

        if "BCannon" in piece:  # if piece to be moved is blue cannon

            move_status = self.blue_cannon_validate_move(from_location, to_location)

            if move_status is True:  # if legal move can be made
                self.blue_update_board("BCannon", from_location, to_location)  # update board in memory

                check_blue_status = self.is_in_check("blue")  # check if player whose turn it is put themselves in check

                if check_blue_status is False:  # if legal move does not put player in check

                    check_red_status = self.is_in_check("red")  # check if other player was put in check

                    if check_red_status is False:  # if other player was not put in check
                        return True  # board has been updated, as well as turn status. It is now other player's turn.

                    else:  # if other player was put in check
                        if self.is_in_checkmate_red() is True:  # check if other player was put in checkmate
                            return True  # main purpose of this is to update game state if a player has won
                        else:
                            return True

                else:  # if legal move puts player in check
                    return self.blue_reverse_board("BCannon", from_location, to_location)  # reverse board in memory
                    # return False and it is still the same player's turn

            else:  # if legal move cannot be made
                return False

        if "RGuard" in piece:  # if piece to be moved is red guard

            move_status = self.red_guard_validate_move(from_location, to_location)

            if move_status is True:  # if legal move can be made
                self.red_update_board("RGuard", from_location, to_location)  # update board in memory

                check_red_status = self.is_in_check("red")  # check if player whose turn it is put themselves in check

                if check_red_status is False:  # if legal move does not put player in check

                    check_blue_status = self.is_in_check("blue")  # check if other player was put in check

                    if check_blue_status is False:  # if other player was not put in check
                        return True  # board has been updated, as well as turn status. It is now other player's turn.

                    else:  # if other player was put in check
                        if self.is_in_checkmate_blue() is True:  # check if other player was put in checkmate
                            return True  # main purpose of this is to update game state if a player has won
                        else:
                            return True

                else:  # if legal move puts player in check
                    return self.red_reverse_board("RGuard", from_location, to_location)  # reverse board in memory
                    # return False and it is still the same player's turn

            else:  # if legal move cannot be made
                return False

        if "BGuard" in piece:  # if piece to be moved is blue guard

            move_status = self.blue_guard_validate_move(from_location, to_location)

            if move_status is True:  # if legal move can be made
                self.blue_update_board("BGuard", from_location, to_location)  # update board in memory

                check_blue_status = self.is_in_check("blue")  # check if player whose turn it is put themselves in check

                if check_blue_status is False:  # if legal move does not put player in check

                    check_red_status = self.is_in_check("red")  # check if other player was put in check

                    if check_red_status is False:  # if other player was not put in check
                        return True  # board has been updated, as well as turn status. It is now other player's turn.

                    else:  # if other player was put in check
                        if self.is_in_checkmate_red() is True:  # check if other player was put in checkmate
                            return True  # main purpose of this is to update game state if a player has won
                        else:
                            return True

                else:  # if legal move puts player in check
                    return self.blue_reverse_board("BGuard", from_location, to_location)  # reverse board in memory
                    # return False and it is still the same player's turn

            else:  # if legal move cannot be made
                return False

        if "RGeneral" in piece:  # if piece to be moved is red general

            move_status = self.red_general_validate_move(from_location, to_location)

            if move_status is True:  # if legal move can be made
                self.red_update_board("RGeneral", from_location, to_location)  # update board in memory

                check_red_status = self.is_in_check("red")  # check if player whose turn it is put themselves in check

                if check_red_status is False:  # if legal move does not put player in check

                    check_blue_status = self.is_in_check("blue")  # check if other player was put in check

                    if check_blue_status is False:  # if other player was not put in check
                        return True  # board has been updated, as well as turn status. It is now other player's turn.

                    else:  # if other player was put in check
                        if self.is_in_checkmate_blue() is True:  # check if other player was put in checkmate
                            return True  # main purpose of this is to update game state if a player has won
                        else:
                            return True

                else:  # if legal move puts player in check
                    return self.red_reverse_board("RGeneral", from_location, to_location)  # reverse board in memory
                    # return False and it is still the same player's turn

            else:  # if legal move cannot be made
                return False

        if "BGeneral" in piece:  # if piece to be moved is blue general

            move_status = self.blue_general_validate_move(from_location, to_location)

            if move_status is True:  # if legal move can be made
                self.blue_update_board("BGeneral", from_location, to_location)  # update board in memory

                check_blue_status = self.is_in_check("blue")  # check if player whose turn it is put themselves in check

                if check_blue_status is False:  # if legal move does not put player in check

                    check_red_status = self.is_in_check("red")  # check if other player was put in check

                    if check_red_status is False:  # if other player was not put in check
                        return True  # board has been updated, as well as turn status. It is now other player's turn.

                    else:  # if other player was put in check
                        if self.is_in_checkmate_red() is True:  # check if other player was put in checkmate
                            return True  # main purpose of this is to update game state if a player has won
                        else:
                            return True

                else:  # if legal move puts player in check
                    return self.blue_reverse_board("BGeneral", from_location, to_location)  # reverse board in memory
                    # return False and it is still the same player's turn

            else:  # if legal move cannot be made
                return False

        if "RSoldier" in piece:  # if piece to be moved is red soldier

            move_status = self.red_soldier_validate_move(from_location, to_location)

            if move_status is True:  # if legal move can be made
                self.red_update_board("RSoldier", from_location, to_location)  # update board in memory

                check_red_status = self.is_in_check("red")  # check if player whose turn it is put themselves in check

                if check_red_status is False:  # if legal move does not put player in check

                    check_blue_status = self.is_in_check("blue")  # check if other player was put in check

                    if check_blue_status is False:  # if other player was not put in check
                        return True  # board has been updated, as well as turn status. It is now other player's turn.

                    else:  # if other player was put in check
                        if self.is_in_checkmate_blue() is True:  # check if other player was put in checkmate
                            return True  # main purpose of this is to update game state if a player has won
                        else:
                            return True

                else:  # if legal move puts player in check
                    return self.red_reverse_board("RSoldier", from_location, to_location)  # reverse board in memory
                    # return False and it is still the same player's turn

            else:  # if legal move cannot be made
                return False

        if "BSoldier" in piece:  # if piece to be moved is blue soldier

            move_status = self.blue_soldier_validate_move(from_location, to_location)

            if move_status is True:  # if legal move can be made
                self.blue_update_board("BSoldier", from_location, to_location)  # update board in memory

                check_blue_status = self.is_in_check("blue")  # check if player whose turn it is put themselves in check

                if check_blue_status is False:  # if legal move does not put player in check

                    check_red_status = self.is_in_check("red")  # check if other player was put in check

                    if check_red_status is False:  # if other player was not put in check
                        return True  # board has been updated, as well as turn status. It is now other player's turn.

                    else:  # if other player was put in check
                        if self.is_in_checkmate_red() is True:  # check if other player was put in checkmate
                            return True  # main purpose of this is to update game state if a player has won
                        else:
                            return True

                else:  # if legal move puts player in check
                    return self.blue_reverse_board("BSoldier", from_location, to_location)  # reverse board in memory
                    # return False and it is still the same player's turn

            else:  # if legal move cannot be made
                return False

    def red_update_board(self, piece, from_location, to_location):
        """This method updates the board to reflect a move that has been made by team Red. It will move the parameter
        piece from and to the passed locations."""

        board_space_from = self._board_dict[from_location]  # convert from_location parameter to board_space coordinate
        from_row = int(board_space_from[0])
        from_column = int(board_space_from[1])

        board_space_to = self._board_dict[to_location]  # convert to_location parameter to board_space coordinate
        to_row = int(board_space_to[0])
        to_column = int(board_space_to[1])

        self._board_space[from_row][from_column] = " "  # make indicated move
        self._board_space[to_row][to_column] = piece  # replace captured piece
        self.set_turn("Blue")  # update turn

    def red_reverse_board(self, piece, from_location, to_location):
        """This method reverses the updated board to reflect the board's state prior to when a move was attempted by
        the Red team. The purpose of this method is to undo the board state after checking if a move would result in a
        check for the team making the move (which is considered an illegal move). After this method is executed, the
        board state is undone, it is still the same player's turn, and False is returned."""

        board_space_from = self._board_dict[from_location]  # convert from_location parameter to board_space coordinate
        from_row = int(board_space_from[0])
        from_column = int(board_space_from[1])

        board_space_to = self._board_dict[to_location]  # convert to_location parameter to board_space coordinate
        to_row = int(board_space_to[0])
        to_column = int(board_space_to[1])

        self._board_space[from_row][from_column] = piece  # reverse making the move
        self._board_space[to_row][to_column] = " "  # do not replace captured piece
        self.set_turn("Red")  # since player put themselves in check, it is still their turn
        return False

    def blue_update_board(self, piece, from_location, to_location):
        """This method updates the board to reflect a move that has been made by team Blue. It will move the parameter
        piece from and to the passed locations."""

        board_space_from = self._board_dict[from_location]  # convert from_location parameter to board_space coordinate
        from_row = int(board_space_from[0])
        from_column = int(board_space_from[1])

        board_space_to = self._board_dict[to_location]  # convert to_location parameter to board_space coordinate
        to_row = int(board_space_to[0])
        to_column = int(board_space_to[1])

        self._board_space[from_row][from_column] = " "  # make indicated move
        self._board_space[to_row][to_column] = piece  # replace captured piece
        self.set_turn("Red")  # update turn

    def blue_reverse_board(self, piece, from_location, to_location):
        """This method reverses the updated board to reflect the board's state prior to when a move was attempted by
        the Blue team. The purpose of this method is to undo the board state after checking if a move would result in a
        check for the team making the move (which is considered an illegal move). After this method is executed, the
        board state is undone, it is still the same player's turn, and False is returned."""

        board_space_from = self._board_dict[from_location]  # convert from_location parameter to board_space coordinate
        from_row = int(board_space_from[0])
        from_column = int(board_space_from[1])

        board_space_to = self._board_dict[to_location]  # convert to_location parameter to board_space coordinate
        to_row = int(board_space_to[0])
        to_column = int(board_space_to[1])

        self._board_space[from_row][from_column] = piece  # do not make move
        self._board_space[to_row][to_column] = " "  # do not replace captured piece
        self.set_turn("Blue")  # update turn to keep at current player
        return False

    def red_cannon_validate_move(self, from_location, to_location):
        """Checks if a proposed move is valid for a Red Cannon. A red cannon can move in a straight line sideways or
        forwards/backwards by jumping over an intervening piece. A cannon cannot capture another cannon and also cannot
        jump over another cannon. Cannons may operate along diagonal lines within the palace, which requires an
        intervening piece at the center of the palace."""

        red_fortress = ["d1", "e1", "f1", "d2", "e2", "f2", "d3", "e3", "f3"]
        blue_fortress = ["d8", "e8", "f8", "d9", "e9", "f9", "d10", "e10", "f10"]

        board_space_from = self._board_dict[from_location]  # convert from_location parameter to board_space coordinate
        from_row = int(board_space_from[0])
        from_column = int(board_space_from[1])

        board_space_to = self._board_dict[to_location]  # convert to_location parameter to board_space coordinate
        to_row = int(board_space_to[0])
        to_column = int(board_space_to[1])

        if "R" in str(self._board_space[to_row][to_column]):  # if moving to a space that contains own team's piece
            return False  # cannot capture own piece

        if from_row == to_row:
            if from_column != to_column:  # moving side to side in a row
                if to_column > from_column:  # moving to the right in a row
                    row = self._board_space[from_row]  # isolate row from board
                    row_segment = row[(from_column + 1):to_column]  # isolate portion containing spaces in cannon's path
                    count = 0  # initialize intervening piece count to 1
                    for space in row_segment:  # iterate through each space in cannon's path
                        if "Cannon" not in space:  # make sure intervening piece is not a cannon
                            if space != " ":  # if there is an intervening piece
                                count += 1  # add 1 to intervening piece count

                    if count == 1:  # intervening piece count must equal 1
                        if "Cannon" not in self._board_space[to_row][to_column]:  # must not try to capture other cannon
                            return True

                    return False

                if to_column < from_column:  # moving to the left in a row
                    row = self._board_space[from_row]  # isolate row from board
                    row_segment = row[(to_column + 1):from_column]  # isolate portion containing spaces in cannon's path
                    count = 0  # initialize intervening piece count to 1
                    for space in row_segment:  # iterate through each space in cannon's path
                        if "Cannon" not in space:  # make sure intervening piece is not a cannon
                            if space != " ":  # if there is an intervening piece
                                count += 1  # add 1 to intervening piece count

                    if count == 1:  # intervening piece count must equal 1
                        if "Cannon" not in self._board_space[to_row][to_column]:  # must not try to capture other cannon
                            return True
                    return False

        if from_column == to_column:
            if from_row != to_row:  # moving up and down
                if to_row > from_row:  # moving down in a column
                    # initialize a list of all spaces in the specified column
                    column = [self._board_space[0][from_column], self._board_space[1][from_column],
                              self._board_space[2][from_column], self._board_space[3][from_column],
                              self._board_space[4][from_column], self._board_space[5][from_column],
                              self._board_space[6][from_column], self._board_space[7][from_column],
                              self._board_space[8][from_column], self._board_space[9][
                                  from_column]]

                    column_segment = column[(from_row + 1):to_row]  # isolate portion containing spaces in cannon's path
                    count = 0  # initialize intervening piece count to 1
                    for space in column_segment:  # iterate through each space in cannon's path
                        if "Cannon" not in space:  # make sure intervening piece is not a cannon
                            if space != " ":  # if there is an intervening piece
                                count += 1  # add 1 to intervening piece count

                    if count == 1:  # intervening piece count must equal 1
                        if "Cannon" not in self._board_space[to_row][to_column]:  # must not try to capture other cannon
                            return True
                    return False

                if to_row < from_row:  # moving up in a column
                    # initialize a list of all spaces in the specified column
                    column = [self._board_space[0][from_column], self._board_space[1][from_column],
                              self._board_space[2][from_column], self._board_space[3][from_column],
                              self._board_space[4][from_column], self._board_space[5][from_column],
                              self._board_space[6][from_column], self._board_space[7][from_column],
                              self._board_space[8][from_column], self._board_space[9][
                                  from_column]]

                    column_segment = column[(to_row + 1):from_row]  # isolate portion containing spaces in cannon's path
                    count = 0  # initialize intervening piece count to 1
                    for space in column_segment:  # iterate through each space in cannon's path
                        if "Cannon" not in space:  # make sure intervening piece is not a cannon
                            if space != " ":  # if there is an intervening piece
                                count += 1  # add 1 to intervening piece count

                    if count == 1:  # intervening piece count must equal 1
                        if "Cannon" not in self._board_space[to_row][to_column]:  # must not try to capture other cannon
                            return True
                    return False

        if from_location in red_fortress:
            if to_location in red_fortress:  # if moving within red palace
                if from_location == "d1":
                    if to_location == "f3" and self._board_space[1][4] != " ":  # make sure E2 is obstructed
                        return True
                if from_location == "d3":
                    if to_location == "f1" and self._board_space[1][4] != " ":
                        return True
                if from_location == "f1":
                    if to_location == "d3" and self._board_space[1][4] != " ":
                        return True
                if from_location == "f3":
                    if to_location == "d1" and self._board_space[1][4] != " ":
                        return True

        if from_location in blue_fortress:
            if to_location in blue_fortress:  # if moving within blue palace
                if from_location == "d8":
                    if to_location == "f10" and self._board_space[8][4] != " ":  # make sure E9 is obstructed
                        return True
                if from_location == "d10":
                    if to_location == "f8" and self._board_space[8][4] != " ":
                        return True
                if from_location == "f8":
                    if to_location == "d10" and self._board_space[8][4] != " ":
                        return True
                if from_location == "f10":
                    if to_location == "d8" and self._board_space[8][4] != " ":
                        return True

        return False  # if no legal move was made

    def blue_cannon_validate_move(self, from_location, to_location):
        """Checks if a proposed move is valid for a Blue Cannon. A blue cannon can move in a straight line sideways or
        forwards/backwards by jumping over an intervening piece. A cannon cannot capture another cannon and also cannot
        jump over another cannon. Cannons may operate along diagonal lines within the palace, which requires an
        intervening piece at the center of the palace."""

        red_fortress = ["d1", "e1", "f1", "d2", "e2", "f2", "d3", "e3", "f3"]
        blue_fortress = ["d8", "e8", "f8", "d9", "e9", "f9", "d10", "e10", "f10"]

        board_space_from = self._board_dict[from_location]  # convert from_location parameter to board_space coordinate
        from_row = int(board_space_from[0])
        from_column = int(board_space_from[1])

        board_space_to = self._board_dict[to_location]  # convert to_location parameter to board_space coordinate
        to_row = int(board_space_to[0])
        to_column = int(board_space_to[1])

        if "B" in str(self._board_space[to_row][to_column]):  # if moving to a space that contains own team's piece
            return False  # cannot capture own piece

        if from_row == to_row:
            if from_column != to_column:  # moving side to side in a row
                if to_column > from_column:  # moving to the right in a row
                    row = self._board_space[from_row]  # isolate row from board
                    row_segment = row[(from_column + 1):to_column]  # isolate portion containing spaces in cannon's path
                    count = 0  # initialize intervening piece count to 1
                    for space in row_segment:  # iterate through each space in cannon's path
                        if "Cannon" not in space:  # make sure intervening piece is not a cannon
                            if space != " ":  # if there is an intervening piece
                                count += 1  # add 1 to intervening piece count

                    if count == 1:  # intervening piece count must equal 1
                        if "Cannon" not in self._board_space[to_row][to_column]:  # must not try to capture other cannon
                            return True
                    return False

                if to_column < from_column:  # moving to the left in a row
                    row = self._board_space[from_row]  # isolate row from board
                    row_segment = row[(to_column + 1):from_column]  # isolate portion containing spaces in cannon's path
                    count = 0  # initialize intervening piece count to 1
                    for space in row_segment:  # iterate through each space in cannon's path
                        if "Cannon" not in space:  # make sure intervening piece is not a cannon
                            if space != " ":  # if there is an intervening piece
                                count += 1  # add 1 to intervening piece count

                    if count == 1:  # intervening piece count must equal 1
                        if "Cannon" not in self._board_space[to_row][to_column]:  # must not try to capture other cannon
                            return True
                    return False

        if from_column == to_column:
            if from_row != to_row:  # moving up and down
                if to_row > from_row:  # moving down in a column
                    # initialize a list of all spaces in the specified column
                    column = [self._board_space[0][from_column], self._board_space[1][from_column],
                              self._board_space[2][from_column], self._board_space[3][from_column],
                              self._board_space[4][from_column], self._board_space[5][from_column],
                              self._board_space[6][from_column], self._board_space[7][from_column],
                              self._board_space[8][from_column], self._board_space[9][
                                  from_column]]

                    column_segment = column[(from_row + 1):to_row]  # isolate portion containing spaces in cannon's path
                    count = 0  # initialize intervening piece count to 1
                    for space in column_segment:  # iterate through each space in cannon's path
                        if "Cannon" not in space:  # make sure intervening piece is not a cannon
                            if space != " ":  # if there is an intervening piece
                                count += 1  # add 1 to intervening piece count

                    if count == 1:  # intervening piece count must equal 1
                        if "Cannon" not in self._board_space[to_row][to_column]:  # must not try to capture other cannon
                            return True
                    return False

                if to_row < from_row:  # moving up in a column
                    # initialize a list of all spaces in the specified column
                    column = [self._board_space[0][from_column], self._board_space[1][from_column],
                              self._board_space[2][from_column], self._board_space[3][from_column],
                              self._board_space[4][from_column], self._board_space[5][from_column],
                              self._board_space[6][from_column], self._board_space[7][from_column],
                              self._board_space[8][from_column], self._board_space[9][
                                  from_column]]

                    column_segment = column[(to_row + 1):from_row]  # isolate portion containing spaces in cannon's path
                    count = 0  # initialize intervening piece count to 1
                    for space in column_segment:  # iterate through each space in cannon's path
                        # print(column_segment)
                        if "Cannon" not in space:  # make sure intervening piece is not a cannon
                            if space != " ":  # if there is an intervening piece
                                count += 1  # add 1 to intervening piece count

                    if count == 1:  # intervening piece count must equal 1
                        if "Cannon" not in self._board_space[to_row][to_column]:  # must not try to capture other cannon
                            return True
                    return False

        if from_location in red_fortress:
            if to_location in red_fortress:  # if moving within red palace
                if from_location == "d1":
                    if to_location == "f3" and self._board_space[1][4] != " ":  # make sure E2 is obstructed
                        return True
                if from_location == "d3":
                    if to_location == "f1" and self._board_space[1][4] != " ":
                        return True
                if from_location == "f1":
                    if to_location == "d3" and self._board_space[1][4] != " ":
                        return True
                if from_location == "f3":
                    if to_location == "d1" and self._board_space[1][4] != " ":
                        return True

        if from_location in blue_fortress:
            if to_location in blue_fortress:  # if moving within blue palace
                if from_location == "d8":
                    if to_location == "f10" and self._board_space[8][4] != " ":  # make sure E9 is obstructed
                        return True
                if from_location == "d10":
                    if to_location == "f8" and self._board_space[8][4] != " ":
                        return True
                if from_location == "f8":
                    if to_location == "d10" and self._board_space[8][4] != " ":
                        return True
                if from_location == "f10":
                    if to_location == "d8" and self._board_space[8][4] != " ":
                        return True

        return False  # if no legal move was made

    def red_elephant_validate_move(self, from_location, to_location):
        """Checks if a proposed move is valid for a Red Elephant. A Red elephant may move one space forward then two
        spaces diagonally. Alternatively, an elephant can move one space sideways and then two spaces diagonally.
        Elephants can be blocked by another piece during their first movement (forward or sideways) and even during
        their second diagonal movement in the intermediate diagonal space. Elephants must not be blocked in order to
        fully execute a move."""

        board_space_from = self._board_dict[from_location]  # convert from_location parameter to board_space coordinate
        from_row = int(board_space_from[0])
        from_column = int(board_space_from[1])

        board_space_to = self._board_dict[to_location]  # convert to_location parameter to board_space coordinate
        to_row = int(board_space_to[0])
        to_column = int(board_space_to[1])

        if "R" in str(self._board_space[to_row][to_column]):  # if moving to a space that contains own team's piece
            return False  # cannot capture own piece

        if from_row + 3 == to_row:
            if from_column + 2 == to_column:
                if self._board_space[from_row + 1][from_column] == " ":  # first movement not blocked
                    if self._board_space[from_row + 2][from_column + 1] == " ":  # second movement not blocked
                        return True
            if from_column - 2 == to_column:
                if self._board_space[from_row + 1][from_column] == " ":
                    if self._board_space[from_row + 2][from_column - 1] == " ":
                        return True

        if from_row + 2 == to_row:
            if from_column + 3 == to_column:
                if self._board_space[from_row][from_column + 1] == " ":
                    if self._board_space[from_row + 1][from_column + 2] == " ":
                        return True
            if from_column - 3 == to_column:
                if self._board_space[from_row][from_column - 1] == " ":
                    if self._board_space[from_row + 1][from_column - 2] == " ":
                        return True

        if from_row - 2 == to_row:
            if from_column + 3 == to_column:
                if self._board_space[from_row][from_column + 1] == " ":
                    if self._board_space[from_row + 1][from_column + 2] == " ":
                        return True
            if from_column - 3 == to_column:
                if self._board_space[from_row][from_column - 1] == " ":
                    if self._board_space[from_row - 1][from_column - 2] == " ":
                        return True

        if from_row - 3 == to_row:
            if from_column + 2 == to_column:
                if self._board_space[from_row - 1][from_column] == " ":
                    if self._board_space[from_row - 2][from_column + 1] == " ":
                        return True
            if from_column - 2 == to_column:
                if self._board_space[from_row - 1][from_column] == " ":
                    if self._board_space[from_row - 2][from_column - 1] == " ":
                        return True

        return False  # if no legal move was made

    def blue_elephant_validate_move(self, from_location, to_location):
        """Checks if a proposed move is valid for a Blue Elephant. A Blue elephant may move one space forward then two
        spaces diagonally. Alternatively, an elephant can move one space sideways and then two spaces diagonally.
        Elephants can be blocked by another piece during their first movement (forward or sideways) and even during
        their second diagonal movement in the intermediate diagonal space. Elephants must not be blocked in order to
        fully execute a move."""

        board_space_from = self._board_dict[from_location]  # convert from_location parameter to board_space coordinate
        from_row = int(board_space_from[0])
        from_column = int(board_space_from[1])

        board_space_to = self._board_dict[to_location]  # convert to_location parameter to board_space coordinate
        to_row = int(board_space_to[0])
        to_column = int(board_space_to[1])

        if "B" in str(self._board_space[to_row][to_column]):  # if moving to a space that contains own team's piece
            return False  # cannot capture own piece

        if from_row + 3 == to_row:
            if from_column + 2 == to_column:
                if self._board_space[from_row + 1][from_column] == " ":  # first movement not blocked
                    if self._board_space[from_row + 2][from_column + 1] == " ":  # second movement not blocked
                        return True
            if from_column - 2 == to_column:
                if self._board_space[from_row + 1][from_column] == " ":
                    if self._board_space[from_row + 2][from_column - 1] == " ":
                        return True

        if from_row + 2 == to_row:
            if from_column + 3 == to_column:
                if self._board_space[from_row][from_column + 1] == " ":
                    if self._board_space[from_row + 1][from_column + 2] == " ":
                        return True
            if from_column - 3 == to_column:
                if self._board_space[from_row][from_column - 1] == " ":
                    if self._board_space[from_row + 1][from_column - 2] == " ":
                        return True

        if from_row - 2 == to_row:
            if from_column + 3 == to_column:
                if self._board_space[from_row][from_column + 1] == " ":
                    if self._board_space[from_row + 1][from_column + 2] == " ":
                        return True
            if from_column - 3 == to_column:
                if self._board_space[from_row][from_column - 1] == " ":
                    if self._board_space[from_row - 1][from_column - 2] == " ":
                        return True

        if from_row - 3 == to_row:
            if from_column + 2 == to_column:
                if self._board_space[from_row - 1][from_column] == " ":
                    if self._board_space[from_row - 2][from_column + 1] == " ":
                        return True
            if from_column - 2 == to_column:
                if self._board_space[from_row - 1][from_column] == " ":
                    if self._board_space[from_row - 2][from_column - 1] == " ":
                        return True

        return False  # if no legal move was made

    def red_horse_validate_move(self, from_location, to_location):
        """Checks if a proposed move is valid for a Red Horse.  A Red horse can move one space forward then one
        space diagonally. Alternatively, it can move one space sideways then one space diagonally. Horses can be
        blocked by another piece during their first movement (forward or sideways), which does not allow the move to
        be executed. Horses must not be blocked in order to fully execute a move."""

        board_space_from = self._board_dict[from_location]  # convert from_location parameter to board_space coordinate
        from_row = int(board_space_from[0])
        from_column = int(board_space_from[1])

        board_space_to = self._board_dict[to_location]  # convert to_location parameter to board_space coordinate
        to_row = int(board_space_to[0])
        to_column = int(board_space_to[1])

        if "R" in str(self._board_space[to_row][to_column]):  # if moving to a space that contains own team's piece
            return False  # cannot capture own piece

        if from_row + 2 == to_row:
            if from_column + 1 == to_column:
                if self._board_space[from_row + 1][from_column] == " ":  # not blocked
                    return True
            if from_column - 1 == to_column:
                if self._board_space[from_row + 1][from_column] == " ":
                    return True

        if from_row + 1 == to_row:
            if from_column + 2 == to_column:
                if self._board_space[from_row][from_column + 1] == " ":
                    return True
            if from_column - 2 == to_column:
                if self._board_space[from_row][from_column - 1] == " ":
                    return True

        if from_row - 1 == to_row:
            if from_column + 2 == to_column:
                if self._board_space[from_row][from_column + 1] == " ":
                    return True
            if from_column - 2 == to_column:
                if self._board_space[from_row][from_column - 1] == " ":
                    return True

        if from_row - 2 == to_row:
            if from_column + 1 == to_column:
                if self._board_space[from_row - 1][from_column] == " ":
                    return True
            if from_column - 1 == to_column:
                if self._board_space[from_row - 1][from_column] == " ":
                    return True

        return False  # if legal move was not made

    def blue_horse_validate_move(self, from_location, to_location):
        """Checks if a proposed move is valid for a Blue Horse.  A Blue horse can move one space forward then one
        space diagonally. Alternatively, it can move one space sideways then one space diagonally. Horses can be
        blocked by another piece during their first movement (forward or sideways), which does not allow the move to
        be executed. Horses must not be blocked in order to fully execute a move."""

        board_space_from = self._board_dict[from_location]  # convert from_location parameter to board_space coordinate
        from_row = int(board_space_from[0])
        from_column = int(board_space_from[1])

        board_space_to = self._board_dict[to_location]  # convert to_location parameter to board_space coordinate
        to_row = int(board_space_to[0])
        to_column = int(board_space_to[1])

        if "B" in str(self._board_space[to_row][to_column]):  # if moving to a space that contains own team's piece
            return False  # cannot capture own piece

        if from_row + 2 == to_row:
            if from_column + 1 == to_column:
                if self._board_space[from_row + 1][from_column] == " ":  # not blocked
                    return True
            if from_column - 1 == to_column:
                if self._board_space[from_row + 1][from_column] == " ":
                    return True

        if from_row + 1 == to_row:
            if from_column + 2 == to_column:
                if self._board_space[from_row][from_column + 1] == " ":
                    return True
            if from_column - 2 == to_column:
                if self._board_space[from_row][from_column - 1] == " ":
                    return True

        if from_row - 1 == to_row:
            if from_column + 2 == to_column:
                if self._board_space[from_row][from_column + 1] == " ":
                    return True
            if from_column - 2 == to_column:
                if self._board_space[from_row][from_column - 1] == " ":
                    return True

        if from_row - 2 == to_row:
            if from_column + 1 == to_column:
                if self._board_space[from_row - 1][from_column] == " ":
                    return True
            if from_column - 1 == to_column:
                if self._board_space[from_row - 1][from_column] == " ":
                    return True

        return False  # if no legal move was made

    def red_chariot_validate_move(self, from_location, to_location):
        """Checks if a proposed move is valid for a Red Chariot.  A Red chariot can move an unlimited number of
        spaces in a straight line, vertically or horizontally.  If the chariot is in a palace, it can move along the
        designated diagonal lines within the palace."""

        red_fortress = ["d1", "e1", "f1", "d2", "e2", "f2", "d3", "e3", "f3"]
        blue_fortress = ["d8", "e8", "f8", "d9", "e9", "f9", "d10", "e10", "f10"]

        board_space_from = self._board_dict[from_location]  # convert from_location parameter to board_space coordinate
        from_row = int(board_space_from[0])
        from_column = int(board_space_from[1])

        board_space_to = self._board_dict[to_location]  # convert to_location parameter to board_space coordinate
        to_row = int(board_space_to[0])
        to_column = int(board_space_to[1])

        if "R" in str(self._board_space[to_row][to_column]):  # if moving to a space that contains own team's piece
            return False  # cannot capture own piece

        if from_row == to_row:
            if from_column != to_column:  # moving side to side in a row
                if to_column > from_column:  # moving to the right in a row
                    row = self._board_space[from_row]  # isolate row from board
                    row_segment = row[(from_column + 1):to_column]  # isolate portion with spaces in chariot's path
                    count = 0
                    for space in row_segment:  # iterate through each space in chariot's path
                        if space == " ":  # if there is no intervening piece
                            count += 1

                    if count == len(row_segment):  # if every single space is clear
                        return True
                    return False

                if to_column < from_column:  # moving to the left in a row
                    row = self._board_space[from_row]  # isolate row from board
                    row_segment = row[(to_column + 1):from_column]  # isolate portion with spaces in chariot's path
                    count = 0
                    for space in row_segment:  # iterate through each space in chariot's path
                        if space == " ":  # if there is no intervening piece
                            count += 1

                    if count == len(row_segment):  # if every single space is clear
                        return True
                    return False

        if from_column == to_column:
            if from_row != to_row:  # moving up and down
                if to_row > from_row:  # moving down in a column
                    # initialize a list of all spaces in the specified column
                    column = [self._board_space[0][from_column], self._board_space[1][from_column],
                              self._board_space[2][from_column], self._board_space[3][from_column],
                              self._board_space[4][from_column], self._board_space[5][from_column],
                              self._board_space[6][from_column], self._board_space[7][from_column],
                              self._board_space[8][from_column], self._board_space[9][
                                  from_column]]

                    column_segment = column[(from_row + 1):to_row]  # isolate portion with spaces in chariot's path
                    count = 0
                    for space in column_segment:  # iterate through each space in chariot's path
                        if space == " ":  # if there is no intervening piece
                            count += 1

                    if count == len(column_segment):  # if every single space is clear
                        return True
                    return False

                if to_row < from_row:  # moving up in a column
                    # initialize a list of all spaces in the specified column
                    column = [self._board_space[0][from_column], self._board_space[1][from_column],
                              self._board_space[2][from_column], self._board_space[3][from_column],
                              self._board_space[4][from_column], self._board_space[5][from_column],
                              self._board_space[6][from_column], self._board_space[7][from_column],
                              self._board_space[8][from_column], self._board_space[9][
                                  from_column]]

                    column_segment = column[(to_row + 1):from_row]  # isolate portion with spaces in chariot's path
                    count = 0
                    for space in column_segment:  # iterate through each space in chariot's path
                        if space == " ":  # if there is no intervening piece
                            count += 1

                    if count == len(column_segment):  # if every single space is clear
                        return True
                    return False

        if from_location in red_fortress:
            if to_location in red_fortress:  # if moving within red palace
                if from_location == "e2":
                    if to_location == "d1" or to_location == "d3" or to_location == "f1" or to_location == "f3":
                        return True
                if from_location == "d1":
                    if to_location == "e2":
                        return True
                    if to_location == "f3" and self._board_space[1][4] == " ":  # make sure E2 is unobstructed
                        return True
                if from_location == "d3":
                    if to_location == "e2":
                        return True
                    if to_location == "f1" and self._board_space[1][4] == " ":
                        return True
                if from_location == "f1":
                    if to_location == "e2":
                        return True
                    if to_location == "d3" and self._board_space[1][4] == " ":
                        return True
                if from_location == "f3":
                    if to_location == "e2":
                        return True
                    if to_location == "d1" and self._board_space[1][4] == " ":
                        return True

        if from_location in blue_fortress:
            if to_location in blue_fortress:  # if moving within blue palace
                if from_location == "e9":
                    if to_location == "d8" or to_location == "d10" or to_location == "f8" or to_location == "f10":
                        return True
                if from_location == "d8":
                    if to_location == "e9":
                        return True
                    if to_location == "f10" and self._board_space[8][4] == " ":  # make sure E9 is unobstructed
                        return True
                if from_location == "d10":
                    if to_location == "e9":
                        return True
                    if to_location == "f8" and self._board_space[8][4] == " ":
                        return True
                if from_location == "f8":
                    if to_location == "e9":
                        return True
                    if to_location == "d10" and self._board_space[8][4] == " ":
                        return True
                if from_location == "f10":
                    if to_location == "e9":
                        return True
                    if to_location == "d8" and self._board_space[8][4] == " ":
                        return True

        return False  # if no legal move was made

    def blue_chariot_validate_move(self, from_location, to_location):
        """Checks if a proposed move is valid for a Blue Chariot.  A Blue chariot can move an unlimited number of
        spaces in a straight line, vertically or horizontally.  If the chariot is in a palace, it can move along the
        designated diagonal lines within the palace."""

        red_fortress = ["d1", "e1", "f1", "d2", "e2", "f2", "d3", "e3", "f3"]
        blue_fortress = ["d8", "e8", "f8", "d9", "e9", "f9", "d10", "e10", "f10"]

        board_space_from = self._board_dict[from_location]  # convert from_location parameter to board_space coordinate
        from_row = int(board_space_from[0])
        from_column = int(board_space_from[1])

        board_space_to = self._board_dict[to_location]  # convert to_location parameter to board_space coordinate
        to_row = int(board_space_to[0])
        to_column = int(board_space_to[1])

        if "B" in str(self._board_space[to_row][to_column]):  # if moving to a space that contains own team's piece
            return False  # cannot capture own piece

        if from_row == to_row:
            if from_column != to_column:  # moving side to side in a row
                if to_column > from_column:  # moving to the right in a row
                    row = self._board_space[from_row]  # isolate row from board
                    row_segment = row[(from_column + 1):to_column]  # isolate portion with spaces in chariot's path
                    count = 0
                    for space in row_segment:  # iterate through each space in chariot's path
                        if space == " ":  # if there is no intervening piece
                            count += 1

                    if count == len(row_segment):  # if every single space is clear
                        return True
                    return False

                if to_column < from_column:  # moving to the left in a row
                    row = self._board_space[from_row]  # isolate row from board
                    row_segment = row[(to_column + 1):from_column]  # isolate portion with spaces in chariot's path
                    count = 0
                    for space in row_segment:  # iterate through each space in chariot's path
                        if space == " ":  # if there is no intervening piece
                            count += 1

                    if count == len(row_segment):  # if every single space is clear
                        return True
                    return False

        if from_column == to_column:
            if from_row != to_row:  # moving up and down
                if to_row > from_row:  # moving down in a column
                    # initialize a list of all spaces in the specified column
                    column = [self._board_space[0][from_column], self._board_space[1][from_column],
                              self._board_space[2][from_column], self._board_space[3][from_column],
                              self._board_space[4][from_column], self._board_space[5][from_column],
                              self._board_space[6][from_column], self._board_space[7][from_column],
                              self._board_space[8][from_column], self._board_space[9][
                                  from_column]]

                    column_segment = column[(from_row + 1):to_row]  # isolate portion with spaces in chariot's path
                    count = 0
                    for space in column_segment:  # iterate through each space in chariot's path
                        if space == " ":  # if there is no intervening piece
                            count += 1

                    if count == len(column_segment):  # if every single space is clear
                        return True
                    return False

                if to_row < from_row:  # moving up in a column
                    # initialize a list of all spaces in the specified column
                    column = [self._board_space[0][from_column], self._board_space[1][from_column],
                              self._board_space[2][from_column], self._board_space[3][from_column],
                              self._board_space[4][from_column], self._board_space[5][from_column],
                              self._board_space[6][from_column], self._board_space[7][from_column],
                              self._board_space[8][from_column], self._board_space[9][
                                  from_column]]

                    column_segment = column[(to_row + 1):from_row]  # isolate portion with spaces in chariot's path
                    count = 0
                    for space in column_segment:  # iterate through each space in chariot's path
                        if space == " ":  # if there is no intervening piece
                            count += 1

                    if count == len(column_segment):  # if every single space is clear
                        return True
                    return False

        if from_location in red_fortress:
            if to_location in red_fortress:  # if moving within red palace
                if from_location == "e2":
                    if to_location == "d1" or to_location == "d3" or to_location == "f1" or to_location == "f3":
                        return True
                if from_location == "d1":
                    if to_location == "e2":
                        return True
                    if to_location == "f3" and self._board_space[1][4] == " ":  # make sure E2 is unobstructed
                        return True
                if from_location == "d3":
                    if to_location == "e2":
                        return True
                    if to_location == "f1" and self._board_space[1][4] == " ":
                        return True
                if from_location == "f1":
                    if to_location == "e2":
                        return True
                    if to_location == "d3" and self._board_space[1][4] == " ":
                        return True
                if from_location == "f3":
                    if to_location == "e2":
                        return True
                    if to_location == "d1" and self._board_space[1][4] == " ":
                        return True

        if from_location in blue_fortress:
            if to_location in blue_fortress:  # if moving within blue palace
                if from_location == "e9":
                    if to_location == "d8" or to_location == "d10" or to_location == "f8" or to_location == "f10":
                        return True
                if from_location == "d8":
                    if to_location == "e9":
                        return True
                    if to_location == "f10" and self._board_space[8][4] == " ":  # make sure E9 is unobstructed
                        return True
                if from_location == "d10":
                    if to_location == "e9":
                        return True
                    if to_location == "f8" and self._board_space[8][4] == " ":
                        return True
                if from_location == "f8":
                    if to_location == "e9":
                        return True
                    if to_location == "d10" and self._board_space[8][4] == " ":
                        return True
                if from_location == "f10":
                    if to_location == "e9":
                        return True
                    if to_location == "d8" and self._board_space[8][4] == " ":
                        return True

        return False  # if no legal move was made

    def red_guard_validate_move(self, from_location, to_location):
        """Checks if a proposed move is valid for a Red Guard. A Red guard may never leave the palace. He can move one
        space in any direction (including along designated diagonal spaces) within the palace."""

        red_fortress = ["d1", "e1", "f1", "d2", "e2", "f2", "d3", "e3", "f3"]  # red palace board spaces
        red_diagonal = ["d1", "d3", "e2", "f1", "f3"]  # red palace diagonal access spaces

        if from_location not in red_fortress:  # guard is not in palace (illegal move)
            return False

        if to_location not in red_fortress:  # guard is trying to leave palace (illegal move)
            return False

        board_space_from = self._board_dict[from_location]  # convert from_location parameter to board_space coordinate
        from_row = int(board_space_from[0])
        from_column = int(board_space_from[1])

        board_space_to = self._board_dict[to_location]  # convert to_location parameter to board_space coordinate
        to_row = int(board_space_to[0])
        to_column = int(board_space_to[1])

        if "R" in str(self._board_space[to_row][to_column]):  # if moving to a space that contains own team's piece
            return False  # cannot capture own piece

        if from_row == to_row:
            if from_column + 1 == to_column:  # moving one space to the right
                return True
            if from_column - 1 == to_column:  # moving one space to the left
                return True

        if from_column == to_column:
            if from_row + 1 == to_row:  # moving one space forward
                return True
            if from_row - 1 == to_row:  # moving one space backward
                return True

        if from_column + 1 == to_column:
            if from_row + 1 == to_row:  # moving diagonally right and forward
                if to_location in red_diagonal:  # accounting for a diagonal space
                    return True
            if from_row - 1 == to_row:  # moving diagonally right and backward
                if to_location in red_diagonal:  # accounting for a diagonal space
                    return True

        if from_column - 1 == to_column:
            if from_row + 1 == to_row:  # moving diagonally left and forward
                if to_location in red_diagonal:  # accounting for a diagonal space
                    return True
            if from_row - 1 == to_row:  # moving diagonally left and backward
                if to_location in red_diagonal:  # accounting for a diagonal space
                    return True

        return False  # if no legal move was made

    def blue_guard_validate_move(self, from_location, to_location):
        """Checks if a proposed move is valid for a Blue Guard. A Blue guard may never leave the palace. He can move one
        space in any direction (including along designated diagonal spaces) within the palace."""

        blue_fortress = ["d8", "e8", "f8", "d9", "e9", "f9", "d10", "e10", "f10"]  # blue palace board spaces
        blue_diagonal = ["d8", "d10", "e9", "f8", "f10"]  # blue palace diagonal access spaces

        if from_location not in blue_fortress:  # guard is not in palace (illegal move)
            return False

        if to_location not in blue_fortress:  # guard is trying to leave palace (illegal move)
            return False

        board_space_from = self._board_dict[from_location]  # convert from_location parameter to board_space coordinate
        from_row = int(board_space_from[0])
        from_column = int(board_space_from[1])

        board_space_to = self._board_dict[to_location]  # convert to_location parameter to board_space coordinate
        to_row = int(board_space_to[0])
        to_column = int(board_space_to[1])

        if "B" in str(self._board_space[to_row][to_column]):  # if moving to a space that contains own piece
            return False  # cannot capture own piece

        if from_row == to_row:
            if from_column + 1 == to_column:  # moving one space to the right
                return True
            if from_column - 1 == to_column:  # moving one space to the left
                return True

        if from_column == to_column:
            if from_row + 1 == to_row:  # moving one space backward
                return True
            if from_row - 1 == to_row:  # moving one space forward
                return True

        if from_column + 1 == to_column:
            if from_row + 1 == to_row:  # moving diagonally right and backward
                if to_location in blue_diagonal:  # accounting for a diagonal space
                    return True
            if from_row - 1 == to_row:  # moving diagonally right and forward
                if to_location in blue_diagonal:  # accounting for a diagonal space
                    return True

        if from_column - 1 == to_column:
            if from_row + 1 == to_row:  # moving diagonally left and backward
                if to_location in blue_diagonal:  # accounting for a diagonal space
                    return True
            if from_row - 1 == to_row:  # moving diagonally left and forward
                if to_location in blue_diagonal:  # accounting for a diagonal space
                    return True

        return False  # if no legal move was made

    def red_general_validate_move(self, from_location, to_location):
        """Checks if the proposed move is valid for a Red General. A Red general is never allowed to leave his palace.
        He can only move one space forward, backward, or sideways within the palace. He may also move one space along
        designated diagonal lines in the palace."""

        red_fortress = ["d1", "e1", "f1", "d2", "e2", "f2", "d3", "e3", "f3"]  # red palace board spaces
        red_diagonal = ["d1", "d3", "e2", "f1", "f3"]  # red palace diagonal access spaces

        if from_location not in red_fortress:  # general is not in palace (illegal move)
            return False

        if to_location not in red_fortress:  # general is trying to leave palace (illegal move)
            return False

        board_space_from = self._board_dict[from_location]  # convert from_location parameter to board_space coordinate
        from_row = int(board_space_from[0])
        from_column = int(board_space_from[1])

        board_space_to = self._board_dict[to_location]  # convert to_location parameter to board_space coordinate
        to_row = int(board_space_to[0])
        to_column = int(board_space_to[1])

        if "R" in str(self._board_space[to_row][to_column]):  # if moving to a space that contains own team's piece
            return False  # cannot capture own piece

        if from_row == to_row:
            if from_column + 1 == to_column:  # moving one space to the right
                return True
            if from_column - 1 == to_column:  # moving one space to the left
                return True

        if from_column == to_column:
            if from_row + 1 == to_row:  # moving one space forward
                return True
            if from_row - 1 == to_row:  # moving one space backward
                return True

        if from_column + 1 == to_column:
            if from_row + 1 == to_row:  # moving diagonally right and forward
                if to_location in red_diagonal:  # accounting for a diagonal space
                    return True
            if from_row - 1 == to_row:  # moving diagonally right and backward
                if to_location in red_diagonal:  # accounting for a diagonal space
                    return True

        if from_column - 1 == to_column:
            if from_row + 1 == to_row:  # moving diagonally left and forward
                if to_location in red_diagonal:  # accounting for a diagonal space
                    return True

            if from_row - 1 == to_row:  # moving diagonally left and backward
                if to_location in red_diagonal:  # accounting for a diagonal space
                    return True

        return False  # if no legal move was made

    def blue_general_validate_move(self, from_location, to_location):
        """Checks if the proposed move is valid for a Blue General. A Blue general is never allowed to leave his palace.
        He can only move one space forward, backward, or sideways within the palace. He may also move one space along
        designated diagonal lines in the palace."""

        blue_fortress = ["d8", "e8", "f8", "d9", "e9", "f9", "d10", "e10", "f10"]  # blue palace board spaces
        blue_diagonal = ["d8", "d10", "e9", "f8", "f10"]  # blue palace diagonal access spaces

        if from_location not in blue_fortress:  # general is not in palace (illegal move)
            return False

        if to_location not in blue_fortress:  # general is trying to leave palace (illegal move)
            return False

        board_space_from = self._board_dict[from_location]  # convert from_location parameter to board_space coordinate
        from_row = int(board_space_from[0])
        from_column = int(board_space_from[1])

        board_space_to = self._board_dict[to_location]  # convert to_location parameter to board_space coordinate
        to_row = int(board_space_to[0])
        to_column = int(board_space_to[1])

        if "B" in str(self._board_space[to_row][to_column]):  # if moving to a space that contains own piece
            return False  # cannot capture own piece

        if from_row == to_row:
            if from_column + 1 == to_column:  # moving one space to the right
                return True
            if from_column - 1 == to_column:  # moving one space to the left
                return True

        if from_column == to_column:
            if from_row + 1 == to_row:  # moving one space backward
                return True
            if from_row - 1 == to_row:  # moving one space forward
                return True

        if from_column + 1 == to_column:
            if from_row + 1 == to_row:  # moving diagonally right and backward
                if to_location in blue_diagonal:  # accounting for a diagonal space
                    return True
            if from_row - 1 == to_row:  # moving diagonally right and forward
                if to_location in blue_diagonal:  # accounting for a diagonal space
                    return True

        if from_column - 1 == to_column:
            if from_row + 1 == to_row:  # moving diagonally left and backward
                if to_location in blue_diagonal:  # accounting for a diagonal space
                    return True
            if from_row - 1 == to_row:  # moving diagonally left and forward
                if to_location in blue_diagonal:  # accounting for a diagonal space
                    return True

        return False  # if no legal move was made

    def red_soldier_validate_move(self, from_location, to_location):
        """Checks if the proposed move is valid for a Red Soldier. A Red soldier can move one space forward or one
        space sideways. A soldier can never move backward. Once in the enemy team's palace, the soldier may move along
        designated diagonal lines."""

        blue_diagonal = ["d8", "d10", "e9", "f8", "f10"]  # blue palace diagonal access spaces

        board_space_from = self._board_dict[from_location]  # convert from_location parameter to board_space coordinate
        from_row = int(board_space_from[0])
        from_column = int(board_space_from[1])

        board_space_to = self._board_dict[to_location]  # convert to_location parameter to board_space coordinate
        to_row = int(board_space_to[0])
        to_column = int(board_space_to[1])

        if "R" in str(self._board_space[to_row][to_column]):  # if moving to a space that contains own piece
            return False  # cannot capture own piece

        if from_row + 1 == to_row:
            if from_column == to_column:  # moving one space forwards
                return True

        if from_row == to_row:
            if from_column - 1 == to_column:  # moving one space left
                return True
            if from_column + 1 == to_column:  # moving one space right
                return True

        if from_column + 1 == to_column:
            if from_row + 1 == to_row:  # moving diagonally right and forward
                if to_location in blue_diagonal:  # only allowed when in blue palace
                    return True

        if from_column - 1 == to_column:
            if from_row + 1 == to_row:  # moving diagonally left and forward
                if to_location in blue_diagonal:  # only allowed when in blue palace
                    return True

        return False  # if no legal move was made

    def blue_soldier_validate_move(self, from_location, to_location):
        """Checks if the proposed move is valid for a Blue Soldier. A Blue soldier can move one space forward or one
        space sideways. A soldier can never move backward. Once in the enemy team's palace, the soldier may move along
        designated diagonal lines."""

        red_diagonal = ["d1", "d3", "e2", "f1", "f3"]  # red palace diagonal access spaces

        board_space_from = self._board_dict[from_location]  # convert from_location parameter to board_space coordinate
        from_row = int(board_space_from[0])
        from_column = int(board_space_from[1])

        board_space_to = self._board_dict[to_location]  # convert to_location parameter to board_space coordinate
        to_row = int(board_space_to[0])
        to_column = int(board_space_to[1])

        if "B" in str(self._board_space[to_row][to_column]):  # if moving to a space that contains own piece
            return False  # cannot capture own piece

        if from_row - 1 == to_row:
            if from_column == to_column:  # moving one space forward
                return True

        if from_row == to_row:
            if from_column - 1 == to_column:  # moving one space left
                return True
            if from_column + 1 == to_column:  # moving one space right
                return True

        if from_column + 1 == to_column:
            if from_row - 1 == to_row:  # moving diagonally right and forward
                if to_location in red_diagonal:  # only allowed when in red palace
                    return True

        if from_column - 1 == to_column:
            if from_row - 1 == to_row:  # moving diagonally left and forward
                if to_location in red_diagonal:  # only allowed when in red palace
                    return True

        return False  # if no legal move was made

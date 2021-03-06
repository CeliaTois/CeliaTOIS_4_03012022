from views.ErrorHandlerView import ErrorHandlerView


class MenuView:
    """MainMenu class"""

    @staticmethod
    def display_main_menu():
        """
        display_main_menu()
        Display the main menu options and an input.
        :rtype: str
        :return: user choice
        """
        print("Menu")
        print("1: Add a player")
        print("2: Create a tournament")
        print("3: Load a tournament")
        print("4: Modify the ranking")
        print("5: Reports")
        while True:
            user_choice = input("Your choice? ")
            if user_choice <= "5":
                return user_choice
            ErrorHandlerView.display_error("Wrong option entered.")

    @staticmethod
    def display_tournament_menu():
        """
        display_tournament_menu()
        Display the tournament menu options and an input.
        :rtype: str
        :return: user choice
        """
        print("Load a tournament:")
        print("1: Launch a round")
        print("2: End a round")
        print("q: Return to the main menu")
        while True:
            user_choice = input("Your choice? ")
            if user_choice <= "2" or user_choice == "q":
                return user_choice
            ErrorHandlerView.display_error("Wrong option entered.")

    @staticmethod
    def display_players(players_to_display):
        """
        display_players()
        Display the players and an input.
        :arg: list of players to display
        :rtype: str
        :return: selected player
        """
        for player in players_to_display:
            print(player)
        while True:
            players_input = input("Player: ")
            for player in players_to_display:
                if players_input == str(player.id):
                    return player
            ErrorHandlerView.display_error("Wrong option entered.")

    @staticmethod
    def modify_ranking(players_to_display):
        """
        modify_ranking()
        Display the selected player name and an input to modify his ranking.
        :arg: list of players to display
        """
        if len(players_to_display) > 0:
            player_selected = MenuView.display_players(players_to_display)
            new_ranking = ErrorHandlerView.is_an_int(f"Enter {player_selected.first_name} "
                                                     f"{player_selected.last_name} ranking: ")
            for player in players_to_display:
                if player_selected.id == player.id:
                    player.ranking = int(new_ranking)
                player.update()
        else:
            ErrorHandlerView.display_error("No players have been created. Please, create at least 1 player.")

import player


class PlayersManager:
    def __init__(self, player_list):
        self.player_list = player_list

    def number_alive(self):
        count = 0
        for player in self.player_list:
            if player.lives > 0:
                count += 1
        return count

    def level_up(self):
        for player in self.player_list:
            player.level_up()

    def update_players(self):
        for player in self.player_list:
            player.update()

    def update_players_key(self, pressed_keys):
        for player in self.player_list:
            player.update_key(pressed_keys)

    def draw_players(self, surface):
        for player in self.player_list:
            player.draw(surface);

    def reset_players(self):
        for player in self.player_list:
            player.reset()

    def decrease_live(self, player_list):
        for player in player_list:
            player.lives -= 1
            if player.lives == 0:
                self.player_list.remove(player)

    def is_winner(self):
        return self.get_winner()

    def get_winner(self):
        winner = None
        for player in self.player_list:
            if player.is_alive() and winner == None:
                winner = player
            elif player.is_alive() and winner:
                return None;
        return winner
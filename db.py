import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchmany(1)
            return bool(len(result))

    def add_user(self, user_id, user_full_name):
        with self.connection:
            self.cursor.execute("INSERT INTO users (user_id, user_full_name) VALUES (?, ?)", (user_id, user_full_name,))

    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE users SET active = ? WHERE user_id = ?", (active, user_id,))

    def get_user(self):
        with self.connection:
            return self.cursor.execute("SELECT `user_id`, `active`, `user_full_name`, `game_rating` FROM `users`").fetchall()

    def remove_all_users(self):
        with self.connection:
            return self.connection.execute("DELETE FROM users;")

    def get_game_rating(self, user_id):
        with self.connection:
            return self.connection.execute("SELECT game_rating FROM users WHERE user_id = ? ", (user_id,)).fetchone()[0]

    def set_game_rating(self, user_id, game_rating):
        with self.connection:
            return self.cursor.execute("UPDATE users SET game_rating = ? WHERE user_id = ?", (game_rating, user_id,))

    def set_default_game_rating(self):
        default = 0
        with self.connection:
            return self.connection.execute("UPDATE users SET game_rating = ?", (default,))
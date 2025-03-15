# ЧАСТИНА 1: Клас Зброя
class Weapon:
    def __init__(self, name, hit_percentage):
        self.name = name
        self.hit_percentage = hit_percentage

    def __str__(self):
        return f"{self.name} - {self.hit_percentage}%"

    def __add__(self, value):
        self.hit_percentage += value
        return self

    def short_name(self):
        return self.name[:3] + '.'

# ЧАСТИНА 2: Клас Стрільба (наслідується від Зброя)
class Shooting(Weapon):
    def __init__(self, name, hit_percentage, shot_count):
        super().__init__(name, hit_percentage)
        self.shot_count = shot_count

    def hit_probability(self):
        return (self.hit_percentage / 100) * self.shot_count

    def __lt__(self, other):
        return self.shot_count < other.shot_count


# ЧАСТИНА 3: Клас Стрільби (список стрільб)
class Shooting:
    def __init__(self):
        self.shoot_list = []

    def add_shoot(self, shoot):
        self.shoot_list.append(shoot)

    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    data = line.strip().split(',')
                    if len(data) == 3:
                        self.add_shoot(ShootingAttempt(data[0], float(data[1]), int(data[2])))
            print("File loaded successfully!")
        except FileNotFoundError:
            print("File not found :(")

    def display_shootings(self):
        for shoot in sorted(self.shoot_list, key=lambda x: x.shots_count, reverse=True):
            print(shoot)

    def effective_shootings(self):
        return len([s for s in self.shoot_list if (s.hit_probability() / s.shots_count) > 0.5])

if __name__ == "__main__":
    weapon = Weapon("Rifle", 60)
    print(weapon)
    print(weapon.short_name())
    shooting1 = Shooting("Pistol", 70, 10)
    shooting2 = Shooting("Sniper Rifle", 90, 5)
    shooting = Shooting()
    shootings.add_shooting(shooting1)
    shootings.add_shooting(shooting2)
    shooting.load_from_file("shootings.txt")
    shooting.display_shootings()
    print("Number of effective shootings:"), shooting.effective_shootings()

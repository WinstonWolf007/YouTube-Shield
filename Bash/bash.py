from Bash.splitLine import Split


splits = Split().splits


class Bash:
    def run(self):
        command = input("YoutubeShield~$ ")
        print(splits(command))


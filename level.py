class Level:

    def get_level_category(self, level_id: int):
        level = []
        #tier/level 1 contains the physiological needs categories
        level.append([ "air.txt", "food.txt", "water.txt","sex.txt"])
        #tier/level 2 contains the safety categories
        level.append(["safety.txt", "security.txt"])
        #tier/level 3 contains love/belonging categories
        level.append(["love.txt", "friendship.txt"])
        #tier/level 4 contains esteem categories
        level.append(["confidence.txt", "achievement.txt"])
        #tier/level 5 contains self-actualization categories
        level.append(["morality.txt", "creativity.txt"])


        return level[level_id]


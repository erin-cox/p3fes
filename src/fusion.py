import json

class Data:
    def __init__(self, path):
        with open(path) as f:
            data = json.load(f)
        
        personae = data["personae"]
        self.personae_by_name = { item["name"]: item for item in personae }
        self.personae_by_arcana = self.get_personae_by_arcana(personae)
        self.arcana = data["arcana"]
        self.arcana = { item: i for i, item in enumerate(data["arcana"]) }
    
    
    def get_personae_by_arcana(self, data):
        personae_by_arcana = {}
        for item in data:
            arcana = item["arcana"]
            if arcana not in personae_by_arcana:
                personae_by_arcana[arcana] = []
            else:
                personae_by_arcana[arcana].append(item)
        return personae_by_arcana








FUSION_TABLE = [
    [ 0,   5,  8, 10,  7,  9,  2,  4,  6,  2,  8, 12,  1, 11,  5,  9, 18, 21, 10,  3, 17, 13],
    [ 4,   1,  6, 12, 14,  9,  4, 15,  5,  7,  4, -1, 15, -1, 13, 14,  3,  3,  2,  6, -1, -1],
    [ 1,  15,  2,  6,  8,  7,  1,  1,  6, 11,  1,  9, 11,  4,  3, -1, -1,  8, 17, 17,  3,  3],
    [10,  12,  6,  3,  6,  2, 10, 15,  4,  6, 11,  7,  7,  6,  6,  6,  7, 14,  6,  6, -1, 18],
    [ 7,   6,  5,  0,  4,  7,  7,  9, 15, 11, -1, 12,  9, 18, 12, -1, -1,  8, -1,  3,  5, -1],
    [ 9,   9,  7,  2,  7,  5,  1,  8,  7,  7,  4,  2,  6,  3, 11, -1, 14,  2, 14, 14,  6, -1],
    [14,  15,  9, 10, 11, 14,  6,  4,  7,  8,  1,  5,  9, 15,  2, 11, 17,  5,  3,  5, -1, 12],
    [15,  18,  4, 15,  8, 19, 11,  7,  1, 14, 11,  8, 10, -1, 13, 12, 18, -1, 10, -1, -1, 13],
    [ 1,   0,  5,  4,  7,  1, 12,  1,  8,  2,  7, 14,  2, 18, 18, -1, 17,  4, -1,  4, 21, -1],
    [ 2,  12,  0,  6,  6,  7,  5, 12, 11,  9,  4, 10, 10, -1, 12, 13, -1,  7,  1, -1, -1, 17],
    [ 8,   4,  1, 11, 19,  4,  0,  9,  7,  4, 10, -1, 11, -1,  6, 18, 18, 18,  7, 14, -1, 15],
    [12,  17,  7,  7, 12,  4,  5,  8, 14, 10, 19, 11,  9, 12, 18, 10, 15,  2, 12,  2, 12, -1],
    [ 1,  15, 11,  7, 14, 10,  9, 10,  2, 10, 11, 10, 12, 15,  5, 18, 13, 11,  3, -1, -1, 14],
    [11,  16,  4, 15, 18,  3, 15,  0, 18, 16, 20, 12, 15, 13, -1, -1, -1, -1, 17, -1, -1, -1],
    [11,  13,  3,  6, 12, 11,  2, 13, 18, 12,  6, 18,  5, 16, 14, 13, 15, 18,  3, 17, 18, 17],
    [  8, 14, 16,  1, 16,  0, 13, 17, 16, 13,  9,  3, 13, 20, 18, 15, -1, -1, -1, -1, -1, 6],
    [18,   3, 13,  7, 13, 14, 17, 18, 19, 13, 21, 20, 13, 19, 15, 20, 16, -1, 10, -1, 21, 18],
    [21,   3,  8, 14,  9,  2,  5, 19,  4,  7, 18,  2, 11, 16,  9,  1, 20, 17, 13,  8, 14, 15],
    [10,  10, 17,  6, 16, 14,  3, 10, 16,  1,  7, 21,  3, 17,  3, 20, 10, 19, 18, 14, -1, -1],
    [ 3,   6, 17,  6,  3, 14,  5,  8,  4, 17, 14,  2, 20, 18, 20, 13, 18, 21, 14, 19, 17,  3],
    [17,  16,  8, 15,  5,  6, 19, 16, 21, 16, 17, 12, 21,  0,  8, 18, 21, 14,  2, 17, 20, 17],
    [13,  19,  3, 18, 19, 14, 12, 13, 20, 17, 15, 16, 14, 19, 17,  6,  0, 15, 20,  3,  0, 21],
]



meow = [
        "Fool",
        "Magician",
        "Priestess",
        "Empress",
        "Emperor",
        "Hierophant",
        "Lovers",
        "Chariot",
        "Justice",
        "Hermit",
        "Fortune",
        "Strength",
        "Hanged Man",
        "Death",
        "Temperance",
        "Devil",
        "Tower",
        "Star",
        "Moon",
        "Sun",
        "Judgement",
        "Aeon"
    ]





def normal_spread_arcana(arcana1, arcana2):
    pass

def normal_spread(persona_1, persona_2):
    arcana = 3
    level = persona1["level"] + persona2["level"] // 2 + 1




if __name__ == "__main__":
    normal = {}
    triple = {}
    for i, s in enumerate(meow):
        table[s] = []
        for i in 
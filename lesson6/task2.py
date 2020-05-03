class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_asphalt(self, weight=25, height=5):
        return int(round(self._length * self._width * weight * height / 1000, 0))


new_road = Road(5000, 20)
print(f'Масса необходимого асфальта для дороги: {new_road.weight_asphalt()} т')

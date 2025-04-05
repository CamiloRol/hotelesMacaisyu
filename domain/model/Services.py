class Services:
    def __init__(self, laundry, breakfast, gym, pool):
        self._laundry = laundry
        self._breakfast = breakfast
        self._gym = gym
        self._pool = pool

    @property
    def get_laundry(self):
        return self._laundry

    @get_laundry.setter
    def set_laundry(self, laundry):
        self._laundry = laundry

    @property
    def get_breakfast(self):
        return self._breakfast

    @get_breakfast.setter
    def set_breakfast(self, breakfast):
        self._breakfast = breakfast

    @property
    def get_gym(self):
        return self._gym

    @get_gym.setter
    def set_gym(self, gym):
        self._gym = gym

    @property
    def get_pool(self):
        return self._pool

    @get_pool.setter
    def set_pool(self, pool):
        self._pool = pool

    def showServices(self):
        print("Servicios del Hotel: ")
        print(f"Lavandería: {'Disponible' if self._laundry else 'No disponible' } ")
        print(f"Desayuno: {'Disponible' if self._breakfast else 'No disponible'} ")
        print(f"Gimnasio: {'Disponible' if self._gym else 'No disponible'} ")
        print(f"Piscina: {'Disponible' if self._pool else 'No disponible'} ")


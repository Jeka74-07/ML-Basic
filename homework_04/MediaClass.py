class MediaFile(ABC):
    def __init__(self, name, size, owner, storage: StorageBackend):
        self.name, self.size, self.owner = name, size, owner
        self.storage = storage  # Инъекция зависимости
        self.path = None

    def save(self, data):
        self.path = self.storage.save(self.name, data)

    @abstractmethod
    def extract_features(self): pass

class VideoFile(MediaFile):
    def __init__(self, name, size, owner, storage, resolution):
        super().__init__(name, size, owner, storage)
        self.resolution = resolution

    def extract_features(self): 
        print(f"Анализ видео {self.resolution}...")
from abc import ABC, abstractmethod

class StorageBackend(ABC):
    @abstractmethod
    def save(self, name: str, data: bytes) -> str: pass
    
    @abstractmethod
    def delete(self, path: str): pass

class LocalStorage(StorageBackend):
    def save(self, name, data): return f"/local/path/{name}"
    def delete(self, path): print(f"Удалено с диска: {path}")

class S3Storage(StorageBackend):
    def save(self, name, data): return f"s3://bucket/{name}"
    def delete(self, path): print(f"Удалено из S3: {path}")
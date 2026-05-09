# Создаем видео для S3
video = VideoFile("Hi.mp4", 1024, "user1", S3Storage(), "4K")
video.save(b"data") # Сохранится в S3

# Создаем фото для локального диска
photo = PhotoFile("Hi.png", 100, "user1", LocalStorage(), (512, 512))
photo.save(b"data") # Сохранится локально


with Session(engine) as session:
    # Создаем объекты (строки таблицы)
    user1 = User(name="Алексей", age=300)
    user2 = User(name="Мария", age=25)

    # Добавляем их в сессию
    session.add_all([user1, user2])

    # Фиксируем изменения в базе данных
    session.commit()
import random
import pytest


class TestBooksCollector:

    def test_books_genre_fav_dict_is_empty(self, books_collector):

        assert len(books_collector.books_genre) == 0 and len(books_collector.favorites) == 0

    def test_genre_list_is_not_empty(self, books_collector):

        assert books_collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_list_is_not_empty(self, books_collector):

        assert books_collector.genre_age_rating == ['Ужасы', 'Детективы']

    @pytest.mark.parametrize('book', ['Zorro', 'Астерикс и Обеликс'])
    def test_add_new_book_positive(self, books_collector, book):
        books_collector.add_new_book(book)
        assert book in books_collector.books_genre
        assert books_collector.books_genre[book] == ''

    @pytest.mark.parametrize('book', ['', 'Как левша подковал блоху, съездил в Париж и проглотил волшебные бобы'])
    def test_add_new_book_invalid_name_does_not_add_book(self, books_collector, book):
        initial_book_count = len(books_collector.books_genre)
        books_collector.add_new_book(book)
        assert len(books_collector.books_genre) == initial_book_count
        
    
    def test_set_book_genre_valid_name(self, books_collector):
        book_name = 'Пирамидо-сосковая война'
        genre = 'Детективы'
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)
        assert books_collector.books_genre[book_name] == genre
        

    @pytest.mark.parametrize('genre', ['Несуществующий жанр', 'Белиберда'])
    def test_set_book_genre_invalid_genre(self, books_collector, genre):

        book_name = 'Вторая пуническая война'
        books_collector.add_new_book(book_name)
        initial_genre = books_collector.get_book_genre(book_name)
        books_collector.set_book_genre(book_name, genre)
        assert books_collector.get_book_genre(book_name) == initial_genre

    def test_get_book_genre_return_valid_name(self, books_collector):

        book_name = 'Иерархиус'
        genre = 'Фантастика'
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)
        assert books_collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre_when_valid_genre(self, books_collector):

        book_with_genre = 'Головочёс'
        genre = 'Мультфильмы'

        books_collector.add_new_book(book_with_genre)
        books_collector.set_book_genre(book_with_genre, genre)

        books_with_genre = books_collector.get_books_with_specific_genre(genre)

        assert books_with_genre == [book_with_genre], f"Ожидался список ['{book_with_genre}'], получен: {books_with_genre}"


    def test_get_books_with_specific_genre_empty_list_book_false_genre(self, books_collector):
        book_name = 'Бирманский кот'
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, 'Фантастика')
        non_existent_genre = 'Шутёхи'
        books_with_genre = books_collector.get_books_with_specific_genre(non_existent_genre)
        assert books_with_genre == [], f"Ожидался пустой список для жанра '{non_existent_genre}', получен: {books_with_genre}"

    def test_get_books_with_specific_genre_no_such_genre(self, books_collector):
        non_existent_genre = 'Шутёхи'
        assert books_collector.get_books_with_specific_genre(non_existent_genre) == [], "Ожидался пустой список для несуществующего жанра"
         
    def test_get_books_genre_filled_dict(self, books_collector):

        books = ['Торадора', 'Закупяченский движ', 'Суета на ферме', 'Огорошен и ладно'] # Исходные названия
        genres = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы'] # Жанры для каждой книги
        expected_books_genre = {}

        for i, name in enumerate(books):
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, genres[i])
            expected_books_genre[name] = genres[i]

        assert books_collector.get_books_genre() == expected_books_genre, \
            f"Ожидался словарь {expected_books_genre}, получен: {books_collector.get_books_genre()}"

    def test_get_books_genre_empty_dict(self, books_collector):

        books = books_collector.get_books_genre()
        assert isinstance(books, dict)
        assert not books


    def test_get_books_for_children_correct_genre(self, books_collector):

        books = ['Бивнеглазый', 'Кучерявая вилка', 'Дуремар', 'Брюквенный вождь', 'Окрест']
        genres = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        expected_children_books = []

        for i, name in enumerate(books):
            books_collector.add_new_book(name)
            books_collector.set_book_genre(name, genres[i])
            if genres[i] not in books_collector.genre_age_rating:
                expected_children_books.append(name)

        children_books = books_collector.get_books_for_children()
        assert children_books == expected_children_books, \
            f"Ожидался список {expected_children_books}, получен: {children_books}"

    
    def test_get_books_for_children_adult_rating(self, books_collector):

        adult_book1 = 'Дюймовочка'
        adult_book2 = 'Снежная королева'
        adult_genre = 'Ужасы'

        books_collector.add_new_book(adult_book1)
        books_collector.set_book_genre(adult_book1, adult_genre)
        books_collector.add_new_book(adult_book2)
        books_collector.set_book_genre(adult_book2, adult_genre)

        children_books = books_collector.get_books_for_children()
        assert children_books == [], "Список детских книг должен быть пустым"
    

    def test_get_books_for_children_mixed_ratings(self, books_collector):
        
        child_book = 'Винни-Пух'
        child_genre = 'Мультфильмы'
        books_collector.add_new_book(child_book)
        books_collector.set_book_genre(child_book, child_genre)

        adult_book = 'Дюна'
        adult_genre = 'Ужасы'
        books_collector.add_new_book(adult_book)
        books_collector.set_book_genre(adult_book, adult_genre)

        children_books = books_collector.get_books_for_children()
        assert children_books == [child_book], f"Ожидался список ['{child_book}'], получен: {children_books}" 


    def test_add_book_in_favorites_when_book_not_in_collection(self, books_collector):

        book_name = 'Кошачья мягковость'
        books_collector.add_book_in_favorites(book_name)
        assert book_name not in books_collector.get_list_of_favorites_books(), f"Книга '{book_name}' не должна быть в избранном, так как ее нет в коллекции."

    def test_add_book_in_favorites_when_book_is_in_collection(self, books_collector):   
        
        book_name = 'Воркователь иглу'
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)
        
        assert book_name in books_collector.favorites

    def test_add_book_in_favorites_twice(self, books_collector):
        
        book_name = 'Горячий слух'
        books_collector.add_new_book(book_name)
        books_collector.add_book_in_favorites(book_name)
        books_collector.add_book_in_favorites(book_name)

        assert books_collector.favorites.count(book_name) == 1        
    
    def test_delete_book_from_favorites(self, books_collector):

        books_collector.add_new_book('Убийца Акамэ')
        books_collector.add_book_in_favorites('Убийца Акамэ')

        books_collector.delete_book_from_favorites('Убийца Акамэ')
        assert 'Убийца Акамэ' not in books_collector.favorites

    def test_delete_book_from_favorites_no_name_in_list(self, books_collector):

        book_to_delete = 'Комплаенс в Слизерин'

        books_collector.delete_book_from_favorites(book_to_delete)
        assert book_to_delete not in books_collector.favorites


    def test_get_list_of_favorites_books_not_empty(self, books_collector):

        books = ['Славянский дебош', 'Кринж в посёлке', 'Дед хейтит внуков']
        for name in books:
            books_collector.add_new_book(name)
            books_collector.add_book_in_favorites(name)

        assert books_collector.get_list_of_favorites_books() == books

    def test_get_list_of_favorites_books_empty_list(self, books_collector):

        favorites = books_collector.get_list_of_favorites_books()
        assert isinstance(favorites, list)
        assert not favorites
        
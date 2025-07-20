## Описание тестовых функций для класса *BooksCollector*

### Создание объекта вынесено фикстурой в конфтест


Ниже приведено описание групп тестов и отдельных тестов.

### Общие тесты инициализации

*   `test_books_genre_fav_dict_is_empty`: Проверяет, что словарь книг и список избранного изначально пустые.
*   `test_genre_list_is_not_empty`: Проверяет, что список доступных жанров (`genre`) не пуст.
*   `test_genre_age_rating_list_is_not_empty`: Проверяет, что список жанров с возрастным рейтингом (`genre_age_rating`) не пуст.

### Тесты add_new_book

*   `test_add_new_book_positive`: Проверяет, что добавление новой книги с допустимым названием добавляет её в словарь `books_genre` с пустым жанром. Использует параметризацию для проверки нескольких названий книг.
*   `test_add_new_book_invalid_name_does_not_add_book`: Проверяет, что книга с некорректным названием не добавляется. 

### Тесты set_book_genre

*   `test_set_book_genre_valid_name`: Проверяет, что возвращается корректный жанр книги.
*   `test_set_book_genre_invalid_genre`: Проверяет, что метод `set_book_genre` не изменяет жанр книги, если переданный жанр не является валидным (т.е. его нет в списке допустимых жанров).  В случае передачи валидного жанра, жанр книги успешно обновляется.

### Тесты get_book_genre

*   `test_get_book_genre_return_valid_name`: Проверяет, что возвращается корректный жанр книги.

### Тесты get_books_with_specific_genre

*   `test_get_books_with_specific_genre_when_valid_genre`: Проверяет, что получение списка книг с определенным жанром возвращает список, содержащий только книги с этим жанром.
*   `test_get_books_with_specific_genre_empty_list_book_false_genre`: Проверяет, когда книга существует в коллекции, у нее установлен определенный жанр, но затем запрашивается список книг с другим, несуществующим (или просто не совпадающим с установленным) жанром.
*   `test_get_books_with_specific_genre_no_such_genre`:  Проверяет, когда в коллекции вообще не выполняется добавление книг. Тест пытается получить список книг с несуществующим жанром, когда в коллекции нет ни одной книги.

### Тесты get_books_genre

*   `test_get_books_genre_filled_dict`: Проверяет, что `get_books_genre` возвращает словарь, содержащий добавленные книги.
*   `test_get_books_genre_empty_dict`: Проверяет, что `get_books_genre` возвращает пустой словарь, если книг не было добавлено.

### Тесты get_books_for_children
*   `test_get_books_for_children_correct_genre`:Проверяет,что возвращаются только книги с "детскими" жанрами.
*   `test_get_books_for_children_adult_rating`: Проверяет, что `get_books_for_children` возвращает пустой список, если добавлены только книги с "взрослыми" жанрами.
*   `test_get_books_for_children_mixed_ratings`: Проверяет, что `get_books_for_children` возвращает только книги с "детскими" жанрами, когда в коллекции есть книги как с детскими, так и со взрослыми жанрами.

### Тесты add_book_in_favorites


*   `test_add_book_in_favorites_when_book_not_in_collection`: Проверяет,  что добавление в избранное книги, которой нет в коллекции, не добавляет её в список `favorites`.
*   `test_add_book_in_favorites_when_book_is_in_collection`: Проверяет, что добавление в избранное книги, которая есть в коллекции, добавляет ее в список `favorites`.
*   `test_add_book_in_favorites_twice`: Проверяет, что повторное добавление книги в избранное добавляет ее в список `favorites` только один раз.

### Тесты delete_book_from_favorites

*   `test_delete_book_from_favorites`: Проверяет, что удаление книги из избранного, когда она там есть, удаляет её из списка `favorites`.
*   `test_delete_book_from_favorites_no_name_in_list`: Проверяет, что удаление книги из избранного, когда её там нет, не изменяет список `favorites`

### Тесты get_list_of_favorites_books

*   `test_get_list_of_favorites_books_not_empty`: Проверяет, что `get_list_of_favorites_books` возвращает список избранных книг, если он не пуст.
*   `test_get_list_of_favorites_books_empty_list`: Проверяет, что `get_list_of_favorites_books` возвращает пустой список, если список избранных книг пуст.

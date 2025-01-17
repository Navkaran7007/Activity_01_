""""
Description: A class to manage LibraryItem objects.
"""
__author__ = "Navkaran Singh Sidhu"
__version__ = "1.0.0"

from genre.genre import Genre


class LibraryItem:
    """
    LibraryItem: Maintain LibraryItem Data.
    """
    def __init__(self, item_id : int,
                 title : str, 
                 author : str ,
                 genre : Genre,  
                 is_borrowed : bool ):
        """
        Initializes the class attributes with argument values.
        Args: 
            item_id (int): The Item Id of LibraryItem.
            title (str): The title of the LibraryItem.
            author (str): The author of the LibraryItem.
            genre (Genre): The genre to which the LibraryItem applies.
            is_borrowed (bool) : The borrowed item of LibraryItem
        Raises:
            ValueError: When title or author is blank, genre is 
            invalid, Item_id is non-numeric and is_borrowed is non-boolean.
        """
        if isinstance(item_id, int):
            self.__item_id = item_id
        else:
            raise ValueError("Item Id must be numeric.")
        
        if len(title.strip()) > 0:
            self.__title = title
        else:
            raise ValueError("Title cannot be blank.")
        
        if len(author.strip()) > 0:
            self.__author = author
        else:
            raise ValueError("Author cannot be blank.")

        if isinstance(genre, Genre):
            self.__genre = genre
        else:
            raise ValueError("Invalid Genre")
        
        if isinstance(is_borrowed, bool):
            self.__is_borrowed = is_borrowed
        else:
            raise ValueError("Is Borrowed must be a boolean value.")

    @property
    def item_id(self) -> int:
        """
        Accessor for Item Id attribute.

        Returns:
            int: item_id value.

        """
        return self.__item_id

    @property
    def title(self) -> str:
        """
        Accessor for title atttibute.

        Returns:
            str: title of the LibraryItem.

        """
        return self.__title
        
    @property
    def author(self) -> str:
        """
        Accessor for author atttibute.

        Returns:
            str: author of the LibraryItem.

        """
        return self.__author    

    @property
    def genre(self) -> Genre:
        """
        Accessor for genre attribute.

        Returns:
            Genre:  Enum value of genre.

        """
        return self.__genre
    
    @property
    def is_borrowed(self) -> bool:
        """
        Accessor for is_borrowed attribute.

        Returns:
            bool: boolean value.

        """
        return self.__is_borrowed







        
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
    def __init__(self, title : str, 
                 author : str ,
                 genre : Genre ):
        """
        Initializes the class attributes with argument values.
        Args: 
            title (str): The title of the LibraryItem.
            author (str): The author of the LibraryItem.
            genre (Genre): The genre to which the LibraryItem applies.

        Raises:
            ValueError: When title or author is blank, genre is 
            invalid.

        """
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







        
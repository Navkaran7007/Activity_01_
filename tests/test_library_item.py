"""
Description: Unit tests for the LibraryItem class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_book.py
"""
__author__ = "Navkaran Singh Sidhu"
__version__ = "1.0.0"

import unittest
from genre.genre import Genre
from library_item.library_item import LibraryItem

class TestLibraryItem(unittest.TestCase):

    def setUp(self):
        self.LibraryItem = LibraryItem("Kingdom of Ash", 
                             "al sweigert", 
                             Genre.TRUE_CRIME)


    def test_init_valid_arguments_attributes_set(self):
        # Arrange & Act
        library_item = LibraryItem("Kingdom of Ash",
                        "al sweigert",           
                        Genre.TRUE_CRIME)

        # Assert
        self.assertEqual("Kingdom of Ash", 
                         library_item._LibraryItem__title )
        self.assertEqual("al sweigert", library_item._LibraryItem__author)
        self.assertEqual(Genre.TRUE_CRIME, 
                         library_item._LibraryItem__genre)
    
    def test_init_blank_title_raises_valueerror(self):
    # Arrange, Act and Assert
        with self.assertRaises(ValueError):
            library_item = LibraryItem("", "al sweigert",Genre.TRUE_CRIME)

    def test_init_invalid_genre_raises_valueerror(self):
        with self.assertRaises(ValueError):
            library_item = LibraryItem("Kingdom of Ash","al sweigert", "INVALID")

    def test_init_blank_author_raises_valueerror(self):
        with self.assertRaises(ValueError):
            library_item = LibraryItem("Kingdom of Ash", 
                            "",Genre.TRUE_CRIME)            
    
    def test_title_accessor_valid_LibraryItem_title_returned(self):
        self.assertEqual("Kingdom of Ash", self.LibraryItem.title)

    
    def test_author_accessor_valid_LibraryItem_author_returned(self):
        self.assertEqual("al sweigert", self.LibraryItem.author)

    def test_genre_accessor_valid_LibraryItem_genre_returned(self):
        self.assertEqual(Genre.TRUE_CRIME, self.LibraryItem.genre)



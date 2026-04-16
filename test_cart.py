import unittest

from cart import ShoppingCart

class test_add_item(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

def test_add_item(self):
    self.cart.add_item("Banana", 5.0, 3)
    self.cart.add_item("Apple", 7.0, 2)
    self.assertEqual(self.cart.get_total(), 29)

def test_valid_discount(self):
    self.cart.add_item("Strawberry",5.0,4)
    self.cart.apply_discount("SAVE10")
    self.assertEqual(self.cart.get_total(), 18)

def test_add_invalid_quality(self):
    with self.assertRaises(ValueError):
        self.cart.add_item("Kiwi",1.0,-2)
    with self.assertRaises(ValueError):
        self.cart.add_item("Kiwi",1.0,-2)

def test_remove_nonexistent(self):
    with self.assertRaises(KeyError):
        self.cart.remove_item("None_existent")

def test_discount_unmet_threshold(self):
    self.cart.add_item("Toilet", 5.0, 1)
    with self.assertRaises(ValueError):
        self.cart.apply_discount("SAVE20")

def test_add_duplicate_item(self):
    self.cart.add_item("Strawberry",5.0,4)
    self.cart.add_item("Strawberry",5.0,3)
    self.assertEqual(self.cart.get_total(), 35)

def test_discount_exact(self):
    self.cart.add_item("Blueberry", 15.0, 2)
    self.cart.apply_discount("FLAT5")
    self.assertEqual(self.cart.get_total(), 25)

def test_get_item_count(self):
    self.cart.add_item("Banana", 5.0, 3)
    self.cart.add_item("Apple", 7.0, 2)
    self.assertEqual(self.cart.get_item_count(), 5)

if __name__ == '__main__':
    unittest.main()
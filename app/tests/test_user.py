# Tests for the class user

import unittest
from app.user.user import User
from app.bucketlist.bucketlist_controller import BucketListController
from app.bucketlist.bucketlist import BucketList


class TestUser(unittest.TestCase):
  '''
    A user is a bucketlist controller
    A user is has a name, email and password
    A user can do everything a bucketlist controller does
  '''

  def setUp(self):
    ''' Set up reusable variables and instances '''
    self.user_details = ("jnlemayian@gmail.com", "Password", "James Lemayian")
    self.user_instance = User(*self.user_details)
    self.bucketlist_details = ("ItemName", "Description: optional")
    self.bucketlist = BucketList(*self.bucketlist_details, owner=self.user_details[0])

  # 1. Test structure and user instance creation
  def test_user_inherits_bucketlistcontroler(self):
    ''' Test that user inherits bucketlist controller '''
    # Assert that it's a user instance
    self.assertEqual(isinstance(self.user_instance, User), True)
    # Assert that it's also a bucketlist instance
    self.assertEqual(isinstance(self.user_instance, BucketListController), True)

  def test_user_has_all_properties(self):
    ''' Ensure user has name, email, password '''
    self.assertEqual(self.user_instance.name, self.user_details[2])
    self.assertEqual(self.user_instance.email, self.user_details[0])
    self.assertEqual(self.user_instance.password, self.user_details[1])

  def test_user_representation(self):
    ''' Assert that __repr__ function returns a useful object representation '''
    self.assertEqual(str(self.user_instance), "James Lemayian")

  ## The user is just an extension of the bucketlist controller
  # 2. Test bucketlist controller operations
  def test_user_can_create_bucketlist(self):
      ''' Asserting that a bucketlist controller can create a bucketlist '''
      new_bucketlist_details = ("NewName", "Description: Optional")
      new_bucketlist = self.user_instance.add_bucketlist(new_bucketlist_details)
      self.assertEqual(isinstance(new_bucketlist[0], BucketList), True)
      self.assertEqual(new_bucketlist_details[0] in self.user_instance.available_bucketlists, True)
      self.assertEqual(new_bucketlist[1], "{} bucketlist has been created".format(new_bucketlist_details[0]))

  
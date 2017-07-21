#  This is the structure of the bucketlist

from app.bucketlist_item import BucketListItem


class BucketList:
    ''' The bucketlist object '''

    def __init__(self, name, details=None, items=None, owner=None):
        ''' Constructing and instance of the object '''
        # Every bucketlist must have an owner
        if owner is None:
            raise Exception("Every bucketlist must have an owner")
        self.name = name
        self.details = details
        if items is not None:
            self.items = items
        else:
            self.items = []
        self.owner = owner

    @property
    def bucket_id(self):
        return "{}-{}".format(self.owner, self.name)

    def add_item(self, item_details, owner):
        # initialize an instance of a BucketListItem
        item_name = item_details[0]
        # ensure that items does not exist in items
        if item_name in self.items:
            raise Exception("{} already exists!".format(item_name))
        self.items.append(item_name)
        new_item = BucketListItem(*item_details, bucketlist=owner)
        return (new_item, "{} added successfully".format(item_name))

    def remove_item(self, item_name):
        if item_name not in self.items:
            raise Exception("{} does not exist.".format(item_name))
        self.items.remove(item_name)
        # the class instance of bucketlist item will be garbage collected
        return "{} removed successfully".format(item_name)

    def __repr__(self):
        ''' Represent item by name '''
        if self.name is None:
            return 'Bucketlist does not exist'
        return self.name

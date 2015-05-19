__author__ = 'moran'
class Crowdmap(object):
	def __init__(self, init_list):
		self.list = init_list
		self.location_service = LocationService()

	def get_all_posts_for(self, name):
		return [post for post in self.list if post.find(name) != -1]

	def is_location_for_name(self, name):
		name_posts = self.get_all_posts_for(name)
		for post in name_posts:
			if self.location_service.find(post): # if location_service.find(post):
				return True
		return False
	
	def is_different_location_for_name(self, name):
		name_post = self.get_all_posts_for(name)
		locations= self.location_service.all_locations(name_post)
		return (len(locations )!= 1)
		
		
class LocationService:
	def find(self, text):
		return (text.find("Bangkok") != -1 or text.find("Langtang") != -1)

	def all_locations(self, name_post):
		list =[]
		for post in name_post:
			if self.find(post):
				list.insert(len(list), self.get_location(post))	
		return list
	
	def get_location(self, text):
		if (text.find("Bangkok") != -1):
			return "Bangkok"
		if(text.find("Langtang") != -1):
			return "Langtang"
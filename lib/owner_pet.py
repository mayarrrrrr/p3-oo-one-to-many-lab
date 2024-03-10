class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self,name,pet_type,owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type.")
        self.name =name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
    
    def get_pet_type(self):
     return self._pet_type

    def set_pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception('Not a valid pet type.')
        self._pet_type = pet_type

    pet_type = property(get_pet_type, set_pet_type)
        
    pass
pass

class Owner:
    def __init__(self,name):
        self.name = name
        pass
    
    def pets(self):
     return [pet for pet in Pet.all if pet.owner == self]
        
    def add_pet(self,pet):
        if isinstance(pet,Pet):
            pet.owner =self
        else:
            raise Exception("Owner can only have pets of type Pet.")  
        
    def get_sorted_pets(self):
        return sorted (self.pets(),key = lambda x:x.name)      

    pass
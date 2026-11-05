class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    def __init__(self, name): 
        self.name = name 
        self.friends = []
    
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    def __init__(self):
        self.people ={}
    
    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)
    
    def add_friendship(self, person1_name, person2_name):
        if person1_name in self.people and person2_name in self.people:
            person1 = self.people[person1_name]
            person2 = self.people[person2_name]
            person1.add_friend(person2)
            person2.add_friend(person1)
        else:
            missing = [n for n in (person1_name, person2_name) if n not in self.people]
            print(f"Error: {', '.join(missing)} not found in the network.")
        
    def print_network(self):
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{name}: {friend_names}")

# Test your code here
if __name__ == "__main__":
    network = SocialNetwork()

    for name in ["Betsi", "Jessica", "Josh", "Kevin", "Ana", "Marc"]:
        network.add_person(name)

    network.add_friendship("Betsi", "Jessica")
    network.add_friendship("Betsi", "Josh")
    network.add_friendship("Betsi", "Kevin")
    network.add_friendship("Jessica", "Josh")
    network.add_friendship("Jessica", "Ana")
    network.add_friendship("Josh", "Kevin")
    network.add_friendship("Kevin", "Marc")
    network.add_friendship("Ana", "Marc")

    print("--- Network after initial setup ---")
    network.print_network()
    
    print("\n--- Edge case: nonexistent person ---")
    network.add_friendship("Betsi", "Zoe")
    network.add_friendship("Zoe", "Yan")
    
    print("\n--- Edge case: duplicate person ---")
    network.add_person("Betsi")
    print(f"Betsi's friends still intact: {[f.name for f in network.people['Betsi'].friends]}")
    print(f"Total people in network: {len(network.people)}")

    print("\n--- Edge case: duplicate friendship ---")
    network.add_friendship("Betsi", "Jessica")
    print(f"Betsi's friends: {[f.name for f in network.people['Betsi'].friends]}")

    print("\n--- Network after additional changes ---")
    network.add_person("Grace")
    network.add_friendship("Grace", "Marc")
    network.add_friendship("Grace", "Betsi")
    network.print_network()

#Design Memo

##Why is a graph the right structure to represent a social network?
#A graph was the right structure to represent a social network because there are sparse connections between friendships, since they are interconnected and one person can have many to many connections. A graph connects nodes through edges arbitrarily. Nodes represent individual users or accounts while edges represent the bonds or interactions between the nodes. Edges can be both undirected or directed. This structure naturally supports cycles, making it easier to represent closed loops of friendships. 
#Why wouldn’t a list or tree work as well for this?
#A list or tree wouldn’t work well because they would require a specific order, sequential or hierarchical relationships, and a social network doesn't have a particular order, breaking the rule of lists and trees. A list can’t show whether a person is simultaneously connected with other people and it would create confusion with duplicated data. A tree can’t contain cycles because it only contains a parent-child hierarchy. A node would only be able to have one parent limiting to represent different connections among various friendships. 
#What performance or structural trade-offs did you notice when adding friends or printing the network?
#The adjacency list for the social network kept memory usage low, since it only stores friendships that do exist instead of every possible friendship with the different individuals. Adding people was fast since the dictionary lookup takes constant time and listing a person's friends is easy because the list is already stored on their Person object. The main trade-off is that checking whether two specific people are friends, or avoiding a duplicate friendship, requires scanning a friends list, which gets slower as someone’s friend count grows. Each friendship is also stored twice, once on each person, which adds redundancy and means the two sides could get out of sync if add_friend is called directly instead of through add_friendship.

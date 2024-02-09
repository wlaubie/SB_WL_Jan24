###########Collection Module

######Collections & Counting

#ex 1: Counter

# Import the Counter object
from collections import Counter

# Create a Counter of the penguins sex using a list comprehensions
##penguins_sex_counts = Counter([penguin['Sex'] for penguin in penguins])

# Print the penguins_sex_counts
##print(penguins_sex_counts)


#ex 2: Counter

# Import the Counter object
from collections import Counter

# Create a Counter of the penguins list: penguins_species_counts
##penguins_species_counts = Counter([penguin["Species"] for penguin in penguins])

# Find the 3 most common species counts
##print(penguins_species_counts.most_common(3))


#ex 3: Dictionaries and Tuples

# Create an empty dictionary: female_penguin_weights
female_penguin_weights = {}

# Iterate over the weight_log entries
##for species, sex, body_mass in weight_log:
    # Check to see if species is already in the dictionary
##    if species not in female_penguin_weights:
        # Create an empty list for any missing species
##        female_penguin_weights[species] = []
    # Append the sex and body_mass as a tuple to the species keys list
##    female_penguin_weights[species].append((sex, body_mass))

# Print the weights for 'Adlie'
##print(female_penguin_weights["Adlie"])


#ex 4: Dictionaries, items and slicing

# Import defaultdict
from collections import defaultdict

# Create a defaultdict with a default type of list: male_penguin_weights
male_penguin_weights = defaultdict(list)

# Iterate over the weight_log entries
##for species, sex, body_mass in weight_log:
    # Use the species as the key, and append the body_mass to it
##    male_penguin_weights[species].append(body_mass)

# Print the first 2 items of the ridership dictionary
##print(list(male_penguin_weights.items())[:2])


#ex 5: Dataclasses

# Import dataclass
from dataclasses import dataclass

@dataclass
class WeightEntry:
    # Define the fields on the class
    species: str
    flipper_length: int
    body_mass: int
    sex: str

    # Define a property that returns the body_mass / flipper_length
    @property
    def mass_to_flipper_length_ratio(self):
        return self.body_mass / self.flipper_length

#ex 6: Data Class iteration

# Create the empty list: labeled_entries
labeled_entries = []

# Iterate over the weight_log entries
##for species, sex, flipper_length, body_mass in weight_log:
    # Append a new WeightEntry instance to labeled_entries
##    labeled_entries.append(WeightEntry(species, flipper_length, body_mass, sex))

# Print a list of the first 5 mass_to_flipper_length_ratio values >> Data class and property
##print([entry.mass_to_flipper_length_ratio for entry in labeled_entries[:5]])


#ex 7: NamedTuple

from collections import namedtuple

Color = namedtuple("Color", ["red", "green", "blue"])
color = Color(55,155,255) #link each color to a value

print(color.red)



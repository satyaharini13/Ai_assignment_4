# Telangana Map Coloring using CSP (Backtracking)

# 33 Districts Adjacency List
telangana_map = {
    "Adilabad": ["Kumuram Bheem", "Nirmal"],
    "Kumuram Bheem": ["Adilabad", "Mancherial", "Nirmal"],
    "Mancherial": ["Kumuram Bheem", "Peddapalli", "Jagtial"],
    "Nirmal": ["Adilabad", "Kumuram Bheem", "Nizamabad"],
    "Nizamabad": ["Nirmal", "Kamareddy", "Jagtial"],
    "Jagtial": ["Nizamabad", "Mancherial", "Peddapalli", "Rajanna Sircilla"],
    "Peddapalli": ["Mancherial", "Jagtial", "Karimnagar"],
    "Karimnagar": ["Peddapalli", "Jagtial", "Rajanna Sircilla", "Siddipet"],
    "Rajanna Sircilla": ["Jagtial", "Karimnagar", "Siddipet", "Kamareddy"],
    "Kamareddy": ["Nizamabad", "Rajanna Sircilla", "Medak"],
    "Medak": ["Kamareddy", "Sangareddy", "Siddipet"],
    "Sangareddy": ["Medak", "Vikarabad", "Rangareddy"],
    "Siddipet": ["Medak", "Karimnagar", "Rajanna Sircilla", "Jangaon"],
    "Jangaon": ["Siddipet", "Warangal Rural", "Yadadri Bhuvanagiri"],
    "Warangal Rural": ["Jangaon", "Warangal Urban", "Mahabubabad"],
    "Warangal Urban": ["Warangal Rural", "Jayashankar Bhupalpally"],
    "Jayashankar Bhupalpally": ["Warangal Urban", "Mulugu"],
    "Mulugu": ["Jayashankar Bhupalpally", "Bhadradri Kothagudem"],
    "Bhadradri Kothagudem": ["Mulugu", "Khammam"],
    "Khammam": ["Bhadradri Kothagudem", "Mahabubabad", "Suryapet"],
    "Mahabubabad": ["Warangal Rural", "Khammam", "Jangaon"],
    "Suryapet": ["Khammam", "Nalgonda", "Yadadri Bhuvanagiri"],
    "Nalgonda": ["Suryapet", "Yadadri Bhuvanagiri", "Rangareddy", "Nagarkurnool"],
    "Yadadri Bhuvanagiri": ["Jangaon", "Suryapet", "Nalgonda", "Medchal"],
    "Medchal": ["Yadadri Bhuvanagiri", "Hyderabad", "Rangareddy"],
    "Hyderabad": ["Medchal", "Rangareddy"],
    "Rangareddy": ["Hyderabad", "Medchal", "Sangareddy", "Vikarabad", "Nalgonda"],
    "Vikarabad": ["Sangareddy", "Rangareddy", "Mahabubnagar"],
    "Mahabubnagar": ["Vikarabad", "Nagarkurnool", "Narayanpet"],
    "Nagarkurnool": ["Mahabubnagar", "Nalgonda", "Wanaparthy"],
    "Wanaparthy": ["Nagarkurnool", "Jogulamba Gadwal"],
    "Jogulamba Gadwal": ["Wanaparthy", "Narayanpet"],
    "Narayanpet": ["Mahabubnagar", "Jogulamba Gadwal"]
}

# Colors 
colors = ["Red", "Green", "Blue", "Yellow"]


# Check constraints
def is_valid(district, color, assignment):
    for neighbor in telangana_map[district]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


# Backtracking CSP
def backtrack(assignment):
    if len(assignment) == len(telangana_map):
        return assignment

    # Select unassigned district
    unassigned = [d for d in telangana_map if d not in assignment][0]

    for color in colors:
        if is_valid(unassigned, color, assignment):
            assignment[unassigned] = color

            result = backtrack(assignment)
            if result:
                return result

            # Backtrack
            del assignment[unassigned]

    return None


# Run
if __name__ == "__main__":
    solution = backtrack({})

    print("\nTelangana Map Coloring Solution:\n")
    for district in sorted(solution):
        print(f"{district:25} -> {solution[district]}")

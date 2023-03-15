from merge_sort import merge_sort
from recipe_stacks import sweet_yummyandfilling, sweet_healthyyetdecadent, savory_vegetarian, savory_nonvegetarian, all_stacks_unsorted

def recipe_choice_path(stck1, stck2, stck3, stck4):
    x = input("What kind of dish are you hungry for? Enter 'a' for savory or 'b' for sweet. ")
    if x == 'a':
        y = input("Great. Now enter 'c' for a nonvegetarian dish or 'd' for a vegetarian option. ")
        if y == 'c':
            print(stck4.pop())
        elif y == 'd':
            print(stck3.pop())
        else:
            print("That didn't work. Let's try again.")
            recipe_program(stck1, stck2, stck3, stck4)
    
    elif x == 'b':
        z = input("Great. Now enter 'e' for a healthy yet decadent dish or 'f' for a yummy and filling option. ")
        if z == 'e':
            print(stck2.pop())
        elif z == 'f':
            print(stck1.pop())
        else:
            print("That didn't work. Let's try again.")
            recipe_program(stck1, stck2, stck3, stck4)

    else:
        print("That didn't work. Let's try again.")
        recipe_program(stck1, stck2, stck3, stck4)

    go_again = input("Would you like to receive another recipe recommendation? Press 'y' for yes, 'n' for no. ")
    print(go_again)
    if go_again == 'y':
        return recipe_program(stck1, stck2, stck3, stck4)
    else:
        return "Thank you for using my recipe recommendation tool. Happy cooking und Guten Appetit!"


def get_sorted_recipe_lst(lst):
    sorted_recipes = merge_sort(lst)
    for recipe in sorted_recipes:
        print("{0}\n".format(recipe))

def greet(stck1, stck2, stck3, stck4):
    print("Hello and welcome to the recipe recommendation engine of my all-time favorite dishes!")
    print(input("Press enter to get started. "))
    print("Here is an alphabetized list of the dishes available to you: ")
    return get_sorted_recipe_lst(all_stacks_unsorted(stck1, stck2, stck3, stck4))


def recipe_program(stck1, stck2, stck3, stck4):
    greet(stck1, stck2, stck3, stck4)
    recipe_choice_path(stck1, stck2, stck3, stck4)

print(recipe_program(sweet_yummyandfilling, sweet_healthyyetdecadent, savory_vegetarian, savory_nonvegetarian))
from stack import Stack

#Initialize stacks

sweet_yummyandfilling = Stack()
sweet_healthyyetdecadent = Stack()
savory_vegetarian = Stack()
savory_nonvegetarian = Stack()

#Push onto stacks

sweet_yummyandfilling.push("Whole Grain Banana Bread")
sweet_yummyandfilling.push("Pumpkin Baked Oatmeal")
sweet_yummyandfilling.push("Spelt Cinnamon Rolls")

sweet_healthyyetdecadent.push("Chickpea Blondies")
sweet_healthyyetdecadent.push("Pumpkin Oatmeal Cookies")
sweet_healthyyetdecadent.push("Avocado Brownies")

savory_vegetarian.push("Sweet Potato Black Bean Salad")
savory_vegetarian.push("Tofu Stir Fry")
savory_vegetarian.push("Roasted Vegetable Salad")

savory_nonvegetarian.push("Mediterranean Shrimp and Veggies")
savory_nonvegetarian.push("Grilled Chicken Tenders")
savory_nonvegetarian.push("Fall Sheet Pan Chicken and Veggies")

#Related function and variable
def recipe_stack_unsorted(recipe_stack):
    recipe_stack_lst = []
    while recipe_stack.size > 0:
        recipe_stack_lst.append(recipe_stack.pop())
    for item in recipe_stack_lst:
        recipe_stack.push(item)
    return recipe_stack_lst


def all_stacks_unsorted(stck1, stck2, stck3, stck4):
     return recipe_stack_unsorted(stck1) + recipe_stack_unsorted(stck2) + recipe_stack_unsorted(stck3) + recipe_stack_unsorted(stck4)
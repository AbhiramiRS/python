Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("Original set elements:")
print("\nColor List 1:", color_list_1)
print("\nColor List 2:", color_list_2)
print("\nAll colors in Color list 1 but not in Color list 2:")
print(color_list_1.difference(color_list_2))
SyntaxError: multiple statements found while compiling a single statement

==== RESTART: C:/Users/DELL/AppData/Local/Programs/Python/Python310/color.py ===
Original set elements:

Color List 1: {'Red', 'White', 'Black'}

Color List 2: {'Red', 'Green'}

All colors in Color list 1 but not in Color list 2:
{'White', 'Black'}

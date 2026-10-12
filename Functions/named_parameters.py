def total_marks(physics, maths, science, english, hindi):
    print(f"Your marks in physics={physics}")
    print(f"Your marks in maths={maths}")
    print(f"Your marks in science={science}")
    print(f"Your marks in english={english}")
    print(f"Your marks in hindi={hindi}")
    total = physics + maths + science + english + hindi
    print(f"Your marks in marks={total}")


# total_marks(56, 98, 79, 32, 83)
# total_marks(science=56, physics=89, maths=90, hindi=89, english=69) #named parameters
total_marks(
    56, 98, hindi=85, english=89, science=70)  # named parameters always right and without name should be left
#Default Parameters
#Required parameters will be in left side and Default parameters
# will be in right side

def total_marks(physics=0, maths=0, science=0, english=0, hindi=0):
    # total_marks(physics, maths, science=0, english=0, hindi=0):#requiresd parameters
    print(f"Your marks in physics={physics}")
    print(f"Your marks in maths={maths}")
    print(f"Your marks in science={science}")
    print(f"Your marks in english={english}")
    print(f"Your marks in hindi={hindi}")
    total = physics + maths + science + english + hindi
    print(f"Your marks in marks={total}")


# total_marks(45, 67) 
# total_marks()
total_marks(maths=99,english=44)


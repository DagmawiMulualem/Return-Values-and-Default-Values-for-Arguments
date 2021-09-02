def allowed_bar(my_age):
    persons_age = my_age + 3
    return persons_age


person_allowed = allowed_bar(18)
print(person_allowed)


def gender_selector(sex ='uknown'):
    if sex is 'm':
        sex = "male"
    elif sex is 'f':
        sex = "female"
    print(sex)


gender_selector()

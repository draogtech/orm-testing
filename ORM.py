from peewee import PostgresqlDatabase, Model, CharField, BooleanField, IntegerField
psql_db = PostgresqlDatabase("class", host="localhost", user="postgres", password="masterdare12", port="5432")


class MyUser(Model):
    class Meta:
            database = psql_db

    age = IntegerField(4)
    username = CharField(20)
    password = CharField(10)
    email = CharField(30)

    is_beautiful = BooleanField(default=False)


if __name__ == "__main__":
    MyUser.create_table(fail_silently=True)

    new_user = MyUser(age=19, username="aberkowitz", password="secret", email="andrew@meltwater.org")
    # new_user.save()
    for my_user in MyUser.select():
        if new_user.age > 20:
            print("email {0} at {1}".format(my_user.username, my_user.email))
        else:
            pass

    user2 = MyUser(age=35, username="abu.okari", password="sasa", email="okari@meltwater.org")
    user2.save()
    user2.delete_instance()

    print(user2.age, user2.username, user2.email)

    is_aberkowitz = MyUser.select().where(MyUser.username == "aberkowitz")
    print(is_aberkowitz.get().username)
    is_not_aberkowitz = MyUser.select().where(MyUser.username != "aberkowitz")
    not_a_child = MyUser.select().where(MyUser.age > 21)
    really_not_a_child = MyUser.select().where((MyUser.age > 21) & (MyUser.username != "kelvint"))


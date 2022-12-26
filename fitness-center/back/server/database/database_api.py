from sqlalchemy import select, func

from database.models import engine, Capability, capability_table
from database.models import user_table, User
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)


def create_user(login: str, password: str) -> User:
    user = User()
    user.login = login
    user.password = password
    return user


def create_capability(img_name: str, title: str, description: str, more_info: str, info_image: str) -> Capability:
    capability = Capability()
    capability.img_name = img_name
    capability.title = title
    capability.description = description
    capability.more_info = more_info
    capability.info_image = info_image
    return capability


def select_from_table(query):
    with engine.connect() as connection:
        return connection.execute(query)


def find_user_by_login(login: str):
    result = select_from_table(select(user_table).where(user_table.c.login == login))
    return [_ for _ in result]


def add_user(user: User):
    s = Session()
    s.bulk_save_objects([user])
    s.commit()
    with engine.connect() as connection:
        res = [n for n in connection.execute(user_table.select())]
        return res[-1][0]


def add_capability(capability: Capability):
    s = Session()
    s.bulk_save_objects([capability])
    s.commit()


def get_all_capability(request):
    result = select_from_table(select(capability_table))
    return [_ for _ in result]

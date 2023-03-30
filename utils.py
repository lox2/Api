import psycopg2
import json
from datetime import datetime

with open("db/db.json") as read_json:
    properties = json.load(read_json)["db"]

CONN = conn = psycopg2.connect(properties)
FORMAT_STRING = "%d.%m.%Y"


def check_user(username: str, password: str) -> dict:
    """
    :param data: dict that contains username and password
    :return: dict {id: int, correct: True/False}
    """
    cursor = CONN.cursor()
    try:
        cursor.execute("""
        SELECT password, id FROM auth
        WHERE username = %s
        """, (username,))
        fetched = cursor.fetchall()[0]
        if fetched[0].strip() == password:
            cursor.close()
            return {"id": fetched[1],
                    "correct": True}
    except:
        cursor.close()


def register(username, password):
    cursor = CONN.cursor()

    cursor.execute("""
       SELECT id FROM auth
       WHERE username = %s
       """, (username,))

    fetched = cursor.fetchall()

    if fetched:
        cursor.close()
        return {"ok": False}

    cursor.execute("""
       INSERT INTO auth (username, password)
       values (%s, %s)
       """, (username, password,))

    cursor.execute("""
           SELECT id FROM auth
           WHERE username = %s
           """, (username,))

    user_id = cursor.fetchall()[0][0]

    cursor.execute("""
           INSERT INTO food (id, food)
           values (%s, %s)
           """, (user_id, json.dumps({})))

    cursor.execute("""
               INSERT INTO trains (id, trains)
               values (%s, %s)
                """, (user_id, json.dumps({})))

    CONN.commit()
    return {"id": user_id}


def change_password(username, password):
    cursor = CONN.cursor()

    cursor.execute("""
          SELECT id FROM auth
          WHERE username = %s
          """, (username,))

    fetched = cursor.fetchall()

    if not fetched:
        cursor.close()
        return False

    cursor.execute("""
          UPDATE auth 
          SET password = %s
          WHERE username = %s
          """, (password, username))

    CONN.commit()
    cursor.close()
    return True


def add_food(user_id, food, date):
    """
    :param user_id: int
    :param food: str
    :param date: format - day.month.year
    :return: bool
    """
    timestamp = str(datetime.strptime(date, FORMAT_STRING).timestamp())

    cursor = CONN.cursor()

    cursor.execute("""
              SELECT food FROM food
              WHERE id = %s
              """, (user_id,))

    fetched = cursor.fetchall()
    if fetched:
        old_food = fetched[0][0]

        if timestamp in old_food.keys():
            old_food[timestamp].append(food)

        else:
            old_food[timestamp] = [food]
        cursor.execute("""
                  UPDATE food 
                  SET food = %s
                  WHERE id = %s
                  """, (json.dumps(old_food), user_id))
        CONN.commit()
        cursor.close()
        return True
    cursor.close()
    return False


def remove_food(user_id, food, date):
    cursor = CONN.cursor()
    timestamp = str(datetime.strptime(date, FORMAT_STRING).timestamp())

    cursor.execute("""
              SELECT food FROM food
              WHERE id = %s
              """, (user_id,))

    fetched = cursor.fetchall()
    if fetched:
        old_food = fetched[0][0]
        if timestamp in old_food.keys():
            old_food[timestamp].remove(food)
        cursor.execute("""
                      UPDATE food 
                      SET food = %s
                      WHERE id = %s
                      """, (json.dumps(old_food), user_id))
        CONN.commit()
        cursor.close()
        return True

    cursor.close()
    return False


def add_train(user_id, train, date):
    cursor = CONN.cursor()

    timestamp = str(datetime.strptime(date, FORMAT_STRING).timestamp())

    cursor.execute("""
                  SELECT trains FROM trains
                  WHERE id = %s
                  """, (user_id,))

    fetched = cursor.fetchall()
    if fetched:
        old_trains = fetched[0][0]
        if timestamp in old_trains.keys():
            old_trains[timestamp].append(train)
        else:
            old_trains[timestamp] = [train]
        cursor.execute("""
                      UPDATE trains 
                      SET trains = %s
                      WHERE id = %s
                      """, (json.dumps(old_trains), user_id))
        CONN.commit()
        cursor.close()
        return True
    cursor.close()
    return False


def remove_train(user_id, train, date):
    cursor = CONN.cursor()
    timestamp = str(datetime.strptime(date, FORMAT_STRING).timestamp())

    cursor.execute("""
                  SELECT trains FROM trains
                  WHERE id = %s
                  """, (user_id,))

    fetched = cursor.fetchall()
    if fetched:
        old_trains = fetched[0][0]
        if timestamp in old_trains.keys():
            old_trains[timestamp].remove(train)
        old_trains["trains"].remove(train)
        cursor.execute("""
                      UPDATE trains 
                      SET trains = %s
                      WHERE id = %s
                      """, (json.dumps(old_trains), user_id))
        CONN.commit()
        cursor.close()
        return True
    cursor.close()
    return False


def get_trains(user_id, date):
    cursor = CONN.cursor()
    timestamp = str(datetime.strptime(date, FORMAT_STRING).timestamp())

    cursor.execute("""
                      SELECT trains FROM trains
                      WHERE id = %s
                      """, (user_id,))

    fetched = cursor.fetchall()

    if fetched[0][0].get(timestamp):
        return fetched[0][0][timestamp]
    return []


def get_food(user_id, date):
    cursor = CONN.cursor()
    timestamp = str(datetime.strptime(date, FORMAT_STRING).timestamp())
    cursor.execute("""
                      SELECT food FROM food
                      WHERE id = %s
                      """, (user_id,))

    fetched = cursor.fetchall()

    if fetched[0][0].get(timestamp):
        return fetched[0][0][timestamp]
    return []

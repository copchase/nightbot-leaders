import model


def test_leader_user_class_eq():
    a = model.LeaderUserClass(value=1, last_modified=2, user_id="a")

    b = model.LeaderUserClass(value=1, last_modified=2, user_id="b")

    assert a == b


def test_leader_user_class_ne():
    a = model.LeaderUserClass(value=2, last_modified=2, user_id="a")

    b = model.LeaderUserClass(value=1, last_modified=2, user_id="b")

    assert a != b


def test_leader_user_class_lt_gt():
    # Remember that we want the classes with lower values
    # to be considered higher for heapq
    a = model.LeaderUserClass(value=1, last_modified=2, user_id="a")

    b = model.LeaderUserClass(value=2, last_modified=2, user_id="b")

    assert b < a
    assert a > b


def test_leader_user_class_lt_gt_timestamp():
    # in the case of a value tie,
    # we want the winner to be the earliest modified
    a = model.LeaderUserClass(value=1, last_modified=20000, user_id="a")

    b = model.LeaderUserClass(value=1, last_modified=1, user_id="b")

    assert a > b
    assert b < a


def test_leader_user_class_lte_gte():
    a = model.LeaderUserClass(value=1, last_modified=2, user_id="a")

    b = model.LeaderUserClass(value=2, last_modified=2, user_id="b")

    assert a >= b
    assert b <= a

    a.value = 2

    assert a <= b
    assert b >= a

from life import questions


def test_life_answer_to_life_the_universe_and_everything():
    assert questions.the_answer_to_life_the_universe_and_everything() == 42


def test_life_answer_to_life_the_universe_and_everything_using_numpy():
    assert (
        len(questions.the_answer_to_life_the_universe_and_everything_using_numpy()) == 1
    )

from datetime import datetime

def validate_new_session(room, new_session):
    """
    Validate that the new session does not overlap with existing sessions in the room.

    Args:
        room 
        new_session 

    Raises:
        ValueError: If the new session overlaps with any existing session in the room.
    """
    pass


def test_no_overlap():
    """
    Test that a new session scheduled after the existing sessions passes without error.
    """
    print("Test No Overlap:")
    room = {
             'session_ids': [{'start_date': datetime(2024, 1, 1), 'end_date': datetime(2024, 1, 3)}]
           }
    new_session = {'start_date': datetime(2024, 1, 5), 'end_date': datetime(2024, 1, 7)}
    try:
        validate_new_session(room, new_session)
        print("Passed\n")
    except ValueError:
        print("Failed\n")


def test_exact_overlap():
    """
    Test that a new session with exact overlapping dates raises a ValueError.
    """
    print("Test Exact Overlap:")
    room = {
              'session_ids': [{'start_date': datetime(2024, 1, 1), 'end_date': datetime(2024, 1, 3)}]
            }
    new_session = {'start_date': datetime(2024, 1, 1), 'end_date': datetime(2024, 1, 3)}
    try:
        validate_new_session(room, new_session)
        print("Failed (Expected Error)\n")
    except ValueError:
        print("Passed (Error Raised as Expected)\n")


def test_partial_overlap():
    """
    Test that a new session partially overlapping with existing sessions raises a ValueError.
    """
    print("Test Partial Overlap:")
    room = {
            'session_ids': [{'start_date': datetime(2024, 1, 1), 'end_date': datetime(2024, 1, 3)}]
          }
    new_session = {'start_date': datetime(2024, 1, 2), 'end_date': datetime(2024, 1, 4)}
    try:
        validate_new_session(room, new_session)
        print("Failed (Expected Error)\n")
    except ValueError:
        print("Passed (Error Raised as Expected)\n")


def test_self_validation():
    """
    Test that validating a session against itself does not raise an error.
    """
    print("Test Self Validation:")
    session = {
               'start_date': datetime(2024, 1, 1), 'end_date': datetime(2024, 1, 3)
                }
    room = {'session_ids': [session]}
    try:
        validate_new_session(room, session)
        print("Passed\n")
    except ValueError:
        print("Failed\n")



test_no_overlap()
test_exact_overlap()
test_partial_overlap()
test_self_validation()

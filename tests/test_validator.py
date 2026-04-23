from app.validator import validate

def test_safe_command():
    assert validate("docker ps") == True


def test_blocked_command():
    assert validate("docker system prune") == False

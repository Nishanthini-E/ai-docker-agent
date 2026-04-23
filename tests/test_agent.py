from app.agent import interpret_command

def test_build_command():
    result = interpret_command("build image")
    assert "docker build" in result


def test_run_command():
    result = interpret_command("run container")
    assert "docker run" in result


def test_unknown_command():
    result = interpret_command("do something random")
    assert result is None

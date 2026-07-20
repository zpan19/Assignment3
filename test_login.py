from login import login


def test_tc01_valid_login():
    result = login("student@example.com", "password123")

    assert result["success"] is True
    assert "token" in result
    assert result["token"] != ""


def test_tc02_missing_email():
    result = login("", "password123")

    assert result["success"] is False
    assert result["error"] == "Email and password are required"


def test_tc03_missing_password():
    result = login("student@example.com", "")

    assert result["success"] is False
    assert result["error"] == "Email and password are required"


def test_tc04_unregistered_email():
    result = login("wrong@example.com", "password123")

    assert result["success"] is False
    assert result["error"] == "Invalid email or password"


def test_tc05_wrong_password():
    result = login("student@example.com", "wrongpassword")

    assert result["success"] is False
    assert result["error"] == "Invalid email or password"


def test_tc06_incomplete_email_format():
    result = login("student@example", "password123")

    assert result["success"] is False
    assert result["error"] == "Invalid email or password"


    
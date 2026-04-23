from unittest.mock import patch
from app.docker_service import list_containers

@patch("app.docker_service.client.containers.list")
def test_list_containers(mock_list):
    mock_list.return_value = ["container1", "container2"]

    result = list_containers()

    assert len(result) == 2

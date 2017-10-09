from datetime import datetime
from .api_connections import RequestAgentsRawData
from .models import PercentIndividualAndCollectiveAgent
from .models import AmountAgentsRegisteredPerYear
from .models import AmountAgentsRegisteredPerMonth
from .models import PercentAgentsPerAreaOperation
from .models import PercentAgentsForState
from .models import PercentAgentsPerAreaOperationForState
from .models import PercentIndividualAndCollectiveAgentForState

class TestPercentIndividualAndCollectiveAgent(object):

    @staticmethod
    def test_total_agents():
        PercentIndividualAndCollectiveAgent.drop_collection()
        agent_indicator = PercentIndividualAndCollectiveAgent(50,
                datetime.now(), 10, 10)
        agent_indicator.save()
        query = PercentIndividualAndCollectiveAgent.objects.first()
        assert query._total_agents == 50

    @staticmethod
    def test_total_individual_agent():
        PercentIndividualAndCollectiveAgent.drop_collection()
        agent_indicator = PercentIndividualAndCollectiveAgent(50,
                datetime.now(), 10, 10)
        agent_indicator.save()
        query = PercentIndividualAndCollectiveAgent.objects.first()
        assert query._total_agents == 10

    @staticmethod
    def test_total_collective_agent():
        PercentIndividualAndCollectiveAgent.drop_collection()
        agent_indicator = PercentIndividualAndCollectiveAgent(50,
                datetime.now(), 10, 10)
        agent_indicator.save()
        query = PercentIndividualAndCollectiveAgent.objects.first()
        assert query._total_agents == 10

def test_success_request():
    current_time = datetime.now().__str__()
    request_agents_raw_data = RequestAgentsRawData(current_time)
    response_agents_raw_data = request_agents_raw_data.response
    response_status_code = response_agents_raw_data.status_code
    assert response_status_code == 200


def test_data_content():
    current_time = datetime.now().__str__()
    request_agents_raw_data = RequestAgentsRawData(current_time)
    agents_raw_data = request_agents_raw_data.data
    type_agents_raw_data = type(agents_raw_data)
    empty_list = []
    assert type_agents_raw_data == type(empty_list)


def test_data_lenght():
    current_time = datetime.now().__str__()
    request_agents_raw_data = RequestAgentsRawData(current_time)
    agents_raw_data = request_agents_raw_data.data_length
    type_agents_raw_data = type(agents_raw_data)
    integer = 1
    assert type_agents_raw_data == type(integer)

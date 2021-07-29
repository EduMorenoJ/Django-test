import json
import pytest

from works_app.models import Work
from works_app.management.commands.load_work_data import Command
from django.db import IntegrityError, DataError

from works_app.test.parametrize_test_cases import create_work_list_test_cases

pytestmark = pytest.mark.django_db

class TestWork:
    @pytest.mark.parametrize(
        argnames='test_case',
        argvalues=create_work_list_test_cases.values(),
        ids=create_work_list_test_cases.keys()     
    )
    def test_work_create(self, test_case, request):
        if request.node.callspec.id in ['correct_parameters']:
            for work in test_case:
                    Work.objects.create(**work)
            assert Work.objects.count() == 2

        elif request.node.callspec.id == 'no_list_on_parameters':
            with pytest.raises(DataError):
                Work.objects.create(**test_case)

        elif request.node.callspec.id == 'repeted_iswc':
            with pytest.raises(IntegrityError):
                for work in test_case:
                    Work.objects.create(**work)


class TestWorkEndpoints:
    def test_get_all_elements(self, api_client):
        for work in create_work_list_test_cases['correct_parameters']:
            Work.objects.create(
                **work
            )
        response = api_client().get(
            '/api/works/'
        )
        assert response.status_code == 200
        assert len(response.json()) == 2


    def test_get_one_element(self, api_client):
        Work.objects.create(
            title='Viento', contributors=['Vacchi'], iswc='rickinillo'
        )
        response = api_client().get(
            '/api/works/rickinillo/'
        )
        assert response.status_code == 200
        assert response.json()['title'] == 'Viento'
        assert response.json()['contributors'] == ['Vacchi']
        assert response.json()['iswc'] == 'rickinillo'

    def test_get_one_element_with_query(self, api_client):
        Work.objects.create(
            title='I don\t mean a thing', 
            contributors=['Tonny Bennet', 'Lady Gaga'], 
            iswc='rickinillo'
        )
        response = api_client().get(
            '/api/works/rickinillo/?query={contributors}'
        )
        assert response.status_code == 200
        assert response.json()['contributors'] == ['Tonny Bennet', 'Lady Gaga']
        assert response.json().keys() not in ['title','iswc']

class TestCommand:

    command = Command()
    def test_command_handle(self,mocker,mocked_data_formated):
        mocker.patch(
            'works_app.management.commands.load_work_data.group_by_title_and_iswc_and_remove_duplicates',
            return_value=mocked_data_formated
        )
        create_mocked = mocker.patch('works_app.management.commands.load_work_data.Work.objects.create')

        self.command.handle(path='mocked_path')

        for row in mocked_data_formated:
            print(row)
            create_mocked.assert_called_with(
                    title=row['title'],
                    contributors=row['contributors'],
                    iswc=row['iswc'])
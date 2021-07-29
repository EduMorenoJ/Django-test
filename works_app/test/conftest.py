import pytest
from rest_framework.test import APIClient
import pandas as pd
from unittest.mock import MagicMock


@pytest.fixture
def api_client():
   return APIClient


@pytest.fixture
def mocked_data_formated():
    return [
        {
            'title':'Jindama',
            'contributors':['Marea'],
            'iswc':'grbugw'
        }
    ]


@pytest.fixture
def work_object_create_side_effect(**kwargs) -> MagicMock:
    instance = MagicMock()
    instance.title = kwargs['title']
    instance.contributors = kwargs['contributors']
    instance.iswc = kwargs['iswc']
    return instance


@pytest.fixture
def mocked_df():
    return  pd.DataFrame({'title':[
                            'Shape of You',
                            'Adventure of a Lifetime',
                            'Adventure of a Lifetime',
                            'Me Enamoré',
                            'Je ne sais pas',
                            'Je ne sais pas',
                        ],
                        'contributors':[
                            'Edward Christopher Sheeran',
                            'O Brien Edward John|Yorke Thomas Edward|Greenwood Colin Charles',
                            'O Brien Edward John|Selway Philip James',
                            'Rayo Gibo Antonio|Ripoll Shakira Isabel Mebarak',
                            'Obispo Pascal Michel|Florence Lionel Jacques',
                            'Obispo Pascal Michel|Florence Lionel Jacques',
                        ],
                        'iswc':[
                            'T9204649558',
                            'T0101974597',
                            'T0101974597',
                            'T9214745718',
                            None,
                            'T0046951705',
                        ]
                    })
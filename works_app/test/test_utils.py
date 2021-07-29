from works_app.utils import group_by_title_and_iswc_and_remove_duplicates

class TestUtils:
    def test_group_by_title_and_iswc_and_remove_duplicates(self, mocker, mocked_df):
        mocker.patch('works_app.utils.pd.read_csv', return_value=mocked_df)

        results = group_by_title_and_iswc_and_remove_duplicates('path_to_file_mocked')
        
        iswcs = []
        for result in results:
            iswcs.append(result['iswc'])
            assert len(result['contributors']) == len(set(result['contributors']))
        assert len(iswcs) == len(set(iswcs))
        
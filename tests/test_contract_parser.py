from fastapi.testclient import TestClient

from parsers.contracts import ContractsParser


def test_contract_parser_class(client: TestClient):
    parser = ContractsParser(
        contracts=[{"title": "test_pdf.pdf", "path": "tests/test_pdf.pdf"}]
    )
    parsed_contract = parser.parse_contracts()
    assert parsed_contract == [
        {
            'date': '2021-07-01',
            'snippet': 'It was autumn. 1st of July, 2021. ',
            'contract': 'test_pdf.pdf'
        },
        {
            'date': '2022-10-11',
            'snippet': 'This sentence contains full date in normal '
                       'format – 10/11/2022 ',
            'contract': 'test_pdf.pdf'},
        {
            'date': '2022-11-10',
            'snippet': 'What about other formats, let’s say USA… 2022/11/10 ',
            'contract': 'test_pdf.pdf'
        },
        {
            'date': '2022-06-22',
            'snippet': 'It should recognize this as well 22 June 2022. ',
            'contract': 'test_pdf.pdf'
        },
        {
            'date': '2022-02-24',
            'snippet': 'Russia is the fucking country, confirmed on'
                       ' 24th of February, 2022 ',
            'contract': 'test_pdf.pdf'
        }
    ]

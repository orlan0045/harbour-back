from typing import List

import pdfplumber
import datefinder


class ContractsParser:
    """
    Parser class to get all the possible dates from the contracts list
    The order of functions to run is from the bottom to top
    """
    def __init__(self, contracts: List[dict]):
        self.contracts = contracts
        self.contract_in_progress = None

    def _find_dates_with_snippets(self, line) -> List[dict]:
        """
        The last called function in the class. Doing all the dirty job calling
        datefinder lib to parse dates.
        :return: list of dicts with found date,
         text snippet (a.k.a. line of text), contract name to render on UI
        """
        found_dates = datefinder.find_dates(line, strict=True)
        found_dates_with_snippets = []
        for date in found_dates:
            found_dates_with_snippets.append(
                {
                    'date': date.strftime("%Y-%m-%d"),
                    'snippet': line,
                    'contract': self.contract_in_progress['title']
                }
            )
        return found_dates_with_snippets

    def _parse_page(self, page):
        """
        Splitting page into lines, so we could get text snippets easily
        """
        text_as_lines = page.extract_text().splitlines()
        parsed_page_dates = []
        for line in text_as_lines:
            parsed_page_dates.extend(self._find_dates_with_snippets(line))
        return parsed_page_dates

    def _parse_pages(self, contract) -> List[dict]:
        parsed_contract_dates = []
        for page in contract.pages:
            parsed_contract_dates.extend(self._parse_page(page))
        return parsed_contract_dates

    def _parse_contract(self) -> List[dict]:
        """
        opening pdf via path and passing PDF class object to parse pages
        """
        with pdfplumber.open(self.contract_in_progress['path']) as pdf:
            return self._parse_pages(pdf)

    def parse_contracts(self) -> List[dict]:
        """
        Main function. Everything starts here
        Iterating through the list of contracts and calling subfunction
        :return:
        """
        parsed_contracts = []
        for contract in self.contracts:
            self.contract_in_progress = contract
            parsed_contracts.extend(self._parse_contract())
        return parsed_contracts

from typing import List
from pathlib import Path

import aiofiles
from fastapi import UploadFile


async def save_single_contract(file: UploadFile, directory: Path) -> dict:
    """
    Single contract saving function. Separated logic in order to keep
    readability
    :return: dict with title and saved path
    """
    file_location = f'{directory}/{file.filename}'
    async with aiofiles.open(file_location, 'wb') as saved_file:
        content = await file.read()
        await saved_file.write(content)
        saved_contract_data = {'title': file.filename, 'path': file_location}
    return saved_contract_data


async def save_contracts(files: List[UploadFile]) -> List[dict]:
    """
    Helper function to control saving contracts.
    :return:
    """
    file_directory = Path('contracts')
    saved_contracts_data = []
    if not file_directory.is_dir():
        file_directory.mkdir()
    for file in files:
        saved_contract_data = await save_single_contract(file, file_directory)
        saved_contracts_data.append(saved_contract_data)
    return saved_contracts_data

from typing import List

from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

from parsers.contracts import ContractsParser
from helpers import save_contracts

app = FastAPI()
app.mount(
    "/contracts-files", StaticFiles(directory="contracts"), name="contracts"
)

origins = [
    "https://harbour-front-cpjco.ondigitalocean.app",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/contracts")
async def contracts(files: List[UploadFile]):
    """
    HTTP POST endpoint to accept and parse contracts.
    :param files: list of files
    :return: JsonResponse
    """
    saved_contracts_data = await save_contracts(files)
    parsed_contracts = ContractsParser(
        contracts=saved_contracts_data
    ).parse_contracts()
    return JSONResponse({
        "contracts": saved_contracts_data,
        "contracts_dates": parsed_contracts
    })


@app.get("/")
async def root():
    return JSONResponse({'detail': 'health-check'})

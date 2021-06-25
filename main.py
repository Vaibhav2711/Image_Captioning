from caption import image_cap
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class ImageInput(BaseModel):
	imagepath : str

class CaptionOut(BaseModel):
	caption: str


@app.post("/caption",response_model = CaptionOut)

async def image_Caption(payload: ImageInput):

	imagepath = payload.imagepath
	final_caption = image_cap(imagepath)
	responseObj = {"caption": final_caption}
	return responseObj
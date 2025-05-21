from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse # Permite retornar respostas personalizadas em formato JSON, inclusive com códigos de erro HTTP
from extractor.pdf_reader import extract_text_from_pdf
from extractor.text_clear import text_clear
from io import BytesIO

app = FastAPI()

@app.post("/processar-pdf/")
async def processar_pdf(file: UploadFile = File(...)):
    try:
         contents = await file.read()
         text = extract_text_from_pdf(BytesIO(contents))
         cleaned_text = text_clear(text)
         return {"texto_limpo": cleaned_text}
    except Exception as e:
         return JSONResponse(status_code=500, content={"erro": str(e)})
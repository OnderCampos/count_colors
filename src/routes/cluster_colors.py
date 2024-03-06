from fastapi import File, UploadFile
from PIL import Image
from fastapi import APIRouter
from src.utils.general import extract_colors, extract_colors2, extract_colors3, meanShift, affinityPropagation
import io

router = APIRouter()

@router.post(
    "/cluster_colors",
    description="Cluster an image in colors"
)
async def cluster_colors(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        #return {"size": str(image.size)}

        colors = extract_colors2(image)
        

        return {"colors": colors.tolist(), "len": len(colors)}
    
    except Exception as e:
        return {"error": str(e)}
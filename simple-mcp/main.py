# TODO: Task 2.1 - Import FastAPI
from fastapi import FastAPI, HTTPException
from models import ModelContextRequest, ModelContextResponse
from tools import GET_WEATHER_TOOL, get_weather

app = FastAPI()

tool_registry = {
    "get_weather": get_weather,
}

@app.post("/mcp")
def handle_mcp_request(request: ModelContextRequest):
    if request.verb == "discovery":
        return ModelContextResponse(tools=[GET_WEATHER_TOOL])
    elif request.verb == "execute":
        try:
            function = tool_registry[request.tool_name]
            result = function(**request.arguments)
            return ModelContextResponse(result=result)
        except KeyError:
            raise HTTPException(status_code=404, detail=f"Tool '{request.tool_name}' not found.")

    pass
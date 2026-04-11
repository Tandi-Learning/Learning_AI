from models import Tool, ToolParameter


def get_weather(location: str) -> str:
	"""Return a simple weather message for a given location."""
	return f"The weather in {location} is sunny, 25C."


GET_WEATHER_TOOL = Tool(
	name="get_weather",
	description="Gets the current weather for a specified location.",
	parameters=[
		ToolParameter(name="location", type="string")
	],
)

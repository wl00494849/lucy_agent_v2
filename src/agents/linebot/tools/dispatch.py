dockerd = {
  "name": "dockerd",
  "description": "docker proxy api",
  "inputSchema": {
    "type": "object",
    "properties": {
      "cmd": {
        "type": "string",
        "description": (
            "Docker operation to perform : "
            "'containers' cans get containers list; "
            "'images' can get images list; "
            "'start' starts as container; "
            "'stop' stops a container"
        ),
        "enum": [
          "containers",
          "images",
          "start",
          "stop"
        ]
      }
    },
    "required": ["cmd"],
    "additionalProperties": False
  }
}
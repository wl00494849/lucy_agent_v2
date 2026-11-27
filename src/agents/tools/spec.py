dockerd_info = {
  "name": "dockerd_info",
  "description": "dockerd get information api",
  "inputSchema": {
    "type": "object",
    "properties": {
      "cmd": {
        "type": "string",
        "description": (
            "Docker operation to perform : "
            "'containers':cans get containers list; "
            "'images':can get images list; "
        ),
        "enum": [
          "containers",
          "images",
        ]
      }
    },
    "required": ["cmd"],
    "additionalProperties": False
  }
}

dockerd_exec = {
  "name": "dockerd_exec",
  "description": "dockerd exec api",
  "inputSchema": {
    "type": "object",
    "properties": {
      "cmd": {
        "type": "string",
        "description": (
            "Docker operation to perform : "
            "'start': starts as container; "
            "'stop':stops a container"
        ),
        "enum": [
          "start",
          "stop"
        ]
      },
      "id":{
        "type":"string",
        "description":"Docker image id"
      }
    },
    "required": ["cmd","id"],
    "additionalProperties": False
  }
}

TOOL = [
    dockerd_info,
    dockerd_exec
]
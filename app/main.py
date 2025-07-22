import anyio
from claude_code_sdk import query, ClaudeCodeOptions, Message

async def main():
    messages: list[Message] = []
    while True:
        try:
            prompt = input(">")
            async for message in query(
                prompt=prompt,
                options=ClaudeCodeOptions(
                    allowed_tools=["Read", "Write", "Bash"],
                    max_turns=3,
                )
            ):
                messages.append(message)

            print(messages[-1].result)
        except KeyboardInterrupt as ex:
            print("Good bye!!")
            return
        
        

anyio.run(main)
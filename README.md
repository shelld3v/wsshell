## WebSocket Remote Shell

Wow, you can do a shell upload, how cool is that! And, the best way to enjoy the code execution is by gaining a shell from your computer. But, WAF, it sucks! It can't connect to the outside world. Here, it is, the solution!

## So, what actually is this?

You have probably heard about reverse shell, or bind shell, or webshell, right? This is the same, got it? But, what is the difference? Well, there is nothing different here, except that this shell uses WebSocket, as the protocol! There are many types of bind/reverse shell, like UDCP, HTTP, basic TCP, ... And this, a new type, that I made to fit the diversity of this world!

## But your shell sucks, even more than the WAF, why don't use bind shell!

This is a really unique way to run a shell, that's what I want! Also, this shell has an encrypted connection, how can be better! And, this shell requires you to have a WebSocket client, if don't, it won't work, like a door to prevent others from accessing your shell! Server admin can't know what did you do! (actually can). And feel free to get out of this project if you don't like it.

## How to play

- Upload the shell: *wsshell.py*
- Execute the shell: `$ ./wsshell.py`
- Done, use it at port 4242, by playing with wscat or websocat! Or, you can use this [awesome Chrome extension](https://chrome.google.com/webstore/detail/simple-websocket-client/pfdhoblngboilpfeibdedpjgfnlcodoo)

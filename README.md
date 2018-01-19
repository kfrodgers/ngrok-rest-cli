# ngrok-rest-cli
Simple ngrok cli commands that use ngrok's REST API (https://ngrok.com/docs#client-api). Allows users to
dynamically create or destroy tunnels without having to restart the ngrok client.

Tip, ngrok can be run in the background by redirecting standard out. I typically use
```
$ ngrok authtoken <auth token>     # optional and only needed once
$ (ngrok start --none | cat) &
```
and then use the cli commands to start and stop tunnels.

### Install

```bash
$ git clone https://github.com/kfrodgers/ngrok-rest-cli
$ pip install ./ngrok-rest-cli
```

To uninstall run 'pip uninstall ngrok_rest_cli'.

### Usage

```bash
ngrok_get [-n <name>] [-m]

ngrok_start -n <name> [-h <local_addr>] [-p <port>] [-P <protocol>] [-r <remote_addr>]

ngrok_stop -n <name>

ngrok_requests
```

Note the default port is 80 and the only supported protocols are tcp and http with the latter being the default.

### Licensing

Copyright (c) [2018], [Kevin Rodgers]
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


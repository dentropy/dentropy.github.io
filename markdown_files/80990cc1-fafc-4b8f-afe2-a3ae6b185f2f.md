---
share: true
uuid: 80990cc1-fafc-4b8f-afe2-a3ae6b185f2f
title: Code Server
---
## Install

[wiki.software.list.vscode.Extensions](/undefined)

## THE ONE IMMEDIATELY BELOW WORKS

``` bash
sudo apt-get -y update
sudo apt-get -y install tmux git
tmux new -s code-server

bash <(curl -s curl https://gist.githubusercontent.com/dentropy/8c44825e9c81cae54c8ae0af74e242cd/raw/ee9208e1e23f3639859c4860927b22808a721c1d/code-server.sh)

code-server --disable-telemetry --cert --auth password --bind-addr 0.0.0.0:8082

cat ~/.config/code-server/config.yaml
```

## Manual Install

```  bash
tmux new -s code-server
curl -fsSL https://code-server.dev/install.sh | sh

# RERUN FROM THIS LINE AFTER REBOOT

# NOTE PASSWORD
rm ~/run-code-sever.sh
echo '#!/bin/bash\ncode-server --disable-telemetry --cert --auth password --bind-addr 0.0.0.0:8082' >> ~/run-code-sever.sh
chmod +x ~/run-code-sever.sh
bash ~/run-code-sever.sh
#  code-server --disable-telemetry --cert --auth password  --bind-addr 0.0.0.0:8082
```
## Script Install

``` bash
#!/bin/bash
curl -fsSL https://code-server.dev/install.sh | sh -s -- --dry-run > ~/code-server-install.txt
curl -fsSL https://code-server.dev/install.sh | sh
echo -e "export PASSWORD=\`tr -cd '[:alnum:]' < /dev/urandom | fold -w31 | head -n1\`" > ~/run-code-sever.sh
echo -e "PASSWORD=\$PASSWORD" >> ~/run-code-sever.sh
echo -e "echo 'Password posted below'" >> ~/run-code-sever.sh
echo -e "echo \$PASSWORD" >> ~/run-code-sever.sh
echo "code-server --disable-telemetry --cert --auth password --bind-addr 0.0.0.0:8082" >> ~/run-code-sever.sh
chmod +x ~/run-code-sever.sh
cat ~/run-code-sever.sh
~/run-code-sever.sh
```

## Review the code below and delete

``` bash
cat <<EOF > ~/run-code-sever.sh
#!/bin/bash
# run-code-sever.sh
set -x
echo -e "export PASSWORD=\`tr -cd '[:alnum:]' < /dev/urandom | fold -w31 | head -n1\`" > ~/run-code-sever.sh

echo "Password = $PASSWORD"
code-server --disable-telemetry --cert --auth password --bind-addr 0.0.0.0:8082

printf "%s\nexport PASSWORD=`tr -cd '[:alnum:]' < /dev/urandom | fold -w31 | head -n1`" -e > ~/run-code-sever.sh
echo "\"Password = $PASSWORD\"" >> ~/code-server-password.txt
echo "code-server --disable-telemetry --cert --auth password --bind-addr 0.0.0.0:8082" >> ~/run-code-sever.sh
chmod +x ~/run-code-sever.sh
EOF
chmod +x ~/run-code-sever.sh
bash ~/run-code-sever.sh
```

## Commands

``` bash
# get password
cat ~/.config/code-server/config.yaml

# Change port
code-server --disable-telemetry --cert --bind-addr 0.0.0.0:8082
```

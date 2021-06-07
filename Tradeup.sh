# shellcheck disable=SC1073
while true; do
  python3 DiscordBot.py &
  python3 MainSt.py
  python3 MainCL.py
  python3 Main.py
  pkill python3
  sleep 2m
done
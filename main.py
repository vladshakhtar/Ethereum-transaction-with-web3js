from encodings import utf_8
from web3 import Web3

ganache_url = 'https://ropsten.infura.io/v3/a2fdd2de9c86497eafcc20310318e5c3'
web3 = Web3(Web3.HTTPProvider(ganache_url))
account_1 = '0xb194719b2A9b38a560797C5a9BA1d9c8A57bFCBe'
private_key1 ='48e345d4f9afff3f9661a3981867e79292e1c061152bcad58f2169f04fa8b3ec'
account_2 = '0xc53D6C0148ddC28Efe623Ab3aD54da5C7779b25C'
nonce = web3.eth.getTransactionCount(account_1)
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(0.01, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
    'data': bytes("Stoliarov Vladyslav", "utf_8")
}
signed_tx = web3.eth.account.sign_transaction(tx, private_key1)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
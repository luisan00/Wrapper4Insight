#!/usr/bin/env python3.4

# A simple Python wrapper for insight.
# This software is under a MIT license,
# see LICENSE file for more information.
# (c) 2015-2017 luisan00

from collections import OrderedDict
import httplib
import json
from config import host, port

# routes
route = {
         'status': {
                    'getInfo': '/insight-api/status?q=getInfo',
                    'getDifficulty': '/insight-api/status?q=getDifficulty',
                    'getBestBlockHash': '/insight-api/status?q=getBestBlockHash',
                    'getLastBlockHash': '/insight-api/status?q=getLastBlockHash'
                    },
         'sync' : '/insight-api/sync',
         'peer' : '/insight-api/peer',
         'tx' : '/insight-api/tx/%s',
         'block' : '/insight-api/block/%s',
         'address': '/insight-api/addr/%s'
         }

# messages

msg = {
            '-1': 'error, connecting to server: %s:%s',
            '-2' : 'error, transsaction: <%s> not found',
            '-3' : 'error, block: <%s> not found',
            '-4' : 'error, address: <%s> not found'
            }

class insight(object):
			
	def __init__(self, _insight__host, _insight__port):
		self.host = __host
		self.port = __port
		self.connection = httplib.HTTPConnection(self.host, self.port)
		
	# Return various status messages.
	
	def status(self, args):
		try:
			self.connection.request('GET', route['status'][args])
		except:
			return (msg['-1'] % (host, port)
		response = self.connection.getresponse()
		return response.read()
		
	# Return sync. info.	
	def sync(self):
		try:
			self.connection.request('GET', route['sync'])
		except:
			return (msg['-1'] % (host, port)
		response = self.connection.getresponse()
		return response.read()
		
	# Return peer info.
	def peer(self):
		try:
			self.connection.request('GET', route['peer'])
		except:
			return (msg['-1'] % (host, port)
		response = self.connection.getresponse()
		return response.read()
		
	# Return tx by txid if exist.
	def tx(self,txid):
		try:
			self.connection.request('GET', route['tx'] % txid)
		except:
			return (msg['-1'] % (host, port)
		response = self.connection.getresponse()
		try: 
			data = response.read()
			this = json.loads(data, object_pairs_hook=OrderedDict)
			return json.dumps(this, indent=4)
		except:
			return (msg['-2'] % txid)
			
	# Return a block by hash if exist.	
	def block(self,block):
		try:
			self.connection.request('GET', route['block'] % block)
		except:
			return (msg['-1'] % (host, port)
		response = self.connection.getresponse()
		try: 
			data = response.read()
			this = json.loads(data, object_pairs_hook=OrderedDict)
			return json.dumps(this, indent=4)
		except:
			return (msg['-3'] % block)
			
	# Return address properties if exist.
	def address(self, addr):
		try:
			self.connection.request('GET', route['address'] % addr)
		except:
			return (msg['-1'] % (host, port)
		response = self.connection.getresponse()
		try: 
			data = response.read()
			this = json.loads(data, object_pairs_hook=OrderedDict)
			return json.dump(this, indent=4)
		except:
			return (msg['-4'] % addr)
			
# Examples.
#
# first create the object in the variable explorer.
# >> explorer = insight(host, port)
#
# you can call the function status, peer, sync, block(byHash), tx(byTxId), address(address)
#
# function status require a param: 'getInfo', 'getDifficulty', 'getBestBlockHash' or getLastBlockHash
# >> bestBlockHash = explorer.status('getBestBlockHash')
# 
# peer, or sync no need options
# >> peer = explorer.peer()
# or
# >> sync = explorer.sync()
#
# 
# >> block = explorer.block('hash_of_the_block')
# or
# >> tx = explorer.tx('tx_id')
# or
# >> address = explorer.address('address_to_search')          

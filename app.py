# A simple Python wrapper for insight.
#
# See %repository% repository for a detailed information.
#
# This software is under a MIT license,
# see LICENSE file for more information.
# (c) 2015 luisan00

from collections import OrderedDict
import httplib
import json
from config import host, port

# routes
route = {'sync' : '/api/sync',
         'peer' : '/api/peer',
         'tx' : '/api/tx/%s',
         'block' : '/api/block/%s'
         }


class insight(object):
			
	def __init__(self, _insight__host, _insight__port):
		self.host = __host
		self.port = __port
		self.connection = httplib.HTTPConnection(self.host, self.port)
		
	# Return sync. status 	
	def sync(self):
		try:
			self.connection.request('GET', route['sync'])
		except:
			return ('error[-1] connecting to server')
		response = self.connection.getresponse()
		return response.read()
		
	# Return peer estatus	
	def peer(self):
		try:
			self.connection.request('GET', route['peer'])
		except:
			return ('error[-1] connecting to server')
		response = self.connection.getresponse()
		return response.read()
		
	# Return tx by txid if exist.
	def tx(self,txid):
		try:
			self.connection.request('GET', route['tx'] % txid)
		except:
			return ('error[-1] connecting to server')
		response = self.connection.getresponse()
		try: 
			data = response.read()
			this = json.loads(data, object_pairs_hook=OrderedDict)
			return json.dumps(this, indent=4)
		except:
			return ('error[0] tx: <%s> not found'% txid)
			
	# Return a block by hash if exist		
	def block(self,block):
		try:
			self.connection.request('GET', route['block'] % block)
		except:
			return ('error[-1] connecting to server')
		response = self.connection.getresponse()
		try: 
			data = response.read()
			this = json.loads(data, object_pairs_hook=OrderedDict)
			return json.dumps(this, indent=4)
		except:
			return ('error[0] block: <%s> not found'% block)
			
# Examples.
# first create the object in the variable explorer.
# >> explorer = insight(host, port)
# later can call the function peer, sync, getBlock(byHash), getTx(byTxId)
# >> peer = explorer.peer()
# or
# >> sync = explorer.sync()
# or
# >> block = block('hash_of_the_block')
# or
# tx = explorer.tx('tx_id')              

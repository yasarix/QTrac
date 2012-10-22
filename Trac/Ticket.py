'''
Created on Oct 21, 2012

@author: yasar
'''
import xmlrpclib

class Ticket(object):
	trac_server = None
	connection = None
	
	def __init__(self, trac_server):
		self.trac_server = trac_server
		self.connection = trac_server.connection
	
	def listTickets(self, criteria):
		multicall = xmlrpclib.MultiCall(self.connection)
		for ticket_id in self.connection.ticket.query("status!=closed"):
			multicall.ticket.get(ticket_id)
		
		for ticket in multicall():
			print str(ticket)

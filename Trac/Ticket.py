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
		if len(criteria) == 0:
			criteria = "status!=closed"
		
		multicall = xmlrpclib.MultiCall(self.connection)
		for ticket_id in self.connection.ticket.query(criteria):
			multicall.ticket.get(ticket_id)
		
		ticket_list = []
		for ticket in multicall():
			ticket_list.append(ticket)
			
		return ticket_list

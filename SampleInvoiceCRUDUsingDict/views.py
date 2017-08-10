from django.shortcuts import render
from mysite.utils import context
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from .invoice_crud import createInvoice, readInvoice, queryInvoice, deleteInvoice, updateInvoice

def index(request):
    return render(request, 'invoiceUsingDict.html')

def create(request):
    reqContext = contextHelper(request)
    response = createInvoice(reqContext)
    return HttpResponse(str(response['Invoice']))

def update(request):
    # query to get an existing invoice id
    reqContext = contextHelper(request)
    query = queryInvoice('select * from invoice startposition 0 maxresults 5', reqContext)
    if not isinstance(query, str) and len(query) > 0:
        invoice = query[0]
        response = updateInvoice(invoice['Id'], reqContext)
        message = str(response['Invoice'])
    elif isinstance(query, str):
        message = query
    else:
        message = 'Unable to find existing invoice to update. Please add an invoice and try again.'
    return HttpResponse(message)

def read(request):
    # query to get an existing invoice id
    reqContext = contextHelper(request)
    query = queryInvoice('select * from invoice startposition 0 maxresults 5', reqContext)
    if not isinstance(query, str) and len(query) > 0:
        invoice = query[0]
        response = readInvoice(invoice['Id'], reqContext)
        message = str(response)
    elif isinstance(query, str):
        message = query
    else:
        message = 'Unable to find existing invoice to read. Please add an invoice and try again.'
    return HttpResponse(message)

def delete(request):
    # query to get an existing invoice id
    reqContext = contextHelper(request)
    query = queryInvoice('select * from invoice startposition 0 maxresults 5', reqContext)
    if not isinstance(query, str) and len(query) > 0:
        invoice = query[0]
        response = deleteInvoice(invoice['Id'], reqContext)
        message = str(response['Invoice'])
    elif isinstance(query, str):
        message = query
    else:
        message = 'Unable to find existing invoice to delete. Please add an invoice and try again.'
    return HttpResponse(message)

def query(request):
    reqContext = contextHelper(request)
    response = queryInvoice('select * from invoice startposition 0 maxresults 5', reqContext)
    return HttpResponse(response)

def contextHelper(request):
    reqContext = context.Context(access_token=request.session.get('access_token'),access_token_secret=request.session.get('access_token_secret'), realm_id=request.session.get('realm_id'))
    return reqContext  


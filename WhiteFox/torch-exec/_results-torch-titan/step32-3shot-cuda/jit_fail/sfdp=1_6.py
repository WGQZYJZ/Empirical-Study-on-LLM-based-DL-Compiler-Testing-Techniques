import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg



class Model(torch.nn.Module):

    def __init__(self, dropout_p=0.0):
        super().__init__()
        self.dropout_p = dropout_p

    def forward(self, query, key, value, attn_mask):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        qk = torch.nn.functional.dropout(qk, self.dropout_p)
        qk = qk.softmax()
        dropout_qk = torch.matmul(value, qk)
        return dropout_qk



func = Model(dropout_p=0.5).to('cuda')



query = torch.randn(1, 8, 64)



key = torch.randn(1, 8, 64)



value = torch.randn(1, 8, 64)



attn_mask = torch.randn(1, 1, 64)


test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
softmax() received an invalid combination of arguments - got (), but expected one of:
 * (int dim, torch.dtype dtype)
 * (name dim, *, torch.dtype dtype)


jit:
Failed running call_method softmax(*(FakeTensor(..., device='cuda:0', size=(1, 8, 8)),), **{}):
softmax() received an invalid combination of arguments - got (), but expected one of:
 * (int dim, torch.dtype dtype)
 * (name dim, *, torch.dtype dtype)


from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
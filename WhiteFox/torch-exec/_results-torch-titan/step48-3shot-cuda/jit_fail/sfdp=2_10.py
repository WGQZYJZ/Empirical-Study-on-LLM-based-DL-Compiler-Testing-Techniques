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

    def __init__(self):
        super().__init__()

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(5, 8, 128)



key = torch.randn(5, 8, 128)



value = torch.randn(6, 8, 128)



inv_scale_factor = torch.randn(6, 8, 8)

dropout_p = 1

test_inputs = [query, key, value, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (5) must match the size of tensor b (6) at non-singleton dimension 0

jit:
Failed running call_method div(*(FakeTensor(..., device='cuda:0', size=(5, 8, 8)), FakeTensor(..., device='cuda:0', size=(6, 8, 8))), **{}):
Attempting to broadcast a dimension of length 6 at -3! Mismatching argument at index 1 had torch.Size([6, 8, 8]); but expected shape should be broadcastable to [5, 8, 8]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def forward(self, query, key, value, scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = softmax(scaled_qk, dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(8, 12, 768)



key = torch.randn(8, 12, 768)



value = torch.randn(8, 12, 768)



scale_factor = torch.randn(8)





dropout_p = torch.nn.Parameter(torch.full((1,), 0.5, dtype=torch.float32))


test_inputs = [query, key, value, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (12) must match the size of tensor b (8) at non-singleton dimension 2

jit:
Failed running call_method mul(*(FakeTensor(..., device='cuda:0', size=(8, 12, 12)), FakeTensor(..., device='cuda:0', size=(8,))), **{}):
Attempting to broadcast a dimension of length 8 at -1! Mismatching argument at index 1 had torch.Size([8]); but expected shape should be broadcastable to [8, 12, 12]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def forward(self, q, k, v, inv_scale_factor, dropout_p):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        _v = torch.nn.functional.dropout(scaled_qk.softmax(dim=(- 1)), p=dropout_p).matmul(v)
        v = v.unsqueeze(1)
        _v = _v.unsqueeze(2)
        sum_vv = torch.sum(torch.multiply(v, _v), dim=(- 1))
        z = torch.sum(torch.multiply(sum_vv, torch.exp((qk / 0.7)).div(inv_scale_factor)), dim=(- 1))
        return (z, qk)



func = Model().to('cuda')



q = torch.randn(1, 8, 5, 5)



k = torch.randn(1, 8, 5, 5)



v = torch.randn(1, 8, 5, 5)

inv_scale_factor = 1
dropout_p = 1

test_inputs = [q, k, v, inv_scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (5) at non-singleton dimension 2

jit:
Failed running call_function <built-in method multiply of type object at 0x7cbefd2699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 8, 5)), FakeTensor(..., device='cuda:0', size=(1, 8, 5, 5))), **{}):
Attempting to broadcast a dimension of length 5 at -2! Mismatching argument at index 1 had torch.Size([1, 8, 5, 5]); but expected shape should be broadcastable to [1, 8, 8, 5]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
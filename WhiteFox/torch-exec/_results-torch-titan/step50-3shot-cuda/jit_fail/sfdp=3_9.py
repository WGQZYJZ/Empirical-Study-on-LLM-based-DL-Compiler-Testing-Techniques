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

    def __init__(self, scale_factor=(1 / (10.0 ** 0.5)), dropout_p=0.1):
        super().__init__()
        self.scale_factor = scale_factor
        self.dropout_p = dropout_p

    def forward(self, query, key, value):
        qk = query.matmul(key.transpose((- 2), (- 1)))
        scaled_qk = (qk * self.scale_factor)
        return (scaled_qk.softmax(dim=(- 1)) * torch.nn.functional.dropout(scaled_qk, p=self.dropout_p).matmul(value))



func = Model().to('cuda')



query = torch.randn(1, 6, 20)



key = torch.randn(1, 8, 20)



value = torch.randn(1, 8, 16)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (16) at non-singleton dimension 2

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 6, 8)), FakeTensor(..., device='cuda:0', size=(1, 6, 16))), **{}):
Attempting to broadcast a dimension of length 16 at -1! Mismatching argument at index 1 had torch.Size([1, 6, 16]); but expected shape should be broadcastable to [1, 6, 8]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
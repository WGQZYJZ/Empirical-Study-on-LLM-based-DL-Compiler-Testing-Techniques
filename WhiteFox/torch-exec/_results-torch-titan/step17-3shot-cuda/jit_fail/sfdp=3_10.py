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
        self.scale_factor = torch.nn.Parameter(torch.ones(1, 1))

    def forward(self, query, key, value, scale_factor=None, dropout_p=0.5):
        scale_factor = (self.scale_factor if (scale_factor is None) else scale_factor)
        shape = []
        for tensor in (query, key, value, scale_factor):
            new_shape = ([1] * len(tensor.size()))
            new_shape[0] = (- 1)
            shape.append(new_shape)
        query = query.view(*shape)
        key = key.view(*shape)
        value = value.view(*shape)
        scale_factor = scale_factor.view(*shape[:(- 1)])
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(scale_factor)
        shape2 = []
        for _ in range((len(tensor.size()) + 1)):
            shape2.append((- 1))
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk.view(*shape2), value.view(*shape2))
        return output



func = Model().to('cuda')



query = torch.randn(1, 64, 128)



key = torch.randn(1, 64, 256)



value = torch.randn(1, 64, 256)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
The size of tensor a (8192) must match the size of tensor b (16384) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x73b9182699e0>(*(FakeTensor(..., device='cuda:0', size=(8192, 1, 1)), FakeTensor(..., device='cuda:0', size=(16384, 1, 1))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 32, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
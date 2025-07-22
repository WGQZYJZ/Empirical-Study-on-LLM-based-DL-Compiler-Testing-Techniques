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

    def forward(self, query, key, value, dropout=0.5, scale_factor=(1 / 8)):
        v1 = torch.matmul(query, key.transpose((- 2), (- 1)))
        v2 = v1.mul(scale_factor)
        v3 = v2.softmax(dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=dropout)
        out = v4.matmul(value)
        return out



func = Model().to('cuda')



query = torch.rand(1, 64, 100)



key = torch.rand(1, 64, 200)



value = torch.rand(1, 64, 200)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 100] but got: [1, 200].

jit:
Failed running call_function <built-in method matmul of type object at 0x78b3a02699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 64, 100)), FakeTensor(..., device='cuda:0', size=(1, 200, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 100] but got: [1, 200].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
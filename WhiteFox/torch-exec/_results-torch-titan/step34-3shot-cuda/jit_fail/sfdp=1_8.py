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

    def forward(self, q, k, v, scale_factor, dropout_p):
        v1 = torch.matmul(q, k.transpose((- 2), (- 1)))
        v2 = v1.div(scale_factor)
        v3 = v2.softmax(dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        v5 = torch.matmul(v4, v)
        return v5



func = Model().to('cuda')



x = torch.randn(1, 1, 1024)



y = torch.randn(1, 1, 1024)

q = 1
k = 1
v = 1

test_inputs = [x, y, q, k, v]

# JIT_FAIL
'''
direct:
matmul(): argument 'other' (position 2) must be Tensor, not int

jit:
Failed running call_function <built-in method matmul of type object at 0x7cbf77c699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 1)), 1), **{}):
matmul(): argument 'other' (position 2) must be Tensor, not int

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
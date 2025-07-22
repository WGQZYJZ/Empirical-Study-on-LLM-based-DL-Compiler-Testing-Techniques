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

    def forward(self, x1, x2, x3, x4, x5, x6, x7, x8, x9):
        qk = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        scaled_qk = qk.div(x3)
        qk = self._softmax(scaled_qk, x4)
        q = torch.nn.functional.dropout(qk, x5)
        o = torch.matmul(q, x6)
        return o

    def _softmax(self, x, dim_size):
        xn = F.softmax(x, dim=(- 1))
        return xn



func = Model().to('cuda')



x1 = torch.randn(12, 64, 512)



x2 = torch.randn(12, 64, 64)



x3 = torch.randn(64)

x4 = 1
x5 = 1
x6 = 1
x7 = 1
x8 = 1
x9 = 1

test_inputs = [x1, x2, x3, x4, x5, x6, x7, x8, x9]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [12, 512] but got: [12, 64].

jit:
Failed running call_function <built-in method matmul of type object at 0x70bcaec699e0>(*(FakeTensor(..., device='cuda:0', size=(12, 64, 512)), FakeTensor(..., device='cuda:0', size=(12, 64, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [12, 512] but got: [12, 64].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
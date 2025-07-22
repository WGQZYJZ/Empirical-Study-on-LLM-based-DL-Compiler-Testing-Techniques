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
        self.head = torch.nn.Linear((80 * 8), (80 * 8))

    def forward(self, x1, x2, x3, x4):
        qkkv = self.head(x1)
        qkkv = qkkv.reshape(1, 24, 80, 8)
        q = qkkv[:, :1, ...]
        k = qkkv[:, 1:2, ...]
        v = qkkv[:, 2:, ...]
        qk = (q @ k.transpose((- 2), (- 1)).matmul((1.0 / math.sqrt(q.size((- 1))))).softmax(dim=(- 1)))
        qkv = (qk @ v)
        return qkv



func = Model().to('cuda')



x1 = torch.randn(1, ((24 * 80) * 8))



x2 = torch.randn(1, ((24 * 80) * 8))



x3 = torch.randn(1, ((24 * 80) * 8))



x4 = torch.randn(1, ((24 * 80) * 8))


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x15360 and 640x640)

jit:
Failed running call_module L__self___head(*(FakeTensor(..., device='cuda:0', size=(1, 15360)),), **{}):
a and b must have same reduction dim, but got [1, 15360] X [640, 640].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
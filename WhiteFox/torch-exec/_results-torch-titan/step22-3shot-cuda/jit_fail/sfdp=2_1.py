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
        self.query = torch.nn.Linear(192, 128)
        self.key = torch.nn.Linear(192, 256)
        self.value = torch.nn.Linear(384, 256)
        self.dropout = torch.nn.Dropout(0.1)

    def forward(self, x1, x2, x3):
        q = self.query(x1)
        k = self.key(x2)
        v = self.value(x3)
        att = (torch.matmul(q, k.transpose((- 2), (- 1))) / math.sqrt(256))
        att = self.dropout(torch.softmax(att, dim=(- 1)))
        return torch.matmul(att, v)



func = Model().to('cuda')



x1 = torch.randn(1, 192)



x2 = torch.randn(4, 384)



x3 = torch.randn(100, 256)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x384 and 192x256)

jit:
Failed running call_module L__self___key(*(FakeTensor(..., device='cuda:0', size=(4, 384)),), **{}):
a and b must have same reduction dim, but got [4, 384] X [192, 256].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
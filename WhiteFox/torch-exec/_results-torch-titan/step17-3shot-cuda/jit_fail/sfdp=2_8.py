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

    def __init__(self, inv_scale_factor):
        super().__init__()
        self.query = torch.nn.Linear(8, 8)
        self.key = torch.nn.Linear(8, 8)
        self.value = torch.nn.Linear(8, 8)
        self.dropout = torch.nn.Dropout(p=0.2)
        self.inv_scale_factor = inv_scale_factor

    def forward(self, x, y):
        q1 = self.query(x)
        k1 = self.key(y)
        v1 = self.value(y)
        q2 = q1.transpose((- 2), (- 1))
        k2 = k1.transpose((- 2), (- 1))
        q3 = q2.div(self.inv_scale_factor)
        q4 = q3.softmax(dim=(- 1))
        d1 = self.dropout(q4)
        o1 = d1.matmul(v1)
        return o1



inv_scale_factor = 1

func = Model(inv_scale_factor).to('cuda')



x = torch.randn(1, 8)



y = torch.randn(2, 8)


test_inputs = [x, y]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x1 and 2x8)

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(8, 1)), FakeTensor(..., device='cuda:0', size=(2, 8))), **{}):
a and b must have same reduction dim, but got [8, 1] X [2, 8].

from user code:
   File "<string>", line 34, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.m1 = torch.nn.Linear(100, 100)

    def forward(self, qb, kb, vb):
        mat = torch.matmul(qb, kb.transpose((- 2), (- 1)))
        f1 = self.m1(mat)
        f = f1.div(0.001)
        d1 = torch.nn.functional.dropout(f, p=0.2)
        output = d1.matmul(vb)
        return output



func = Model().to('cuda')



qb = torch.randn(100, 100)



kb = torch.randn(800, 100)



vb = torch.randn(800, 100)


test_inputs = [qb, kb, vb]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (100x800 and 100x100)

jit:
Failed running call_module L__self___m1(*(FakeTensor(..., device='cuda:0', size=(100, 800)),), **{}):
a and b must have same reduction dim, but got [100, 800] X [100, 100].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
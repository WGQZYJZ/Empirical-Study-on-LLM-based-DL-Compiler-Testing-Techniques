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
        mat = torch.matmul(qb, kb.transpose(-2, -1))
        f1 = self.m1(mat)
        f = f1.div(0.001)
        d1 = torch.nn.functional.dropout(f, p=0.2)
        output = d1.matmul(vb)
        return output


func = Model().to('cpu')


qb = torch.randn(100, 100)

kb = torch.randn(800, 100)

vb = torch.randn(800, 100)

test_inputs = [qb, kb, vb]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (100x800 and 100x100)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(100, 800)), Parameter(FakeTensor(..., size=(100, 100), requires_grad=True)), Parameter(FakeTensor(..., size=(100,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [100, 800] X [100, 100].

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
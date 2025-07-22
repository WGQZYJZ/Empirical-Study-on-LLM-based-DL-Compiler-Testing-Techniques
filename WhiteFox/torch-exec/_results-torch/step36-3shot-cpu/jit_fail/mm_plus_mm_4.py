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

    def forward(self, t1, t2, t3, t4):
        v1 = torch.mm(t1, t2)
        v2 = torch.mm(t3, t4)
        v3 = v1 + v2
        return v3



func = Model().to('cpu')


t1 = torch.randn(600, 1)

t2 = torch.randn(600, 1)

t3 = torch.randn(600, 1)

t4 = torch.randn(600, 1)

test_inputs = [t1, t2, t3, t4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (600x1 and 600x1)

jit:
Failed running call_function <built-in method mm of type object at 0x73653d196ec0>(*(FakeTensor(..., size=(600, 1)), FakeTensor(..., size=(600, 1))), **{}):
a and b must have same reduction dim, but got [600, 1] X [600, 1].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
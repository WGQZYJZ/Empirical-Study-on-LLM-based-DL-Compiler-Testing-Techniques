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
        self.w1 = torch.randn(5, 5)
        self.w2 = torch.randn(5, 5)

    def forward(self, x1, x2):
        v1 = torch.mm(x1, self.w1)
        v2 = torch.mm(x1, self.w2)
        v3 = torch.mm(self.w1, x2)
        v4 = torch.mm(self.w2, x2)
        v5 = v1 + v2 + v3 + v4
        return v5 + v5



func = Model().to('cpu')


x1 = torch.randn(5, 5)

x2 = torch.randn(4, 5)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x5 and 4x5)

jit:
Failed running call_function <built-in method mm of type object at 0x7c7ce5b96ec0>(*(FakeTensor(..., size=(5, 5)), FakeTensor(..., size=(4, 5))), **{}):
a and b must have same reduction dim, but got [5, 5] X [4, 5].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
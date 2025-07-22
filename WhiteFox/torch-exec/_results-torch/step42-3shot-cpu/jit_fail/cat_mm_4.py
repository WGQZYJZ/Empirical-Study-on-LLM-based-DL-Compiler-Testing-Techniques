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
        self.v1 = torch.nn.Parameter(torch.randn(2, 3))
        self.v2 = torch.nn.Parameter(torch.randn(3, 4))
        self.v3 = torch.nn.Parameter(torch.randn(5, 3))
        self.v4 = torch.nn.Parameter(torch.randn(13, 11))
        self.v5 = torch.nn.Parameter(torch.randn(1, 13))

    def forward(self, x1):
        v6 = torch.mm(self.v1, self.v2)
        v7 = torch.mm(self.v3, self.v4)
        v8 = torch.mm(v7, self.v1)
        v9 = torch.mm(self.v3, self.v5)
        v10 = torch.mm(v9, x1)
        return torch.cat([v10, v6, v8, v9, v9, v8, v6, v9, v8, v6, v9], 0)



func = Model().to('cpu')


x1 = torch.randn(11, 1)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x3 and 13x11)

jit:
Failed running call_function <built-in method mm of type object at 0x7134c1196ec0>(*(Parameter(FakeTensor(..., size=(5, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(13, 11), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [5, 3] X [13, 11].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conva = torch.nn.Conv2d(3, 8, (1, 3), (1, 1), (0, 1))
        self.convb = torch.nn.Conv2d(8, 4, (7, 1), (1, 1), (0, 1))

    def forward(self, x1, other=None):
        var1 = self.conva(x1)
        var2 = self.convb(var1)
        if other == None:
            other = torch.randn([var2.shape[0]])
        var3 = var2 + other
        return var3



func = Model().to('cpu')


x1 = torch.randn(3, 3, 255, 255)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (257) must match the size of tensor b (3) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(s0, 4, s2 - 6, s3 + 2)), FakeTensor(..., size=(s0,))), **{}):
The size of tensor a (s3 + 2) must match the size of tensor b (s0) at non-singleton dimension 3)

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
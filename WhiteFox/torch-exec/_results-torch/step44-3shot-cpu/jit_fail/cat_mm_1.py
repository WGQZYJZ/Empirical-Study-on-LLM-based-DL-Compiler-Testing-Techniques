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

    def forward(self, x1, x2):
        v = [torch.mm(x1, x2)]
        v.append(torch.mm(x1, x2))
        v.append(torch.mm(x1, x2))
        for loopVar1 in range(100):
            v = torch.cat(v, 1)
            v = torch.split(v, 1, 1)
            v.append(torch.split(v, 1, 1)[-1])
        return v



func = Model().to('cpu')


x1 = torch.randn(2, 3)

x2 = torch.randn(2, 3)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x3 and 2x3)

jit:
Failed running call_function <built-in method mm of type object at 0x728f5db96ec0>(*(FakeTensor(..., size=(2, 3)), FakeTensor(..., size=(2, 3))), **{}):
a and b must have same reduction dim, but got [2, 3] X [2, 3].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
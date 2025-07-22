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

    def forward(self, input):
        t = torch.mm(input, input)
        return torch.cat([t, t])



func = Model().to('cpu')


input = torch.randn(3, 4)

test_inputs = [input]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x4 and 3x4)

jit:
Failed running call_function <built-in method mm of type object at 0x7e7126796ec0>(*(FakeTensor(..., size=(3, 4)), FakeTensor(..., size=(3, 4))), **{}):
a and b must have same reduction dim, but got [3, 4] X [3, 4].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
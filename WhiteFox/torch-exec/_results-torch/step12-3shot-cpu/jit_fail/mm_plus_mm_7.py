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

    def forward(self, input, input5):
        t1 = torch.mm(input, input5)
        t2 = torch.mm(input5, input)
        t3 = t1 + t2
        return t3



func = Model().to('cpu')


input = torch.randn(5, 5)

input5 = torch.randn(5, 3)

test_inputs = [input, input5]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x3 and 5x5)

jit:
Failed running call_function <built-in method mm of type object at 0x75da20796ec0>(*(FakeTensor(..., size=(5, 3)), FakeTensor(..., size=(s0, 5))), **{}):
a and b must have same reduction dim, but got [5, 3] X [s0, 5].

from user code:
   File "<string>", line 17, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
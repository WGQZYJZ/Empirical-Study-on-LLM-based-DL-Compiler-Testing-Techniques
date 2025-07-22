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

    def forward(self, input):
        t1 = torch.mm(input, input)
        t2 = torch.mm(input, input.T)
        return torch.mm(input, t1 + t2)



func = Model().to('cpu')


input1 = torch.randn(2, 3)

test_inputs = [input1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x3 and 2x3)

jit:
Failed running call_function <built-in method mm of type object at 0x71a9d0196ec0>(*(FakeTensor(..., size=(2, 3)), FakeTensor(..., size=(2, 3))), **{}):
a and b must have same reduction dim, but got [2, 3] X [2, 3].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
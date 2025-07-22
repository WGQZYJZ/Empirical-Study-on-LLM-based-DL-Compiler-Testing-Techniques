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

    def forward(self, x):
        return torch.mm(x, x)



func = Model().to('cpu')


x = torch.randn(150, 75)

test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (150x75 and 150x75)

jit:
Failed running call_function <built-in method mm of type object at 0x73653d196ec0>(*(FakeTensor(..., size=(150, 75)), FakeTensor(..., size=(150, 75))), **{}):
a and b must have same reduction dim, but got [150, 75] X [150, 75].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
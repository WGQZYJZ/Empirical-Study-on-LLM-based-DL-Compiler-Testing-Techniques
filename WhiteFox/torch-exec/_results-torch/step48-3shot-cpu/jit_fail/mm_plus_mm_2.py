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
        matrix = torch.nn.Parameter(torch.randn(1024, 1000))
        output = torch.mm(input, matrix)
        return output



func = Model().to('cpu')


input = torch.randn(5, 15)

test_inputs = [input]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x15 and 1024x1000)

jit:
Failed running call_function <built-in method mm of type object at 0x7135b4d96ec0>(*(FakeTensor(..., size=(5, 15)), FakeTensor(..., size=(1024, 1000), grad_fn=<TracableCreateParameterBackward>)), **{}):
a and b must have same reduction dim, but got [5, 15] X [1024, 1000].

from user code:
   File "<string>", line 17, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
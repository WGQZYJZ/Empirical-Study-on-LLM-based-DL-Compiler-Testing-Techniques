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
        return torch.mm(input, input)



func = Model().to('cpu')


input = torch.randn(7, 7, 7)

test_inputs = [input]

# JIT_FAIL
'''
direct:
self must be a matrix

jit:
Failed running call_function <built-in method mm of type object at 0x78bb93d96ec0>(*(FakeTensor(..., size=(7, 7, 7)), FakeTensor(..., size=(7, 7, 7))), **{}):
a must be 2D

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(3, 4)

    def forward(self, x):
        x = self.layers(x)
        x = torch.reshape(x, (2, 2))
        return x



func = Model().to('cpu')


x = torch.randn(2, 3)

test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[2, 2]' is invalid for input of size 8

jit:
Failed running call_function <built-in method reshape of type object at 0x7b1cd9d96ec0>(*(FakeTensor(..., size=(s0, 4)), (2, 2)), **{}):
shape '[2, 2]' is invalid for input of size 4*s0

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
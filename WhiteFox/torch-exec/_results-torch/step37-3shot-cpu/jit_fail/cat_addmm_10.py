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
        self.layers = nn.Linear(3, 2)

    def forward(self, x):
        x = self.layers(x)
        z = torch.stack((x,), dim=1)
        y = torch.cat((z, x), dim=1)
        return y



func = Model().to('cpu')


x = torch.randn(2, 3)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 3 and 2

jit:
Failed running call_function <built-in method cat of type object at 0x72889db96ec0>(*((FakeTensor(..., size=(2, 1, 2)), FakeTensor(..., size=(2, 2))),), **{'dim': 1}):
Number of dimensions of tensors must match.  Expected 3-D tensors, but got 2-D for tensor number 1 in the list

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
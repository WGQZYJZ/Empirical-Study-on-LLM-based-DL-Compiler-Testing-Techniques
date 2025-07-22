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
        self.layers = nn.Linear(2, 2)

    def forward(self, x):
        x = self.layers(x)
        x = x.flatten(start_dim=1)
        y = torch.stack([x, x, x], dim=1)
        x = x.flatten(start_dim=1)
        return torch.cat([x, y], dim=1)



func = Model().to('cpu')


x = torch.randn(1, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 2 and 3

jit:
Failed running call_function <built-in method cat of type object at 0x750e07196ec0>(*([FakeTensor(..., size=(1, 2)), FakeTensor(..., size=(1, 3, 2))],), **{'dim': 1}):
Number of dimensions of tensors must match.  Expected 2-D tensors, but got 3-D for tensor number 1 in the list

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
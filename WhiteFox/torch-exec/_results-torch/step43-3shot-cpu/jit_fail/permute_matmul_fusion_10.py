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
        self.v1 = torch.Tensor(2, 3)
        self.v1.uniform_(-10, 10)

    def forward(self, x1, x2):
        return torch.bmm(self.v1, x1)



func = Model().to('cpu')


x1 = torch.randn(1, 2, 3)

x2 = torch.randn(1, 2, 3)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
batch1 must be a 3D tensor

jit:
Failed running call_function <built-in method bmm of type object at 0x7dea82396ec0>(*(FakeTensor(..., size=(2, 3)), FakeTensor(..., size=(1, 2, 3))), **{}):
batch1 must be a 3D tensor

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
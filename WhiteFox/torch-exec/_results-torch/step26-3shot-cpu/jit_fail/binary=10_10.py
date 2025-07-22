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
        self.linear = torch.nn.Linear(3, 4)
        self.other = torch.nn.Parameter(torch.randn(4))

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = v1
        v3 = v2.transpose(0, 1).view(v2.shape[1]) + self.other
        return v3


func = Model().to('cpu')


x1 = torch.randn(2, 3)

x2 = torch.randn(4, 3)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
shape '[4]' is invalid for input of size 8

jit:
Failed running call_method view(*(FakeTensor(..., size=(4, 2)), 4), **{}):
shape '[4]' is invalid for input of size 8

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
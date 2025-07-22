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
        self.layers = nn.Linear(20, 4)

    def forward(self, x):
        x = self.layers(x)
        x = x.reshape(-1, 4, 5, 5)
        x = x.permute([3, 0, 1, 2])
        t = (x, x)
        x = torch.flatten(t)
        x = torch.stack((x, x, x, x), dim=0)
        return x



func = Model().to('cpu')


x = torch.randn(8, 20)

test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[-1, 4, 5, 5]' is invalid for input of size 32

jit:
Failed running call_method reshape(*(FakeTensor(..., size=(s0, 4)), -1, 4, 5, 5), **{}):
shape '[-1, 4, 5, 5]' is invalid for input of size 4*s0

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
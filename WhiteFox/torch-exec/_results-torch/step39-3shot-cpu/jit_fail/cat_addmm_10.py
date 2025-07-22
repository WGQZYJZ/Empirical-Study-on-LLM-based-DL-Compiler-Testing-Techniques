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
        self.layers = nn.Linear(100, 100)

    def forward(self, x):
        x = self.layers(x)
        x = torch.stack((x, x), dim=1)
        x = x.reshape(4, 100)
        return x



func = Model().to('cpu')


x = torch.randn(8, 100)

test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[4, 100]' is invalid for input of size 1600

jit:
Failed running call_method reshape(*(FakeTensor(..., size=(8, 2, 100)), 4, 100), **{}):
shape '[4, 100]' is invalid for input of size 1600

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
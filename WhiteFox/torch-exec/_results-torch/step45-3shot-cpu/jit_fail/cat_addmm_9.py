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
        self.layers = nn.Linear(2, 3)
        self.stack = torch.stack
        self.reshape = torch.reshape

    def forward(self, x):
        x = self.layers(x)
        x = self.stack((x, x, x), dim=0)
        x = self.reshape(x, (4, 3))
        x = self.stack((x, x, x), dim=0)
        x = self.reshape(x, (2, 3, 3))
        x = x.view(x.shape[1], 3)
        x = x.flatten(_sorted_check=False)
        x = x.view(x.shape[0], 3, 2)
        x = x.permute(2, 1, 0)
        x = torch.flatten(x)
        return x



func = Model().to('cpu')


x = torch.randn(2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[4, 3]' is invalid for input of size 18

jit:
Failed running call_function <built-in method reshape of type object at 0x7b017cd96ec0>(*(FakeTensor(..., size=(3, s0, 3)), (4, 3)), **{}):
shape '[4, 3]' is invalid for input of size 9*s0

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
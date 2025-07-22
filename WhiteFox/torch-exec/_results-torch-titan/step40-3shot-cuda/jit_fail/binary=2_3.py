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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v = torch.unsqueeze(x, 2)
        y = x.roll(10000, 1, 2)
        v1 = self.conv(v)
        v2 = (v1 - y)
        return v2




func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
roll() takes from 1 to 2 positional arguments but 3 were given

jit:
Failed running call_method roll(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), 10000, 1, 2), **{}):
roll() takes from 1 to 2 positional arguments but 3 were given

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
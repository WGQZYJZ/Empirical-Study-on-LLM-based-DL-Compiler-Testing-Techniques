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
        self.conv = torch.nn.Conv2d(1, 1, 1)

    def forward(self, x2):
        s2 = self.conv(x2)
        t2 = torch.nn.functional.tanh(s2)
        u2 = torch.nn.functional.tanh(s2)
        t2.retain_grad()
        u2.retain_grad()
        v2 = t2.view_as(u2)
        y2 = ((s2 + u2) + v2)
        return y2




func = Model().to('cuda')



x2 = torch.randn(5, 5, 1, 1)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 1, 1], expected input[5, 5, 1, 1] to have 1 channels, but got 5 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(5, 5, 1, 1)),), **{}):
Given groups=1, weight of size [1, 1, 1, 1], expected input[5, 5, 1, 1] to have 1 channels, but got 5 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
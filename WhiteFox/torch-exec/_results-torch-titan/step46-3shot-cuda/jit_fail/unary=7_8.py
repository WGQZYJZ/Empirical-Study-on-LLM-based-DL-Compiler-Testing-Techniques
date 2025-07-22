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
        self.linear = torch.nn.Linear(197, 100)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.linear(v1.view((- 1), 197)).clamp(0, 6)
        v3 = (v2 / 6)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[-1, 197]' is invalid for input of size 34848

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66)), -1, 197), **{}):
shape '[-1, 197]' is invalid for input of size 34848

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv2d_2 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 + x)
        v3 = torch.relu(v2)
        v4 = self.conv2d_2(v3)
        v5 = (v4 + x)
        v6 = torch.relu(v5)
        v7 = v6.view(10)
        return v7




func = Model().to('cuda')



x = torch.randn(1, 16, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
shape '[10]' is invalid for input of size 65536

jit:
Failed running call_method view(*(FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64)), 10), **{}):
shape '[10]' is invalid for input of size 65536

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
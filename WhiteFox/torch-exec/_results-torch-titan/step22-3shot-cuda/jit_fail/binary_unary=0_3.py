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
        self.conv1 = torch.nn.Conv2d(16, 16, 3, stride=16, padding=15)

    def forward(self, input):
        v1 = torch.relu(self.conv1(input))
        v2 = torch.tanh(v1)
        v3 = torch.matmul(v2, v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 8, 28, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 16, 3, 3], expected input[1, 8, 28, 28] to have 16 channels, but got 8 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(1, 8, 28, 28)),), **{}):
Given groups=1, weight of size [16, 16, 3, 3], expected input[1, 8, 28, 28] to have 16 channels, but got 8 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
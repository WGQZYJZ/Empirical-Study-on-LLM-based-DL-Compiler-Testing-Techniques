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
        self.conv = torch.nn.ConvTranspose2d(5, 10, 16, stride=3)
        self.max_pool = torch.nn.MaxPool2d(3, 2, padding=0)
        self.conv_transpose = torch.nn.ConvTranspose2d(2, 4, 4, padding=1, stride=2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = self.max_pool(v2)
        v4 = self.conv_transpose(v3)
        v5 = torch.relu(v4)
        v6 = torch.sigmoid(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 5, 100, 100)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [2, 4, 4, 4], expected input[1, 10, 156, 156] to have 2 channels, but got 10 channels instead

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 10, 156, 156)),), **{}):
Given transposed=1, weight of size [2, 4, 4, 4], expected input[1, 10, 156, 156] to have 2 channels, but got 10 channels instead

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
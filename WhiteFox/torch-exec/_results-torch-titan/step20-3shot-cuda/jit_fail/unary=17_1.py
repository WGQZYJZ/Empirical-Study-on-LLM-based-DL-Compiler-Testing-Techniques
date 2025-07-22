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
        self.conv = torch.nn.Conv2d(1, 32, 1, padding=0)
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 2, 1, stride=14)
        self.max_pool = torch.nn.MaxPool2d(3, 2, padding=0)
        self.conv_transpose1 = torch.nn.ConvTranspose2d(1, 2, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        y = self.conv_transpose(torch.relu(v1))
        v3 = self.max_pool(v1)
        w = self.conv_transpose1(v3)
        y1 = torch.relu(y)
        y2 = torch.relu(w)
        x = torch.max(y1, y2)
        return x




func = Model().to('cuda')



x1 = torch.ones(1, 1, 1, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 2, 1, 1], expected input[1, 32, 1, 1] to have 1 channels, but got 32 channels instead

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 32, 1, 1)),), **{}):
Given transposed=1, weight of size [1, 2, 1, 1], expected input[1, 32, 1, 1] to have 1 channels, but got 32 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
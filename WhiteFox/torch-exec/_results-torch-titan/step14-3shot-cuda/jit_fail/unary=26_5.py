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
        self.conv_t = torch.nn.ConvTranspose2d(10, 1, 3, stride=1)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        y = self.conv_t(x)
        y1 = (y > 0)
        y2 = (y * 0.2424)
        y3 = torch.where(y1, y, y2)
        y4 = self.relu(y3)
        return y4




func = Model().to('cuda')



x = torch.randn(1, 10, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [10, 1, 3, 3], expected input[1, 1, 10, 10] to have 10 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv_t(*(FakeTensor(..., device='cuda:0', size=(1, 10, 10)),), **{}):
Given transposed=1, weight of size [10, 1, 3, 3], expected input[1, 1, 10, 10] to have 10 channels, but got 1 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
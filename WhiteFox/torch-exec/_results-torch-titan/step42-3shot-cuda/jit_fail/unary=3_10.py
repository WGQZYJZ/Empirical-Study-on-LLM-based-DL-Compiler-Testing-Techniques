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
        self.conv1 = torch.nn.ConvTranspose2d(3, 3, (4, 4), stride=2)
        self.conv2 = torch.nn.ConvTranspose2d(6, 6, (2, 2), stride=2)
        self.conv3 = torch.nn.ConvTranspose2d(9, 12, (3, 3), stride=2)
        self.conv4 = torch.nn.ConvTranspose2d(15, 24, (4, 4), stride=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 41, 41)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [6, 6, 2, 2], expected input[1, 3, 84, 84] to have 6 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 3, 84, 84)),), **{}):
Given transposed=1, weight of size [6, 6, 2, 2], expected input[1, 3, 84, 84] to have 6 channels, but got 3 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
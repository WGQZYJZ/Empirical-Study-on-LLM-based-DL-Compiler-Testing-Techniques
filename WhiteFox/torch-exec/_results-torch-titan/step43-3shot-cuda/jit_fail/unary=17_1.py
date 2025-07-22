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
        self.conv2d = torch.nn.ConvTranspose2d(5, 3, 3, stride=2, padding=0)

    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = torch.relu(v1)
        v3 = v2.transpose(2, 1)
        v4 = torch.relu(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 1, 480, 100)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [5, 3, 3, 3], expected input[1, 1, 480, 100] to have 5 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv2d(*(FakeTensor(..., device='cuda:0', size=(1, 1, 480, 100)),), **{}):
Given transposed=1, weight of size [5, 3, 3, 3], expected input[1, 1, 480, 100] to have 5 channels, but got 1 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
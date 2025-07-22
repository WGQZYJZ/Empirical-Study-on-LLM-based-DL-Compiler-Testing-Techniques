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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 16, 3, padding=2, stride=2)
        self.conv_transpose1 = torch.nn.ConvTranspose2d(3, 32, 3, padding=2, stride=2)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.relu(v1)
        v3 = self.conv_transpose1(v2)
        v4 = torch.sigmoid(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [3, 32, 3, 3], expected input[1, 16, 125, 125] to have 3 channels, but got 16 channels instead

jit:
Failed running call_module L__self___conv_transpose1(*(FakeTensor(..., device='cuda:0', size=(1, 16, 125, 125)),), **{}):
Given transposed=1, weight of size [3, 32, 3, 3], expected input[1, 16, 125, 125] to have 3 channels, but got 16 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv2d = torch.nn.Conv2d(1, 2, 3, 1, 1)
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 2, 3, 1, 1)
        self.softmax = torch.nn.Softmax()

    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = self.conv_transpose(v1)
        v3 = self.softmax(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 2, 3, 3], expected input[1, 2, 2, 2] to have 1 channels, but got 2 channels instead

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2, 2)),), **{}):
Given transposed=1, weight of size [1, 2, 3, 3], expected input[1, 2, 2, 2] to have 1 channels, but got 2 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
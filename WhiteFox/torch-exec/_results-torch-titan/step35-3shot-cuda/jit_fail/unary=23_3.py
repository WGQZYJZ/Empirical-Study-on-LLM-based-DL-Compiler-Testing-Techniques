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
        self.conv = torch.nn.Conv2d(96, 192, kernel_size=(1, 3), stride=(1, 1), padding=(0, 1))
        self.conv_transpose = torch.nn.ConvTranspose2d(192, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.tanh(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 96, 35, 192)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [192, 128, 3, 3], expected input[1, 96, 35, 192] to have 192 channels, but got 96 channels instead

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 96, 35, 192)),), **{}):
Given transposed=1, weight of size [192, 128, 3, 3], expected input[1, 96, 35, 192] to have 192 channels, but got 96 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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



class Conv2dTest(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv2d = torch.nn.Conv2d(3, 1, 7, stride=2)
        self.conv_transpose = torch.nn.ConvTranspose2d(2, 1, 7, stride=2)

    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = self.conv_transpose(x1)
        return (v1, v2)




func = Conv2dTest().to('cuda')



x1 = torch.randn(1, 3, 62, 62)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [2, 1, 7, 7], expected input[1, 3, 62, 62] to have 2 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 3, 62, 62)),), **{}):
Given transposed=1, weight of size [2, 1, 7, 7], expected input[1, 3, 62, 62] to have 2 channels, but got 3 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv_t = torch.nn.ConvTranspose2d(11, 3, 2, stride=2)
        self.conv_t3 = torch.nn.ConvTranspose3d(22, 44, 3)

    def forward(self, x2):
        x5 = self.conv_t(x2)
        x6 = (x5 * 0.578)
        x7 = self.conv_t3(x2)
        return (x6, x7)




func = Model().to('cuda')



x2 = torch.randn(3, 11, 8, 8)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [22, 44, 3, 3, 3], expected input[1, 3, 11, 8, 8] to have 22 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv_t3(*(FakeTensor(..., device='cuda:0', size=(3, 11, 8, 8)),), **{}):
Given transposed=1, weight of size [22, 44, 3, 3, 3], expected input[1, 3, 11, 8, 8] to have 22 channels, but got 3 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
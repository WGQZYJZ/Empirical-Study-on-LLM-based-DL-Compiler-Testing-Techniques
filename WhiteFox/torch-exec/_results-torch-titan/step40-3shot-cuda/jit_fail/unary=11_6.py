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
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 32, 5, stride=1, padding=1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(8, 16, 3, stride=1, padding=1)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(4, 8, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.conv_transpose2(v1)
        v3 = self.conv_transpose3(v2)
        v4 = (v3 + 4)
        v5 = torch.clamp_min(v4, 0)
        v6 = torch.clamp_max(v5, 8)
        v7 = (v6 / 8)
        return (v7, v3, v2, v1)




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [8, 16, 3, 3], expected input[1, 32, 66, 66] to have 8 channels, but got 32 channels instead

jit:
Failed running call_module L__self___conv_transpose2(*(FakeTensor(..., device='cuda:0', size=(1, 32, 66, 66)),), **{}):
Given transposed=1, weight of size [8, 16, 3, 3], expected input[1, 32, 66, 66] to have 8 channels, but got 32 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.con_t1 = torch.nn.ConvTranspose2d(in_channels=1, out_channels=2, bias=False, kernel_size=(4, 4), stride=1, padding=2, output_padding=0)
        self.sigmoid = torch.nn.Sigmoid()
        self.con_t2 = torch.nn.ConvTranspose2d(in_channels=1, out_channels=2, bias=False, kernel_size=(6, 1), stride=1, padding=0, output_padding=0)

    def forward(self, x1):
        v1 = self.con_t1(x1)
        v2 = self.sigmoid(v1)
        v3 = self.con_t2(v2)
        v4 = self.sigmoid(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 1, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 2, 6, 1], expected input[1, 2, 15, 15] to have 1 channels, but got 2 channels instead

jit:
Failed running call_module L__self___con_t2(*(FakeTensor(..., device='cuda:0', size=(1, 2, 15, 15)),), **{}):
Given transposed=1, weight of size [1, 2, 6, 1], expected input[1, 2, 15, 15] to have 1 channels, but got 2 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
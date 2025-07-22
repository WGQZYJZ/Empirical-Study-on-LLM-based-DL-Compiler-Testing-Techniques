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
        self.module_0 = torch.nn.Sequential(torch.nn.ConvTranspose2d(8, 3, [3, 4], stride=[2, 1], padding=(0, 1)), torch.nn.Sigmoid())
        self.module_1 = torch.nn.Sequential(torch.nn.Conv2d(8, 1, [7, 5], stride=[2, 1], padding=(1, 3)), torch.nn.Sigmoid())
        self.module_2 = torch.nn.Sequential(torch.nn.ConvTranspose2d(8, 8, [4, 5], stride=[2, 1], padding=[1, 2]), torch.nn.ReLU())

    def forward(self, x1):
        v1 = self.module_0(x1)
        v2 = self.module_1
        v3 = self.module_2(v1)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 8, 93, 20)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [8, 8, 4, 5], expected input[1, 3, 187, 21] to have 8 channels, but got 3 channels instead

jit:
Failed running call_module L__self___module_2_0(*(FakeTensor(..., device='cuda:0', size=(1, 3, 187, 21)),), **{}):
Given transposed=1, weight of size [8, 8, 4, 5], expected input[1, 3, 187, 21] to have 8 channels, but got 3 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv_1 = torch.nn.ConvTranspose2d(220, 119, 1, stride=1, padding=1)
        self.max_pool_2 = torch.nn.MaxPool2d(kernel_size=3, stride=1, padding=1)
        self.conv_3 = torch.nn.ConvTranspose2d(119, 90, 1, stride=1, padding=1)
        self.conv_4 = torch.nn.ConvTranspose2d(90, 79, 1, stride=1, padding=1)
        self.conv_5 = torch.nn.ConvTranspose2d(79, 67, 1, stride=1, padding=1)
        self.conv_6 = torch.nn.ConvTranspose2d(67, 59, 1, stride=1, padding=1)
        self.conv_7 = torch.nn.ConvTranspose2d(59, 55, 1, stride=1, padding=1)
        self.conv_8 = torch.nn.ConvTranspose2d(55, 50, 1, stride=1, padding=1)
        self.max_pool_9 = torch.nn.MaxPool2d(kernel_size=3, stride=1, padding=1)
        self.conv_transpose_10 = torch.nn.ConvTranspose2d(50, 50, 2, stride=2, padding=1)

    def forward(self, x10):
        v20 = self.conv_1(x10)
        v21 = self.max_pool_2(v20)
        v22 = self.conv_3(v21)
        v23 = self.conv_4(v22)
        v24 = self.conv_5(v23)
        v25 = self.conv_6(v24)
        v26 = self.conv_7(v25)
        v27 = self.conv_8(v26)
        v28 = self.max_pool_9(v27)
        v29 = self.conv_transpose_10(v28)
        return v29




func = Model().to('cuda')



x10 = torch.randn(1, 220, 5, 19)


test_inputs = [x10]

# JIT_FAIL
'''
direct:
Trying to create tensor with negative dimension -1: [1, 79, -1, 13]

jit:
Failed running call_module L__self___conv_4(*(FakeTensor(..., device='cuda:0', size=(1, 90, 1, 15)),), **{}):
Trying to create tensor with negative dimension -1: [1, 79, -1, 13]

from user code:
   File "<string>", line 34, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
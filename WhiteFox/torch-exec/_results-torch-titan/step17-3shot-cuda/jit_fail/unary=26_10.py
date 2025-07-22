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
        self.conv_t = torch.nn.ConvTranspose2d(480, 24, kernel_size=(3, 3), padding=1, stride=2)
        self.linear1 = torch.nn.Linear(256, 345)
        self.relu = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(324, 2)

    def forward(self, x1):
        x2 = self.conv_t(x1)
        x3 = self.linear1(torch.flatten(x2))
        x4 = self.relu(x3)
        x5 = self.linear2(x4)
        return x5




func = Model().to('cuda')



x1 = torch.randn(16, 480, 6, 6)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x46464 and 256x345)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(46464,)),), **{}):
a and b must have same reduction dim, but got [1, 46464] X [256, 345].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
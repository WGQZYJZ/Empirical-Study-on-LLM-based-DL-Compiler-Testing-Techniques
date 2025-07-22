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



class model(nn.Module):

    def __init__(self, in_channels, out_channels, kernel_size, padding):
        super(model, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size, padding)
        self.relu1 = nn.ReLU()
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size, padding)
        self.relu2 = nn.ReLU()
        self.conv3 = nn.Conv2d(out_channels, out_channels, kernel_size, padding)
        self.relu3 = nn.ReLU()
        self.conv4 = nn.Conv2d(out_channels, out_channels, kernel_size, padding)
        self.relu4 = nn.ReLU()
        self.conv5 = nn.Conv2d(out_channels, out_channels, kernel_size, padding)
        self.relu5 = nn.ReLU()
        self.conv6 = nn.Conv2d(out_channels, out_channels, kernel_size, padding)
        self.relu6 = nn.ReLU()
        self.linear = nn.Linear(out_channels, 10)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.relu1(v1)
        v3 = self.conv2(v2)
        v4 = self.relu2(v3)
        v5 = self.conv3(v4)
        v6 = self.relu3(v5)
        v7 = self.conv4(v6)
        v8 = self.relu4(v7)
        v9 = self.conv5(v8)
        v10 = self.relu5(v9)
        v11 = self.conv6(v10)
        v12 = self.relu6(v11)
        v13 = v12.view(v12.size(0), (- 1))
        v14 = self.linear(v13)
        return v14




in_channels = 4


out_channels = 16


kernel_size = 3


padding = 1


func = model(in_channels, out_channels, kernel_size, padding).to('cuda')



x = torch.randn(1, 4, 32, 32)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x6400 and 16x10)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 6400)),), **{}):
a and b must have same reduction dim, but got [1, 6400] X [16, 10].

from user code:
   File "<string>", line 47, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv1 = torch.nn.Conv2d(3, 64, kernel_size=(1, 1))
        self.conv2 = torch.nn.Conv2d(64, 256, kernel_size=(3, 3), stride=1, padding=1)
        self.max_pool = torch.nn.MaxPool2d(kernel_size=3, stride=1, padding=1)
        self.drop1 = torch.nn.Dropout(p=0.136)
        self.drop2 = torch.nn.Dropout(p=0.436)
        self.dense1 = torch.nn.Linear(48032, 44, bias=True)
        self.dense3 = torch.nn.Linear(44, 25, bias=True)
        self.relu = torch.nn.ReLU()
        self.relu1 = torch.nn.ReLU()
        self.elu = torch.nn.ELU(alpha=0.019)
        self.selu = torch.nn.SELU()
        self.celu = torch.nn.CELU()

    def forward(self, x):
        v1 = self.elu(self.conv1(x))
        v2 = self.relu(self.conv2(v1))
        v3 = self.relu1(self.max_pool(v2))
        v4 = self.drop1(v3)
        v5 = v4.flatten((- 2), (- 1))
        v6 = self.drop2(self.relu(self.dense1(v5)))
        v7 = self.relu(self.dense3(v6))
        return v7




func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (256x4096 and 48032x44)

jit:
Failed running call_module L__self___dense1(*(FakeTensor(..., device='cuda:0', size=(1, 256, 4096)),), **{}):
a and b must have same reduction dim, but got [256, 4096] X [48032, 44].

from user code:
   File "<string>", line 38, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
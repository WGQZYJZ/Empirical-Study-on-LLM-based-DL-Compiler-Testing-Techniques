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
        self.linear1 = torch.nn.Linear(3, 2)
        self.bn1 = torch.nn.BatchNorm1d(num_features=3, affine=False)
        self.relu1 = torch.nn.ReLU(inplace=False)
        self.linear2 = torch.nn.Linear(3, 2)
        self.bn2 = torch.nn.BatchNorm1d(num_features=3, affine=False)
        self.sigmoid1 = torch.nn.Sigmoid()

    def forward(self, x):
        l1 = self.linear1(x)
        l2 = self.bn1(x)
        a = self.linear2((l1 + l2))
        a = self.bn2(a)
        a = self.relu1(a)
        x = self.bn2(torch.relu(self.linear2((self.bn1(self.linear1(x)) + a))))
        x = self.sigmoid1(x)
        return x




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (6x4 and 3x2)

jit:
Failed running call_module L__self___linear1(*(FakeTensor(..., device='cuda:0', size=(2, 3, 4)),), **{}):
a and b must have same reduction dim, but got [6, 4] X [3, 2].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
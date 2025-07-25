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
        torch.manual_seed(3)
        self.conv1 = torch.nn.Conv2d(3, 7, (3, 3), (1, 1), (1, 1))
        self.bn1 = torch.nn.BatchNorm2d(7)
        self.relu1 = torch.nn.ReLU(inplace=False)
        self.conv2 = torch.nn.Conv2d(7, 6, (3, 3), (2, 2), (1, 1))
        self.bn2 = torch.nn.BatchNorm2d(6)
        self.relu2 = torch.nn.ReLU(inplace=True)
        self.conv3 = torch.nn.Conv2d(6, 8, (3, 3), (1, 1), (1, 1))
        self.relu3 = torch.nn.ReLU(inplace=True)
        self.flatten3 = torch.nn.Flatten(start_dim=1, end_dim=(- 1))
        self.flatten1 = torch.nn.Flatten(start_dim=1, end_dim=(- 1))
        torch.manual_seed(5)
        self.layers1 = torch.nn.Sequential(torch.nn.ReLU(inplace=True), self.flatten3, torch.nn.Linear(384, 128), torch.nn.ReLU(inplace=True), torch.nn.Linear(128, 10))
        torch.manual_seed(6)
        self.layers2 = torch.nn.Sequential(torch.nn.LayerNorm([5408, 6]))
        torch.manual_seed(7)
        self.layers3 = torch.nn.Sequential(torch.nn.Linear(5408, 64))
        torch.manual_seed(8)
        self.layers4 = torch.nn.Sequential(torch.nn.Linear(6, 8))
        torch.manual_seed(9)
        self.layers5 = torch.nn.Sequential(torch.nn.Linear(8, 64))
        torch.manual_seed(10)
        self.layers6 = torch.nn.Sequential(torch.nn.Linear(64, 128))
        torch.manual_seed(1)
        self.layers7 = torch.nn.Sequential(torch.nn.ReLU(inplace=True), torch.nn.Linear(128, 384))
        torch.manual_seed(2)
        self.layers8 = torch.nn.Sequential(torch.nn.ReLU(inplace=True), torch.nn.Linear(384, 5408))
        torch.manual_seed(3)
        self.layers9 = torch.nn.Sequential(self.flatten1, torch.nn.ReLU(inplace=True), torch.nn.Linear(5408, 256), torch.nn.ReLU(inplace=True))

    def forward(self, x3):
        p1 = self.layers1(x3)
        p2 = self.layers2(x3)
        p3 = self.layers3(p2)
        o1 = self.layers4(p3)
        o2 = self.layers5(o1)
        o3 = self.layers6(o2)
        o4 = self.layers7(o3)
        o5 = self.layers8(o4)
        q1 = self.layers9(o5)
        return (q1 + p1)




func = Model().to('cuda')



x3 = torch.randn(42, 3, 28, 28)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (42x2352 and 384x128)

jit:
Failed running call_module L__self___layers1_2(*(FakeTensor(..., device='cuda:0', size=(42, 2352)),), **{}):
a and b must have same reduction dim, but got [42, 2352] X [384, 128].

from user code:
   File "<string>", line 50, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
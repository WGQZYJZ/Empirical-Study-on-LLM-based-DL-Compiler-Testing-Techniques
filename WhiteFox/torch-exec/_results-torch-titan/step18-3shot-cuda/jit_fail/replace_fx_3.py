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



class MyNet(nn.Module):

    def __init__(self):
        super(MyNet, self).__init__()
        self.features = nn.Sequential(nn.Conv2d(3, 16, kernel_size=3, padding=1), nn.ReLU(inplace=True), nn.Conv2d(16, 16, kernel_size=3, padding=1), nn.ReLU(inplace=True), nn.Conv2d(16, 32, kernel_size=3, padding=1), nn.ReLU(inplace=True))
        self.fc = nn.Linear(32768, 1)
        self.dropout = nn.Dropout(0.5)
        self.bn = nn.BatchNorm2d(32)

    def forward(self, x):
        out = self.features(x)
        out = self.bn(out)
        out = out.view(out.size(0), (- 1))
        out = self.dropout(out)
        out = self.fc(out)
        return out




func = MyNet().to('cuda')



x = torch.randn(2, 3, 50, 50)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x80000 and 32768x1)

jit:
Failed running call_module L__self___fc(*(FakeTensor(..., device='cuda:0', size=(2, 80000)),), **{}):
a and b must have same reduction dim, but got [2, 80000] X [32768, 1].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
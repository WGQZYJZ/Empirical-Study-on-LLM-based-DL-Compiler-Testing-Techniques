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
        self.features = torch.nn.Sequential(torch.nn.Conv2d(1, 168, 45, 35, 46), torch.nn.Conv2d(168, 107, 3, 21, 8))
        self.pad = torch.nn.Sequential(torch.nn.ConstantPad3d((0, 160, 100, 50), value=1.69117943))
        self.relu = torch.nn.ReLU(inplace=True)
        self.reshape = torch.nn.Sequential(torch.nn.Bilinear(490, 62, 482, bias=False))
        self.gelu = torch.nn.GELU()

    def forward(self, x1):
        x2 = self.features(x1)
        x2 = self.pad(x2)
        x2 = torch.clamp(x2, 0)
        x2 = self.relu(x2)
        x2 = torch.split(x2, [1, 1, 1, 1], dim=1)
        x2 = self.reshape(x2)
        x2 = torch.t(x2)
        x2 = self.gelu(x2)
        return (x2, x2)



func = Model().to('cpu')


x1 = torch.randn(1, 1, 789, 215)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 107 (input tensor's size at dimension 1), but got split_sizes=[1, 1, 1, 1]

jit:
Failed running call_function <function split at 0x728960bbbf70>(*(FakeTensor(..., size=(1, 107, 152, 162)), [1, 1, 1, 1]), **{'dim': 1}):
Split sizes add up to 4 but got the tensor's size of 107

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
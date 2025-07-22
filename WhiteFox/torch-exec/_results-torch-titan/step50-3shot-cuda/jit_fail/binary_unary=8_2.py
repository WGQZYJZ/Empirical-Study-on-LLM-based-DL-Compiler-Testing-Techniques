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
        self.conv1 = torch.nn.Conv2d(1, 8, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.nn.functional.interpolate(v1, scale_factor=0.5)
        v3 = self.conv1(x1)
        v4 = torch.cat((v2, v3), dim=1)
        v5 = torch.relu(v4)
        v6 = self.conv1(x1)
        v7 = torch.nn.functional.interpolate(v6, scale_factor=0.5)
        v8 = self.conv1(x1)
        v9 = torch.cat((v7, v8), dim=1)
        v10 = torch.relu(v9)
        return (v5 + v10)




func = Model().to('cuda')



x1 = torch.randn(1, 1, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 32 but got size 64 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x77f6ca2699e0>(*((FakeTensor(..., device='cuda:0', size=(1, 8, 32, 32)), FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64))),), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 32 but got 64 for tensor number 1 in the list

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
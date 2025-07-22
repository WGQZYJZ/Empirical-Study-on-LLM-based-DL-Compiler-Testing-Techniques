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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, padding=0)
        self.conv2 = torch.nn.Conv2d(8, 16, 3, stride=2, padding=1)

    def forward(self, x1):
        v0 = x1
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv2(v2)
        v4 = torch.relu(v3)
        v5 = torch.cat((v0, v4), 1)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 128, 512)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 128 but got size 64 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x719cace699e0>(*((FakeTensor(..., device='cuda:0', size=(1, 3, 128, 512)), FakeTensor(..., device='cuda:0', size=(1, 16, 64, 256))), 1), **{}):
Sizes of tensors must match except in dimension 1. Expected 128 but got 64 for tensor number 1 in the list

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
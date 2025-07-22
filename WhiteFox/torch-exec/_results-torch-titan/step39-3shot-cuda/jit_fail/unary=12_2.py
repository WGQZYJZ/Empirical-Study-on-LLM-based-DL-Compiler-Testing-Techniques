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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=2, dilation=2)
        self.conv3 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(8, 16, 3, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(16, 32, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        v3 = self.conv3(v1)
        v4 = self.conv4(v2)
        v5 = self.conv5(v3)
        v6 = torch.cat((v3, v4, v5), dim=1)




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 68 but got size 70 for tensor number 2 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x79e58b6699e0>(*((FakeTensor(..., device='cuda:0', size=(1, 16, 68, 68)), FakeTensor(..., device='cuda:0', size=(1, 16, 68, 68)), FakeTensor(..., device='cuda:0', size=(1, 32, 70, 70))),), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 68 but got 70 for tensor number 2 in the list

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
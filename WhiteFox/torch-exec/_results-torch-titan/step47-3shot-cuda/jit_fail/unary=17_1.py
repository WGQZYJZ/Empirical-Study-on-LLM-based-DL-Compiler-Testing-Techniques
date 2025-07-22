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
        self.conv = torch.nn.ConvTranspose2d(1, 1, 1, stride=1, padding=0)
        self.conv1 = torch.nn.ConvTranspose2d(1, 1, 3, stride=1, padding=0)

    def forward(self, x0, x1):
        v0 = self.conv(x0)
        v1 = self.conv1(x1)
        v2 = self.conv(v0)
        v3 = self.conv1(v1)
        v4 = self.conv(v2)
        v5 = self.conv1(v3)
        v6 = torch.cat([v4, v5], dim=1)
        v7 = torch.split(v6, [1, 1], dim=1)
        v8 = v7[0]
        v9 = v7[1]
        v10 = torch.relu(v9)
        v11 = torch.sigmoid(v9)
        v12 = torch.tanh(v8)
        v13 = ((v12 + v10) - v11)
        v14 = torch.squeeze(v13)
        v15 = ((v14 + v9) - v11)
        v16 = self.conv(v15)
        v17 = torch.max(v16)
        v18 = torch.argmax(v17)
        return v18




func = Model().to('cuda')



x0 = torch.randn(1, 1, 32, 32)



x1 = torch.randn(1, 1, 64, 64)


test_inputs = [x0, x1]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 32 but got size 70 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x74af4da699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 1, 32, 32)), FakeTensor(..., device='cuda:0', size=(1, 1, 70, 70))],), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 32 but got 70 for tensor number 1 in the list

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
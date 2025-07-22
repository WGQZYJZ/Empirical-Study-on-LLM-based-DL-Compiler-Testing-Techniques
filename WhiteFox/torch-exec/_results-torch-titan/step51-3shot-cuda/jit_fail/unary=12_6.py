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
        self.conv = torch.nn.Conv2d(3, 1, 1)
        self.conv2d = torch.nn.Conv2d(3, 4, 1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv2d(x1)
        v3 = torch.cat([v1, v2])
        v4 = self.sigmoid(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 0. Expected size 1 but got size 4 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x764a6fc699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 1, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 4, 64, 64))],), **{}):
Sizes of tensors must match except in dimension 0. Expected 1 but got 4 for tensor number 1 in the list

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
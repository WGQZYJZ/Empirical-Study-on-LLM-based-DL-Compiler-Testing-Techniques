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
        self.conv1 = torch.nn.Conv2d(3, 50, 5, stride=1, padding=2)
        self.conv2 = torch.nn.Conv2d(10, 80, 5, stride=1, padding=2)
        self.conv3 = torch.nn.Conv2d(100, 100, 5, stride=1, padding=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (v1 - 10)
        v3 = F.relu(v2)
        v4 = torch.unsqueeze(x1, 1)
        v5 = torch.cat([v3, v4], 1)
        v6 = self.conv2(v5)
        v7 = (v6 - torch.round(torch.neg(v6)))
        v8 = torch.mean(v7)
        v9 = torch.unsqueeze(v8, 1)
        v10 = torch.cat([v7, v9], 1)
        v11 = self.conv3(v10)
        v12 = (v11 - 10)
        v13 = F.relu(v12)
        return v13




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 4 and 5

jit:
Failed running call_function <built-in method cat of type object at 0x75e0ce6699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 50, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 1, 3, 64, 64))], 1), **{}):
Sizes of tensors must match except in dimension 1. Expected 64 but got 3 for tensor number 1 in the list

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
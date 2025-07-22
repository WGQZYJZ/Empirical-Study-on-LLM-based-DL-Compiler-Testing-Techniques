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

    def forward(self, x1):
        v1 = torch.nn.functional.conv2d(x1, torch.randn(16, 1, 3, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
        v2 = torch.nn.functional.conv2d(x1, torch.randn(16, 1, 3, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
        v3 = torch.nn.functional.conv2d(x1, torch.randn(16, 1, 3, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
        v4 = torch.nn.functional.conv2d(x1, torch.randn(16, 1, 3, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
        v5 = torch.nn.functional.conv2d(x1, torch.randn(16, 1, 3, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
        v6 = torch.nn.functional.conv2d(x1, torch.randn(16, 1, 3, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
        v7 = torch.nn.functional.conv2d(x1, torch.randn(16, 1, 3, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
        v8 = torch.nn.functional.conv2d(x1, torch.randn(16, 1, 3, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
        v9 = torch.nn.functional.conv2d(x1, torch.randn(16, 1, 3, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
        v10 = torch.nn.functional.conv2d(x1, torch.randn(16, 1, 3, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
        v11 = torch.nn.functional.conv2d(x1, torch.randn(16, 1, 3, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
        v12 = torch.nn.functional.conv2d(x1, torch.randn(16, 1, 3, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
        v13 = torch.nn.functional.conv2d(x1, torch.randn(16, 1, 3, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
        v14 = torch.nn.functional.conv2d(x1, torch.randn(16, 1, 3, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
        v15 = torch.nn.functional.conv2d(x1, torch.randn(16, 1, 3, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
        v16 = torch.nn.functional.conv2d(x1, torch.randn(16, 1, 3, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
        v17 = torch.nn.functional.conv2d(x1, torch.randn(16, 1, 3, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
        v18 = torch.nn.functional.conv2d(x1, torch.randn(16, 1, 3, 3), bias=None, stride=1, padding=0, dilation=1, groups=1)
        v19 = torch.cat((v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18), 1)
        v20 = torch.add(v19, torch.randn(1, 64, 56, 56))
        v21 = torch.nn.functional.relu(v20)
        return v21



func = Model().to('cuda')


x1 = torch.randn(1, 1, 56, 56)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Input type (torch.cuda.FloatTensor) and weight type (torch.FloatTensor) should be the same

jit:
Failed running call_function <built-in method add of type object at 0x7c3133396ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 288, s0 - 2, s1 - 2)), FakeTensor(..., size=(1, 64, 56, 56))), **{}):
The size of tensor a (s1 - 2) must match the size of tensor b (56) at non-singleton dimension 3)

from user code:
   File "<string>", line 38, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
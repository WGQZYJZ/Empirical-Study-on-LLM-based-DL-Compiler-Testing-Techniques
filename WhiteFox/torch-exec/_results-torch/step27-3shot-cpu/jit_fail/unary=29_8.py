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

    def __init__(self, min_value=-0.1, max_value=0.3):
        super().__init__()
        self.conv_transpose2d = torch.nn.ConvTranspose2d(3, 16, 1, stride=1, padding=1, bias=True)
        self.max_pool2d_1 = torch.nn.MaxPool2d(kernel_size=(2, 2), stride=1, padding=0)
        self.act_1 = torch.nn.ReLU()
        self.conv_transpose2d_1 = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0, bias=True)
        self.max_pool2d = torch.nn.MaxPool2d(kernel_size=(2, 2), stride=1, padding=0)
        self.act_2 = torch.nn.ReLU()
        self.conv_transpose2d_2 = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose2d(x1)
        v2 = self.max_pool2d_1(v1)
        v3 = self.act_1(v2)
        v4 = v1 + v3
        v5 = self.conv_transpose2d_1(v4)
        v6 = self.max_pool2d(v5)
        v7 = self.act_2(v6)
        v8 = self.conv_transpose2d_2(v7)
        v9 = torch.clamp_min(v8, self.min_value)
        v10 = torch.clamp_max(v9, self.max_value)
        return v10



func = Model().to('cpu')


x1 = torch.randn(1, 3, 768, 768)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (766) must match the size of tensor b (765) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(1, 16, 766, 766)), FakeTensor(..., size=(1, 16, 765, 765))), **{}):
Attempting to broadcast a dimension of length 765 at -1! Mismatching argument at index 1 had torch.Size([1, 16, 765, 765]); but expected shape should be broadcastable to [1, 16, 766, 766]

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.linear = torch.nn.Linear(2, 2)
        self.dropout = torch.nn.Dropout(0.5)
        self.sigmoid = torch.nn.Identity()
        self.maxpool = torch.nn.MaxPool1d(kernel_size=2, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)
        self.adaptive_avg_pool1d = torch.nn.AdaptiveAvgPool1d((1,))

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v3 = self.sigmoid(v2)
        v4 = self.dropout(v3)
        v5 = v4.unsqueeze(1)
        v6 = self.maxpool(v5)
        v7 = v6.squeeze(1)
        v8 = self.adaptive_avg_pool1d(v7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
max_pool1d: Expected 2D or 3D (batch mode) tensor with optional 0 dim batch size for input, but got:[1, 1, 2, 2]

jit:
Failed running call_module L__self___maxpool(*(FakeTensor(..., device='cuda:0', size=(1, 1, 2, 2)),), **{}):
max_pool1d: Expected 2D or 3D (batch mode) tensor with optional 0 dim batch size for input, but got:[1, 1, 2, 2]

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
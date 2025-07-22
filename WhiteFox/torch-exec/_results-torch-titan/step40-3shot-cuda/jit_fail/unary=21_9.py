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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.Conv2d_0a_1x1 = torch.nn.Conv2d(1, 32, 3, stride=2)
        self.Conv2d_1a_3x3 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=1)
        self.Conv2d_1b_1x3 = torch.nn.Conv2d(32, 32, (1, 3), stride=(1, 2), padding=(0, 1))
        self.Conv2d_1c_3x1 = torch.nn.Conv2d(32, 32, (3, 1), stride=2)
        self.Conv2d_1d_3x3 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=1)
        self.Conv2d_1e_1x3 = torch.nn.Conv2d(32, 32, (1, 3), stride=(1, 2), padding=(0, 1))
        self.Conv2d_1f_3x1 = torch.nn.Conv2d(32, 32, (3, 1), stride=2)
        self.BatchNorm_0 = torch.nn.BatchNorm2d(32, eps=9.999999747378752e-06, momentum=0.1)
        self.Conv2d_0b_1x1 = torch.nn.Conv2d(32, 256, 1, stride=1)
        self.Flatten_0 = torch.nn.Flatten((- 1))
        self.Softmax_0 = torch.nn.Softmax()
        self.Dropout_0 = torch.nn.Dropout(p=0.2)
        self.Linear_0 = torch.nn.Linear(256, 10)

    def forward(self, x):
        v1 = self.Conv2d_0a_1x1(x)
        v2 = self.Conv2d_1a_3x3(v1)
        v3 = self.Conv2d_1b_1x3(v2)
        v4 = self.Conv2d_1c_3x1(v3)
        v5 = torch.tanh(torch.tanh(v4))
        v6 = self.Conv2d_1d_3x3(v5)
        v7 = self.Conv2d_1e_1x3(v6)
        v8 = self.Conv2d_1f_3x1(v7)
        v9 = self.BatchNorm_0(v8)
        v10 = self.Conv2d_0b_1x1(v9)
        v11 = self.Flatten_0(v10)
        v12 = self.Softmax_0(v11)
        v13 = torch.tanh(v12)
        v14 = self.Dropout_0(v13)
        v15 = self.Linear_0(v14)
        return v15




func = ModelTanh().to('cuda')



x = torch.randn(1, 1, 5, 5)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2 x 1). Kernel size: (3 x 1). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___Conv2d_1c_3x1(*(FakeTensor(..., device='cuda:0', size=(1, 32, 2, 1)),), **{}):
Calculated padded input size per channel: (2 x 1). Kernel size: (3 x 1). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 37, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
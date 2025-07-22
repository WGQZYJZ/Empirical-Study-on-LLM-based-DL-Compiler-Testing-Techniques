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

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        x2 = torch.nn.functional.relu(v2)
        v3 = torch.nn.functional.interpolate(x2, size=5, scale_factor=0.125, mode='bilinear', align_corners=False)
        v4 = torch.argmax(v3, dim=1).unsqueeze(dim=1)
        v4 = torch.nn.functional.embedding(v4, self.linear.weight)
        v5 = (v3 == v2).to(v3.dtype)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
only one of size or scale_factor should be defined

jit:
Failed running call_function <function interpolate at 0x7dffc62f8430>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)),), **{'size': 5, 'scale_factor': 0.125, 'mode': 'bilinear', 'align_corners': False}):
only one of size or scale_factor should be defined

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
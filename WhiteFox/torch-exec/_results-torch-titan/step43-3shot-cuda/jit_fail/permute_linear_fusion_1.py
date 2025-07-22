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
        self.avg_pool2d = torch.nn.AvgPool2d(kernel_size=(1, 1), stride=(1, 1), padding=(0,), ceil_mode=False, count_include_pad=True)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v3 = v2.unsqueeze(1).unsqueeze(2)
        v4 = self.avg_pool2d(v3)
        v5 = v4.squeeze()
        v6 = (v2 + v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D or 4D (batch mode) tensor with optional 0 dim batch size for input, but got:[1, 1, 1, 2, 2]

jit:
Failed running call_module L__self___avg_pool2d(*(FakeTensor(..., device='cuda:0', size=(1, 1, 1, 2, 2)),), **{}):
Expected 3D or 4D (batch mode) tensor with optional 0 dim batch size for input, but got: torch.Size([1, 1, 1, 2, 2])

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
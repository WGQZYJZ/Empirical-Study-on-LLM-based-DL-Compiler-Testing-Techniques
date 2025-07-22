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

    def forward(self, x1, x2):
        v1 = torch.nn.functional.conv_transpose2d(x1, x2, 3, stride=2, padding=1, output_padding=1)
        v2 = (v1 + 3)
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = (v4 / 6)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(8, 3, 3, 3)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'bias' (position 3) must be Tensor, not int

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7e936da699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), FakeTensor(..., device='cuda:0', size=(8, 3, 3, 3)), 3), **{'stride': 2, 'padding': 1, 'output_padding': 1}):
conv_transpose2d(): argument 'bias' (position 3) must be Tensor, not int

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
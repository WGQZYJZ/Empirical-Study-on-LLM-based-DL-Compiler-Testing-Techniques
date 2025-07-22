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
        v1 = torch.nn.functional.conv_transpose3d(x1, 16, 5, 5, 0, 2, 1, bias=False)
        v2 = (v1 + 4)
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = (v1 * v4)
        v6 = (v5 / 6)
        return v6




func = Model().to('cuda')



x1 = torch.randn(2, 3, 256, 256, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv_transpose3d(): argument 'weight' (position 2) must be Tensor, not int

jit:
Failed running call_function <built-in method conv_transpose3d of type object at 0x7ad78ba699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 3, 256, 256, 256)), 16, 5, 5, 0, 2, 1), **{'bias': False}):
conv_transpose3d(): argument 'weight' (position 2) must be Tensor, not int

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
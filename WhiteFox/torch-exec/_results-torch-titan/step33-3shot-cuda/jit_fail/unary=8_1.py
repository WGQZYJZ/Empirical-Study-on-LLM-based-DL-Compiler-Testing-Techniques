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
        v1 = torch.conv_transpose3d(x1, torch.randn(21, 6, 5, 5, 3), stride=2, groups=1, padding=4, dilation=1, out_padding=1)
        v2 = (v1 + 3)
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = (v1 * v4)
        v6 = (v5 / 6)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 9, 16, 16, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv_transpose3d() got an unexpected keyword argument 'out_padding'

jit:
Failed running call_function <built-in method conv_transpose3d of type object at 0x7d734de699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 9, 16, 16, 16)), FakeTensor(..., size=(21, 6, 5, 5, 3))), **{'stride': 2, 'groups': 1, 'padding': 4, 'dilation': 1, 'out_padding': 1}):
conv_transpose3d() got an unexpected keyword argument 'out_padding'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
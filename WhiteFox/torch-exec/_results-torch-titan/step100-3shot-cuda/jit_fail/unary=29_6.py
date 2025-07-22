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

    def __init__(self, min_value=(- 9.662e+37), max_value=6.687e+37):
        super().__init__()
        self.conv_transpose2d = torch.nn.ConvTranspose2d(3, 4, 3, stride=2, padding=1)
        self.conv_transpose3d = torch.nn.ConvTranspose3d(2, 5, 3, stride=1, padding=0)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v0 = x1
        v1 = self.conv_transpose2d(v0)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = v3.contiguous(memory_format=torch.channels_last)
        v4 = self.conv_transpose3d(v4)
        return v4




func = Model().to('cuda')



x1 = torch.randn(6, 3, 76, 88, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [6, 3, 76, 88, 1]

jit:
Failed running call_module L__self___conv_transpose2d(*(FakeTensor(..., device='cuda:0', size=(6, 3, 76, 88, 1)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv_transpose2d, but got input of size: [6, 3, 76, 88, 1]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
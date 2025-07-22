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

    def __init__(self, min_value=(- 2.0), max_value=12.0):
        super().__init__()
        self.conv_transpose3d = torch.nn.ConvTranspose3d(3, 2, kernel_size=(1, 1, 1))
        self.conv2d = torch.nn.Conv2d(3, 3, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0), dilation=(1, 1))
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x8):
        v9 = self.conv_transpose3d(x8)
        v10 = self.conv2d(v9)
        v11 = torch.clamp_min(v10, self.min_value)
        v12 = torch.clamp_max(v11, self.max_value)
        return v12




func = Model().to('cuda')



x8 = torch.randn(16, 3, 4, 36, 56)


test_inputs = [x8]

# JIT_FAIL
'''
direct:
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [16, 2, 4, 36, 56]

jit:
Failed running call_module L__self___conv2d(*(FakeTensor(..., device='cuda:0', size=(16, 2, 4, 36, 56)),), **{}):
Expected 3D (unbatched) or 4D (batched) input to conv2d, but got input of size: [16, 2, 4, 36, 56]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
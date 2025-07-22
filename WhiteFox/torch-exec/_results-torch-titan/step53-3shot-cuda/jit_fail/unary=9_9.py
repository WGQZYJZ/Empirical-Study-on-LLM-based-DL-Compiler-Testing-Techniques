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
        self.layer_norm = torch.nn.LayerNorm([2, 2], elementwise_affine=False)

    def forward(self, x1):
        v1 = self.layer_norm(x1)
        v2 = torch.nn.functional.conv2d(v1, torch.ones(1, 1, 3, 3), padding=1)
        v3 = v2.clamp(min=0, max=6)
        v4 = (v3 / 6)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 3, 3], expected input[1, 3, 2, 2] to have 1 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7c7a41a699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 2, 2)), FakeTensor(..., size=(1, 1, 3, 3))), **{'padding': 1}):
Given groups=1, weight of size [1, 1, 3, 3], expected input[1, 3, 2, 2] to have 1 channels, but got 3 channels instead

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
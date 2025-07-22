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

    def __init__(self, min_value=475.75, max_value=489.0):
        super().__init__()
        self.threshold = torch.nn.Threshold(0.0, 0.0)
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 6, 2, stride=2, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x2):
        v1 = self.conv_transpose(x2)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.threshold(v3, 0.0)
        return v4




func = Model().to('cuda')



x2 = torch.randn(1, 8, 19, 17)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
Failed running call_module L__self___threshold(*(FakeTensor(..., device='cuda:0', size=(1, 6, 36, 32)), 0.0), **{}):
forward() takes 2 positional arguments but 3 were given

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
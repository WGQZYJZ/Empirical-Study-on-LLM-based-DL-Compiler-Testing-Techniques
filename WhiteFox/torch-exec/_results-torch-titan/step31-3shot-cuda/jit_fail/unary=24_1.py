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
        self.conv_1 = torch.nn.Conv2d(4, 8, 1, stride=1, padding=1)
        self.conv_2 = torch.nn.Conv2d(8, 4, 1, stride=1, padding=1)

    def forward(self, x):
        negative_slope = 0
        v1 = self.conv_1(x)
        v2 = torch.sum(v1, dim=1)
        v3 = (v2 > 0)
        v4 = (v2 * negative_slope)
        v5 = torch.where(v3, v2, v4)
        v6 = v5.shape[2]
        v7 = v5.shape[3]
        v8 = self.conv_2(v5)
        v9 = v8[:, :, :v6, :v7].squeeze()
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 4, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
tuple index out of range

jit:
list index out of range

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
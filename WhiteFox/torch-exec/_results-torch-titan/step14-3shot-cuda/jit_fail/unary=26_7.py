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
        self.conv_t_11 = torch.nn.ConvTranspose2d(1024, 11, 1)

    def forward(self, x):
        v0 = x.view(x.size(0), 1024, (- 1))
        v1 = v0.view(v0.size(0), (- 1), 1, 11)
        v9 = self.conv_t_11(v1)
        v10 = (v9 > 0)
        v4 = (v9 * 0.4)
        v5 = torch.where(v10, v9, v4)
        v11 = (v5 < 1)
        v12 = (v11 * 0.1)
        v2 = (v5 * 0.2)
        v7 = torch.where(v11, v2, v12)
        v3 = (v7 * (- 0.9))
        v6 = torch.where(v11, v3, v7)
        v8 = torch.mean(x)
        return torch.cat([v6, v8])




func = Model().to('cuda')



x = torch.randn(1, 1024, 11, 1)


test_inputs = [x]

# JIT_FAIL
'''
direct:
zero-dimensional tensor (at position 1) cannot be concatenated

jit:
backend='inductor' raised:
AssertionError: 


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
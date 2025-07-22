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
        self.block = torch.nn.Sequential(torch.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=3), torch.nn.ReLU(inplace=True))

    def forward(self, x1):
        v1 = self.block(x1)
        (v, v1) = torch.split(v1, [1, 1, 1], dim=1)
        x2 = self.block(v)
        return ((x1 * x2), ((v1 * x1), (v1 * x2)), v1)




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
too many values to unpack (expected 2)

jit:


from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
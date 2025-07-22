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
        self.conv = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)

    def forward(self, x, y):
        v1 = self.conv(x)
        y_len = y.size(0)
        v2 = y.view(1, y_len)
        v3 = torch.cat([v1, v2], 1)
        v4 = torch.full((y_len,), (- 1), dtype=torch.int32)
        v5 = v3[:, v4]
        return v5



func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)



y = torch.randn(10)


test_inputs = [x, y]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 4 and 2

jit:
backend='inductor' raised:
AssertionError: 


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
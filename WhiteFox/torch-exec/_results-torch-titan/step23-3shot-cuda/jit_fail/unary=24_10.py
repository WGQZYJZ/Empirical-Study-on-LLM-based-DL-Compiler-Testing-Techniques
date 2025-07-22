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
        self.conv1 = torch.nn.Conv2d(2, 3, 1, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = (v1 * 0.1)
        v3 = v1[0, 0, 0, :]
        v4 = v1[:, :, 0, 0]
        v5 = torch.cat((v3, v4), dim=0)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 2, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 1 and 2

jit:
backend='inductor' raised:
AssertionError: 


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
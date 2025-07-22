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
        self.conv = torch.nn.Conv2d(4, 12, 3, stride=2, padding=1)

    def forward(self, x1, other):
        v1 = self.conv(x1)
        if (x1.shape[0] != other.shape[0]):
            v1 = torch.randn(v1.shape)
        other = v1
        if (v1.shape[1] == other.shape[1]):
            if (other.shape[1] == other.shape[3]):
                if (v1.shape[3] < other.shape[1] == 8):
                    if ((other.shape[0] == other.shape[2]) or (other.shape[1] == 8)):
                        if (v1.shape[1] == other.shape[3]):
                            other = torch.randn(v1.shape)
        v2 = other
        if (other.shape[0] >= 4):
            if (other.shape[0] != v2.shape[0]):
                v2 = torch.randn(v2.shape)
            v2 = torch.randn(v2.shape)
            v2 = v1
        if (v1.shape[1] < v2.shape[1]):
            other = v1
        v3 = (v2 + other)
        if (self.conv.stride == (2, 2)):
            if (v3.shape[1] == v2.shape[1] == 1):
                if (v2.shape[0] == v2.shape[3] == 8):
                    if ((v1.shape[3] > v3.shape[1]) and (v2.shape[1] == v3.shape[1] == v2.shape[2])):
                        if (v2.shape[2] < v3.shape[1] == 1):
                            if ((v2.shape[0] * v2.shape[1]) == v1.shape[1] == v2.shape[3]):
                                if (v2.shape[3] == v3.shape[0] == v2.shape[2]):
                                    if (v3.shape[3] == v2.shape[3]):
                                        other = torch.randn((v1.shape[0], ((v1.shape[1] + v1.shape[2]) + v1.shape[3]), v3.shape[0], (v3.shape[1] - v3.shape[2])))
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 4, 64, 64)

other = 1

test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'shape'

jit:
'int' object has no attribute 'shape'

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
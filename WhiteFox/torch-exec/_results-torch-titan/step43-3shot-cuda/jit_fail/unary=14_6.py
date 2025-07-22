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
        self.conv_transpose_0 = torch.nn.ConvTranspose2d(1385, 599, 1, stride=1, padding=0, dilation=1)
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(599, 785, 1, stride=1, padding=0, dilation=1)

    def forward(self, x1):
        v1 = self.conv_transpose_0(x1)
        v2 = torch.sigmoid(v1)
        v4 = self.conv_transpose_1(v2)
        v5 = torch.sigmoid(v4)
        v6 = (v4 * v5)
        v7 = (v3 * v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 1385, 100, 100)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'v3' is not defined

jit:
name 'v3' is not defined

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
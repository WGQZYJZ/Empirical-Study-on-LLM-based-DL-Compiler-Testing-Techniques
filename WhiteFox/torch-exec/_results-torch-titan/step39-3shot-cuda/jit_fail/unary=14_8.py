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
        self.conv_transpose_5 = torch.nn.ConvTranspose2d(7338, 1, 7, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose_5(x1)
        v2 = torch.sigmoid(v1)
        v3 = (v1 * v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 6638, 1, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [7338, 1, 7, 7], expected input[1, 6638, 1, 3] to have 7338 channels, but got 6638 channels instead

jit:
Failed running call_module L__self___conv_transpose_5(*(FakeTensor(..., device='cuda:0', size=(1, 6638, 1, 3)),), **{}):
Given transposed=1, weight of size [7338, 1, 7, 7], expected input[1, 6638, 1, 3] to have 7338 channels, but got 6638 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
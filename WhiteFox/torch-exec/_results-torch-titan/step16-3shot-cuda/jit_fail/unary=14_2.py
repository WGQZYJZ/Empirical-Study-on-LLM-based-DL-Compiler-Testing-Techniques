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
        self.trans_3 = torch.nn.ConvTranspose3d(4, 1, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.trans_3(x1)
        v2 = torch.sigmoid(v1)
        v3 = (v1 * v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 1, 2, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [4, 1, 1, 1, 1], expected input[1, 1, 2, 2, 2] to have 4 channels, but got 1 channels instead

jit:
Failed running call_module L__self___trans_3(*(FakeTensor(..., device='cuda:0', size=(1, 1, 2, 2, 2)),), **{}):
Given transposed=1, weight of size [4, 1, 1, 1, 1], expected input[1, 1, 2, 2, 2] to have 4 channels, but got 1 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv_transpose1d = torch.nn.ConvTranspose1d(3, 6, 3, stride=4, padding=5)
        self.conv_transpose2d = torch.nn.ConvTranspose2d(5, 1, 3, stride=1, padding=1)
        self.conv_transpose3d = torch.nn.ConvTranspose3d(7, 6, (1, 4, 3), stride=(1, 2, 3), padding=(2, 1, 4))

    def forward(self, x1):
        v1 = torch.tanh(self.conv_transpose1d(x1))
        v2 = torch.tanh(self.conv_transpose2d(v1))
        v3 = torch.tanh(self.conv_transpose3d(v2))
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 127)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [5, 1, 3, 3], expected input[1, 1, 6, 497] to have 5 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv_transpose2d(*(FakeTensor(..., device='cuda:0', size=(1, 6, 497)),), **{}):
Given transposed=1, weight of size [5, 1, 3, 3], expected input[1, 1, 6, 497] to have 5 channels, but got 1 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
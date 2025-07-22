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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(1, 24, kernel_size=(3, 3), stride=(3, 3), padding=1)
        self.avg_pool = torch.nn.AvgPool2d(kernel_size=(3, 3), stride=(3, 3), padding=2)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = self.avg_pool(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(5, 1, 2, 6)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
pad should be at most half of kernel size, but got pad=2 and kernel_size=3

jit:
Failed running call_module L__self___avg_pool(*(FakeTensor(..., device='cuda:0', size=(5, 24, 4, 16)),), **{}):
pad should be at most half of kernel size, but got pad=2 and kernel_size=3

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
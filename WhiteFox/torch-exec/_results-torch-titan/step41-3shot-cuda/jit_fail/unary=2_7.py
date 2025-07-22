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
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 5, kernel_size=1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        return v1




func = Model().to('cuda')



x1 = torch.randn(5, 3, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [3, 5, 1, 1], expected input[1, 5, 3, 1] to have 3 channels, but got 5 channels instead

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(5, 3, 1)),), **{}):
Given transposed=1, weight of size [3, 5, 1, 1], expected input[1, 5, 3, 1] to have 3 channels, but got 5 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def __init__(self, channels_in):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(1, 3, 11, padding=5, bias=False)

    def forward(self, x):
        x = self.conv_t(x)
        return x




channels_in = 9


func = Model(channels_in).to('cuda')



channels_in = 9


x = torch.randn(1, channels_in, 12, 12)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 3, 11, 11], expected input[1, 9, 12, 12] to have 1 channels, but got 9 channels instead

jit:
Failed running call_module L__self___conv_t(*(FakeTensor(..., device='cuda:0', size=(1, 9, 12, 12)),), **{}):
Given transposed=1, weight of size [1, 3, 11, 11], expected input[1, 9, 12, 12] to have 1 channels, but got 9 channels instead

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
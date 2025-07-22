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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_1 = torch.nn.Conv2d(in_channels=3, out_channels=1, kernel_size=(1, 203), stride=(1, 1), padding=(0, 0), dilation=(1, 1))

    def forward(self, input):
        X0 = self.conv_1(input)
        X1 = torch.tanh(X0)
        return X1




func = ModelTanh().to('cuda')



input = torch.randn(1, 3, 253, 1)


test_inputs = [input]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (253 x 1). Kernel size: (1 x 203). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv_1(*(FakeTensor(..., device='cuda:0', size=(1, 3, 253, 1)),), **{}):
Calculated padded input size per channel: (253 x 1). Kernel size: (1 x 203). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
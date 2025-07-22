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



class model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv3d(32, 12, 2, bias=False)
        self.dropout_fn = torch.nn.Dropout2d(0.5, inplace=False)

    def forward(self, input, weight, bias):
        x = input.permute(0, 2, 3, 4, 1)
        y = self.conv(x)
        y = (y + self.conv.weight)
        z = self.dropout_fn(y)
        x = z.permute(0, 4, 1, 2, 3)
        x = input.view(input.shape)
        return (input, x, weight, bias)




func = model().to('cuda')



input = torch.randn(1, 32, 2, 2, 2)



weight = torch.randn(1024, 16384)



bias = torch.randn(1024)


test_inputs = [input, weight, bias]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [12, 32, 2, 2, 2], expected input[1, 2, 2, 2, 32] to have 32 channels, but got 2 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2, 2, 32)),), **{}):
Given groups=1, weight of size [12, 32, 2, 2, 2], expected input[1, 2, 2, 2, 32] to have 32 channels, but got 2 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
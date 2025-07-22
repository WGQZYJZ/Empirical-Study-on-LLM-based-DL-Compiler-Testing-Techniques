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
        self.conv_transpose = torch.nn.ConvTranspose2d(in_channels=1, out_channels=2, kernel_size=8, stride=1, padding=0)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(in_channels=2, out_channels=4, kernel_size=8, stride=1, padding=0)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(in_channels=4, out_channels=8, kernel_size=8, stride=1, padding=0)

    def forward(self, x1, x2, x3):
        v1 = [self.conv_transpose, self.conv_transpose2, self.conv_transpose3][0](x1)
        v2 = self.conv_transpose3(x2)
        v3 = ((v1 + v2) + x3)
        v4 = torch.relu6(v3)
        v5 = torch.dropout(v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 1, 1, 1)



x2 = torch.randn(1, 1, 1, 1)



x3 = torch.randn(1, 1, 1, 1)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [4, 8, 8, 8], expected input[1, 1, 1, 1] to have 4 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv_transpose3(*(FakeTensor(..., device='cuda:0', size=(1, 1, 1, 1)),), **{}):
Given transposed=1, weight of size [4, 8, 8, 8], expected input[1, 1, 1, 1] to have 4 channels, but got 1 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
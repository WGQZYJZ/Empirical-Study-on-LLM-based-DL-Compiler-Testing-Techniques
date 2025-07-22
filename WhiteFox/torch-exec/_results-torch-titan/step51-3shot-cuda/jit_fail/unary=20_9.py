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
        self.conv_t1 = torch.nn.ConvTranspose2d(30, 16, kernel_size=(3, 3), stride=(2, 2), padding=(2, 2))
        self.conv_t2 = torch.nn.ConvTranspose2d(16, 10, kernel_size=(3, 3), stride=(1, 2), padding=(2, 2))
        self.conv_t3 = torch.nn.ConvTranspose2d(10, 5, kernel_size=(4, 4), stride=(1, 1), padding=(2, 2))

    def forward(self, x1):
        v1 = self.conv_t1(x1)
        v2 = F.relu(v1)
        v3 = self.conv_t2(v2)
        v4 = F.softmax(v3, dim=1)
        v5 = v4.transpose(1, 2)
        v6 = self.conv_t3(v5)
        v7 = F.sigmoid(v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 30, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [10, 5, 4, 4], expected input[1, 123, 10, 247] to have 10 channels, but got 123 channels instead

jit:
Failed running call_module L__self___conv_t3(*(FakeTensor(..., device='cuda:0', size=(1, 123, 10, 247)),), **{}):
Given transposed=1, weight of size [10, 5, 4, 4], expected input[1, 123, 10, 247] to have 10 channels, but got 123 channels instead

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
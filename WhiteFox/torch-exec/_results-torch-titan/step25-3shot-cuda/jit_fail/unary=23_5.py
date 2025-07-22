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
        self.pool = torch.nn.AvgPool2d(10, stride=1)
        self.conv_transpose = torch.nn.ConvTranspose2d(64, 32, kernel_size=10, padding=10, stride=10, dilation=10, groups=32)

    def forward(self, x1):
        v1 = self.pool(x1)
        v2 = self.conv_transpose(v1)
        v3 = v2.reshape((- 1), 32, 100)
        return (v3, v1)




func = Model().to('cuda')



x1 = torch.randn(1, 64, 500, 600)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[-1, 32, 100]' is invalid for input of size 949818912

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(1, 32, 4971, 5971)), -1, 32, 100), **{}):
shape '[-1, 32, 100]' is invalid for input of size 949818912

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
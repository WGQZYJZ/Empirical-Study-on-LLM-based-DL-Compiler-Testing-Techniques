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
        self.conv2d0_1 = torch.nn.Conv2d(5, 2, kernel_size=(3, 5), stride=(3, 5), padding=(2, 1))
        self.conv2d1_1 = torch.nn.Conv2d(2, 5, kernel_size=(3, 5), stride=(5, 4), padding=(1, 0))
        self.conv2d0_2 = torch.nn.Conv2d(3, 2, kernel_size=(3, 4), stride=(1, 4), padding=(0, 1))
        self.conv2d1_2 = torch.nn.Conv2d(2, 4, kernel_size=(1, 5), stride=(1, 4), padding=(1, 2))
        self.conv2d2 = torch.nn.Conv2d(4, 4, kernel_size=7, stride=8, padding=1)
        self.conv2d3 = torch.nn.Conv2d(4, 5, kernel_size=9, stride=2, padding=2)

    def forward(self, x1):
        v1 = self.conv2d0_1(x1)
        v1_shape = torch.tensor(v1.shape)
        v1 = v1.reshape(5, 2, 6, 7)
        v1 = self.conv2d1_1(v1)
        v1 = v1.reshape(v1_shape)
        v2 = self.conv2d0_2(v1)
        v2_shape = torch.tensor(v2.shape)
        v2 = v2.reshape(3, 2, 7, 11)
        v2 = self.conv2d1_2(v2)
        v2 = v2.reshape(v2_shape)
        v3 = self.conv2d2(v2)
        v4 = self.conv2d3(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 5, 19, 39)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[5, 2, 6, 7]' is invalid for input of size 112

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(1, 2, 7, 8)), 5, 2, 6, 7), **{}):
shape '[5, 2, 6, 7]' is invalid for input of size 112

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
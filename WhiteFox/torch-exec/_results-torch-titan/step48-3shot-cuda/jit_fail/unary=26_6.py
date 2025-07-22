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
        super(Model, self).__init__()
        self.conv_t_1 = torch.nn.ConvTranspose2d(200, 509, kernel_size=[1, 4], stride=[2, 1], bias=False)
        self.conv_t_2 = torch.nn.ConvTranspose2d(509, 357, kernel_size=[5, 2], stride=[2, 1], bias=False)
        self.conv_t_3 = torch.nn.ConvTranspose2d(357, 200, kernel_size=[3, 2], stride=[1, 1], bias=False)

    def forward(self, input1, input2):
        v1 = self.conv_t_1(input1)
        v2 = self.conv_t_2(input2)
        v3 = self.conv_t_3((v2 + v1))
        t2 = (v3 > 0)
        t3 = (v3 * (- 1.65))
        v4 = torch.where(t2, v3, t3)
        t4 = (v4 > 0)
        t5 = (v4 * 0.5)
        v5 = torch.where(t4, v4, t5)
        return v5




func = Model().to('cuda')



input1 = torch.randn([868, 565, 1, 1])

input2 = 1

test_inputs = [input1, input2]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [200, 509, 1, 4], expected input[868, 565, 1, 1] to have 200 channels, but got 565 channels instead

jit:
Failed running call_module L__self___conv_t_1(*(FakeTensor(..., device='cuda:0', size=(868, 565, 1, 1)),), **{}):
Given transposed=1, weight of size [200, 509, 1, 4], expected input[868, 565, 1, 1] to have 200 channels, but got 565 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
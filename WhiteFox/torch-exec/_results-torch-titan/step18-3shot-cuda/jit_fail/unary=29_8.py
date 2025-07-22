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

    def __init__(self, min_value=0.5, max_value=10.9):
        super().__init__()
        self.linear = torch.nn.Linear(2, 28)
        self.sigmoid = torch.nn.Sigmoid()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 4, 1, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, input):
        v1 = self.conv_transpose(input)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.sigmoid(v3)
        v5 = self.linear(v4)
        v6 = v5.view((v5.size() + (1, 1)))
        return v6




func = Model().to('cuda')



input = torch.randn(1, 3, 64, 64)


test_inputs = [input]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (248x62 and 2x28)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 4, 62, 62)),), **{}):
a and b must have same reduction dim, but got [248, 62] X [2, 28].

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
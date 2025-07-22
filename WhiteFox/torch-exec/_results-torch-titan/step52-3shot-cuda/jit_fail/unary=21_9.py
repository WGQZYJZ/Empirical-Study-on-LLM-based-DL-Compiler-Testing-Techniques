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
        super(ModelTanh, self).__init__()
        self.conv = torch.nn.Conv2d(3, 16, (3, 7), 2)
        self.linear_1 = torch.nn.Linear((15 * 40), 10)
        self.linear_2 = torch.nn.Linear(10, 10)
        self.linear_3 = torch.nn.Linear(10, 2)
        self.tanh = torch.nn.Tanh()

    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), (- 1))
        x = self.tanh(x)
        x = self.linear_1(x)
        x = x.tanh()
        x = self.linear_2(x)
        x = self.linear_3(x)
        return x




func = ModelTanh().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x14384 and 600x10)

jit:
Failed running call_module L__self___linear_1(*(FakeTensor(..., device='cuda:0', size=(1, 14384)),), **{}):
a and b must have same reduction dim, but got [1, 14384] X [600, 10].

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
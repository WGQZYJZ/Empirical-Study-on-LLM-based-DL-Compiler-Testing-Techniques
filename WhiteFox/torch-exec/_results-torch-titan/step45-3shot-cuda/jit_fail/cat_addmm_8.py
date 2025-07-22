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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(8, 1)
        self.flatten = torch.flatten
        self.permute = torch.Tensor.transpose

    def forward(self, x):
        x = self.layers(x)
        x = self.flatten(x.transpose(0, 1), start_dim=0, end_dim=1)
        x = self.permute(x, 0, 1)
        return x




func = Model().to('cuda')



x = torch.randn(8, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (8x4 and 8x1)

jit:
Failed running call_module L__self___layers(*(FakeTensor(..., device='cuda:0', size=(8, 4)),), **{}):
a and b must have same reduction dim, but got [8, 4] X [8, 1].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.linear = nn.Linear(3, 5)
        self.conv = nn.Conv2d(12, 24, 3, stride=2, padding=1)

    def forward(self, x):
        x = self.linear(x)
        x = self.conv(x.reshape(x.shape[0], 4, (- 1)))
        x = torch.flatten(x, start_dim=1)
        return x




func = Model().to('cuda')



x = torch.randn(2, 3, 9)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (6x9 and 3x5)

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(2, 3, 9)),), **{}):
a and b must have same reduction dim, but got [6, 9] X [3, 5].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
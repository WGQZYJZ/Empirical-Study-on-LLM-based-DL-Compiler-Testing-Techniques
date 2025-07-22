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
        self.layers_1 = nn.Linear(2, 4)
        self.layers_2 = nn.Linear(2, 4)
        self.layers = nn.Linear(4, 4)

    def forward(self, x):
        print('x:', x.shape)
        x = self.layers_1(x)
        print('After layer_1:', x.shape)
        x = self.layers_2(x)
        print('After layer_2:', x.shape)
        x = self.layers(x)
        return x




func = Model().to('cuda')



x = torch.randn(2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x4 and 2x4)

jit:
Failed running call_module L__self___layers_2(*(FakeTensor(..., device='cuda:0', size=(2, 4)),), **{}):
a and b must have same reduction dim, but got [2, 4] X [2, 4].

from user code:
   File "<string>", line 27, in <resume in forward>


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
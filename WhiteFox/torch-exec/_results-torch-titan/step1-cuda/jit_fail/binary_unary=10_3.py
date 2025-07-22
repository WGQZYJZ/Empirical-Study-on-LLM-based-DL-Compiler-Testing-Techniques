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
        self.conv = torch.nn.Conv2d(50, 50, 3, stride=1, padding=1)

    def forward(self, x):
        y = self.conv(x)
        z = torch.relu(y, other='fused_add_relu')
        return z



func = Model().to('cuda')



x = torch.randn(1, 50, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
relu() got an unexpected keyword argument 'other'

jit:
Failed running call_function <built-in method relu of type object at 0x7f73370699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 50, 64, 64)),), **{'other': 'fused_add_relu'}):
relu() got an unexpected keyword argument 'other'

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
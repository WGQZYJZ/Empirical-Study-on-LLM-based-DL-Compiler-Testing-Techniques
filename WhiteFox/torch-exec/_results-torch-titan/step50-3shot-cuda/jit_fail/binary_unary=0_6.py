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
        self.conv1 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)

    def forward(self, x1, x2, x3, x4):
        v1 = self.conv1((x1 + x2))
        v2 = torch.relu(v1)
        v3 = self.conv3((x3 + x4))
        v4 = torch.relu(v3)
        v5 = self.conv2((v2 + v4))
        v6 = (v5 + v1)
        v7 = torch.relu(v6)
        return torch.nn.functional.max_pool2d(v7, kernal_size=3, stride=1, padding=1)




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)



x2 = torch.randn(1, 16, 64, 64)



x3 = torch.randn(1, 16, 64, 64)



x4 = torch.randn(1, 16, 64, 64)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
_max_pool2d() got an unexpected keyword argument 'kernal_size'

jit:
Failed running call_function <function boolean_dispatch.<locals>.fn at 0x718cd78ddca0>(*(FakeTensor(..., device='cuda:0', size=(1, 16, 64, 64)),), **{'kernal_size': 3, 'stride': 1, 'padding': 1}):
_max_pool2d() got an unexpected keyword argument 'kernal_size'

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
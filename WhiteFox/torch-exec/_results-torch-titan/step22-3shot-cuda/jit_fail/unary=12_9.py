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
        self.conv1 = torch.nn.Conv2d(3, 32, 1, stride=1, padding=2)
        self.conv2 = torch.nn.Conv2d(32, 16, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(16, 8, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = torch.conv2(v2)
        v4 = torch.sigmoid(v3)
        v5 = torch.conv3(v4)
        v6 = torch.sigmoid(v5)
        v7 = (v5 * v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
module 'torch' has no attribute 'conv2'

jit:
module 'torch' has no attribute 'conv2'

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv_transpose0 = torch.nn.ConvTranspose2d(1, 64, 9, padding=0, stride=2)
        self.conv2d0 = torch.nn.Conv2d(64, 29, 21, padding=0, stride=1)

    def forward(self, x1):
        v1 = self.conv_transpose0(x1)
        v4 = torch.avg_pool2d(v1, 3, stride=1, padding=1)
        v2 = self.conv2d0(v4)
        return v2




func = Model().to('cuda')



x1 = torch.randn(2, 1, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
module 'torch' has no attribute 'avg_pool2d'

jit:
module 'torch' has no attribute 'avg_pool2d'

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
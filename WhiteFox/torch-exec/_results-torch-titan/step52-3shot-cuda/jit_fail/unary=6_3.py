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
        self.conv = torch.nn.Conv2d(3, 32, 1, stride=2, padding=0)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = (t1 + 3)
        t3 = t2.clamp(0, 6)
        t4 = (t1 * t3)
        t5 = (t4 / 6)
        t6 = self.relu(conv)
        return t6




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'conv' is not defined

jit:
name 'conv' is not defined

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv = torch.nn.Conv2d(64, 8, 1, stride=1, padding=0)
        self.batch_norm = torch.nn.BatchNorm1d((56, 56))
        self.conv2 = torch.nn.Conv2d(8, 4, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = self.conv2(v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 64, 56, 56)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'v4' is not defined

jit:
name 'v4' is not defined

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
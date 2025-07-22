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
        self.conv = torch.nn.Conv2d(128, 64, 1)

    def forward(self, x1):
        x1 = F.softmax(x1, dim=(- 1))
        x2 = F.dropout(x1)
        x3 = self.pool(x1)
        x4 = torch.relu(x2)
        x5 = self.conv(x4)
        x6 = self.convt(x5)
        x7 = torch.relu(x6)
        return x7




func = Model().to('cuda')



x1 = torch.randn(1, 128, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'pool'

jit:
pool

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
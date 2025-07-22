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
        self.bn1 = torch.nn.BatchNorm2d(16)
        self.linear1 = torch.nn.Linear(((16 * 3) * 3), 10)

    def forward(self, x):
        v1 = self.bn1(x)
        v2 = v1.contiguous().view(v1.shape[0], (- 1))




func = Model().to('cuda')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'dim'

jit:
Failed running call_module L__self___bn1(*(1,), **{}):
'int' object has no attribute 'dim'

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
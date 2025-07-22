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
        self.fc = torch.nn.Linear((1000 * 1), 4)

    def forward(self, x1):
        v1 = x1.view((x1.shape[0], (- 1)))
        v2 = self.fc(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x3072 and 1000x4)

jit:
Failed running call_module L__self___fc(*(FakeTensor(..., device='cuda:0', size=(1, 3072)),), **{}):
a and b must have same reduction dim, but got [1, 3072] X [1000, 4].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
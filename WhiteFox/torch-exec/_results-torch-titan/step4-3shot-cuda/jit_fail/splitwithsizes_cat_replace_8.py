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

    def forward(self, x1):
        split = torch.split(x1, split_sizes=[12, 8, 95, 111], dim=3)
        v2 = torch.cat([split[i] for i in range(len(split_sizes))], dim=3)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 1, 56, 149)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
split() got an unexpected keyword argument 'split_sizes'

jit:
Failed running call_function <function split at 0x720a0056f0d0>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 56, 149)),), **{'split_sizes': [12, 8, 95, 111], 'dim': 3}):
split() got an unexpected keyword argument 'split_sizes'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
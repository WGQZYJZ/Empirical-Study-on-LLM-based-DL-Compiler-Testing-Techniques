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
        self.features = torch.nn.BatchNorm2d(32, affine=False, track_running_stats=False)

    def forward(self, v1, v2):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_tensors))], dim=1)
        return (concatenated_tensor, torch.split(v2, [1, 1, 1], dim=1))



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)
v1 = 1

test_inputs = [x1, v1]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'split'

jit:
Failed running call_function <function split at 0x7983f11faf70>(*(1, [1, 1, 1]), **{'dim': 1}):
'int' object has no attribute 'split'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
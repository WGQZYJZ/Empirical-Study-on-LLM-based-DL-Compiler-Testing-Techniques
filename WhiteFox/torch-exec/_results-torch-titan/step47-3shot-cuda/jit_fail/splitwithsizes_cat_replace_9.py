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
        self.features = torch.nn.ModuleList([torch.nn.Conv2d(3, 32, 3, 1, 1), torch.nn.Conv2d((3 * 64), 32, 3, 1, 1), torch.nn.Conv2d(32, 32, 3, 1, 2)])

    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return concatenated_tensor




func = Model().to('cuda')

v1 = 1

test_inputs = [v1]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'split'

jit:
Failed running call_function <function split at 0x7b1323eef0d0>(*(1, [1, 1, 1]), **{'dim': 1}):
'int' object has no attribute 'split'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
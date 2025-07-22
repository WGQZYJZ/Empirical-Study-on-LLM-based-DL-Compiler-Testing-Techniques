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

    def __init__(self, size):
        super().__init__()
        self.size = size

    def forward(self, x1):
        x2 = torch.cat([x1, x1], dim=1)
        x3 = x2[:, 0:9223372036854775807]
        x4 = x3[:, 0:self.size]
        x5 = torch.cat([x1, x4], dim=1)
        return x5



size = 1

func = Model(size).to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected Tensor as element 0 in argument 0, but got int

jit:
Failed running call_function <built-in method cat of type object at 0x7f389b8699e0>(*([1, 1],), **{'dim': 1}):
expected Tensor as element 0 in argument 0, but got int

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
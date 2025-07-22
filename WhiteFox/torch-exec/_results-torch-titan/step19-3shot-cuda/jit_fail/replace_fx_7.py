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

    def forward(self, x):
        w1 = torch.rand_like(x, dtype=torch.float)
        y = torch.nn.functional.dropout(x, p=0.8, training=True)
        z = (w1 + y)
        return z




func = Model().to('cuda')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
rand_like(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method rand_like of type object at 0x7e752ce699e0>(*(1,), **{'dtype': torch.float32}):
rand_like(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
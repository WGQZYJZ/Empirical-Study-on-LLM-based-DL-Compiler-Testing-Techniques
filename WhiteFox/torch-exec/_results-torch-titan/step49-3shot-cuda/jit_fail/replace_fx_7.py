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

    def forward(self, x, y):
        a = torch.rand_like(x)
        b = torch.rand_like(y)
        return 1




func = Model().to('cuda')



y1 = torch.randn(1, 2, 2)

x = 1

test_inputs = [y1, x]

# JIT_FAIL
'''
direct:
rand_like(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method rand_like of type object at 0x7039782699e0>(*(1,), **{}):
rand_like(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        z1 = torch.nn.functional.gelu(0.1)
        z2 = z1
        w1 = torch.nn.functional.dropout(z2)
        return z2




func = Model().to('cuda')



x = torch.randn(3, 4, 5)


test_inputs = [x]

# JIT_FAIL
'''
direct:
gelu(): argument 'input' (position 1) must be Tensor, not float

jit:
Failed running call_function <built-in function gelu>(*(0.1,), **{}):
gelu(): argument 'input' (position 1) must be Tensor, not float

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
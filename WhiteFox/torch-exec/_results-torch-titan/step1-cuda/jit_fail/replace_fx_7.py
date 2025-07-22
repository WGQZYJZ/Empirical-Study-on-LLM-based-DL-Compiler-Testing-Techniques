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

    def forward(self, x):
        v1 = torch.nn.functional.dropout(x, p=0.2, training=False)
        v2 = torch.rand_like(v1)
        r1 = (v1 * v2)
        r2 = r1.permute(0, 2, 1)
        r3 = torch.nn.functional.linear(r2, torch.tensor([[1.0, 0.0], [0.0, 1.0]]).T, v2.reshape((- 1)))
        return r1



func = Model().to('cuda')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
dropout(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <function dropout at 0x74a7a72df8b0>(*(1,), **{'p': 0.2, 'training': False}):
dropout(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        for loopVar1 in range(5):
            x1 = torch.nn.functional.batch_norm(x1)
        v1 = x1
        for loopVar1 in range(7):
            v1 = torch.nn.functional.batch_norm(v1)
        return torch.cat([v1, v1, v1], 1)




func = Model().to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
batch_norm() missing 2 required positional arguments: 'running_mean' and 'running_var'

jit:
Failed running call_function <function batch_norm at 0x78aa2b564b80>(*(1,), **{}):
batch_norm() missing 2 required positional arguments: 'running_mean' and 'running_var'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
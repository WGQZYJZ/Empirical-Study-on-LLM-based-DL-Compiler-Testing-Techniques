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
        self.conv = torch.nn.Conv2d(3, 3, 2)

    def forward(self, x):
        y = F.batch_norm(self.conv(x), running_mean=0.0, running_var=0.1, training=False)
        return y




func = Model().to('cuda')



x = torch.randn(1, 3, 4, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
batch_norm(): argument 'running_mean' (position 4) must be Tensor, not float

jit:
Failed running call_function <function batch_norm at 0x75f11b7a1b80>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 3, 3)),), **{'running_mean': 0.0, 'running_var': 0.1, 'training': False}):
batch_norm(): argument 'running_mean' (position 4) must be Tensor, not float

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
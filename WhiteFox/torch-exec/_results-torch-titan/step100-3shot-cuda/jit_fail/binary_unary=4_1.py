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
        self.linear = torch.nn.Linear(16, 32)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = {'other': (v1 + 1)}
        v3 = F.relu(v2).result
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 16)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
relu(): argument 'input' (position 1) must be Tensor, not dict

jit:
Failed running call_function <function relu at 0x738b697dfca0>(*({'other': FakeTensor(..., device='cuda:0', size=(1, 32))},), **{}):
relu(): argument 'input' (position 1) must be Tensor, not immutable_dict

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
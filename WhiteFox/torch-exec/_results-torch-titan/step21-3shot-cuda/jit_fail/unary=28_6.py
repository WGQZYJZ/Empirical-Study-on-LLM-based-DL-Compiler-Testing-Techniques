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
        self.linear = torch.nn.Linear(224, 224)

    def forward(self, x1, kwargs):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=kwargs['min'])
        v3 = torch.clamp_max(v2, max_value=kwargs['max'])
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, (64 * 64), 224)

kwargs = 1

test_inputs = [x1, kwargs]

# JIT_FAIL
'''
direct:
'int' object is not subscriptable

jit:
'int' object is not subscriptable

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
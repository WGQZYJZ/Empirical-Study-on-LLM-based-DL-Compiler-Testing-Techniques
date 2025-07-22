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
        linear = torch.nn.Linear(256, 128)

    def forward(self, x1):
        v1 = linear(x1)
        v2 = torch.clamp_min(v1, min_value=0)
        v3 = torch.clamp_max(v2, max_value=255)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 256)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'linear' is not defined

jit:
name 'linear' is not defined

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
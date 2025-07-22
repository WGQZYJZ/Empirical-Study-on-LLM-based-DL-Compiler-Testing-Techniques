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
        self.lin = torch.nn.Linear(28, 10)

    def forward(self, x1):
        (v1,) = self.lin.get_weight()
        v2 = torch.sum(v1)
        v3 = (v2 * other)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Linear' object has no attribute 'get_weight'

jit:
get_weight

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
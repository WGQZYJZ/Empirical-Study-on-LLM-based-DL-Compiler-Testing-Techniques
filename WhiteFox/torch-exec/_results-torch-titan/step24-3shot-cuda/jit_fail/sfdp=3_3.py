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
        self.linear = torch.nn.Linear(5, 5)

    def forward(self, x1):
        a1 = self.linear(x1)
        q_m = torch.baddbmm(self.b, self.u, self.v, transpose_b=True)
        return q_m



func = Model().to('cuda')



x1 = torch.randn(5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'b'

jit:
b

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
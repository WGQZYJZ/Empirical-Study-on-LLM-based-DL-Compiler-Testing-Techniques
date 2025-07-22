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
        self.linear = torch.nn.Linear(13, 7)

    def forward(self, x2):
        v2 = x2
        v4 = v2 * 0.5
        v6 = v4 * 0.7071067811865476
        v7 = torch.erf(v6)
        v9 = v7 + 1
        v10 = v9 * v4
        v11 = torch.add(v1, v8)
        return v10


func = Model().to('cpu')


x2 = torch.randn(19, 13)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
name 'v1' is not defined

jit:
NameError: name 'v1' is not defined

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
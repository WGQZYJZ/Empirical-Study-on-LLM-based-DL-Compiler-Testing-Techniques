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

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(6, 1)

    def forward(self, x):
        l1 = self.linear(x)
        l2 = clamp(l1, min=0, max=6) + 3
        l3 = l2 / 6
        return l3


func = Model().to('cpu')


x = torch.randn(1, 6)

test_inputs = [x]

# JIT_FAIL
'''
direct:
name 'clamp' is not defined

jit:
NameError: name 'clamp' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
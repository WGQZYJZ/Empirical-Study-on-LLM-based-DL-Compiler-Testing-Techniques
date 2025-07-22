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
        v1 = linear1(x1)
        v2 = v1 - x1
        v3 = linear2(v1)
        v4 = linear3(v3 + v2)
        v5 = linear4(v3 + v2) + v4
        v6 = linear5(v5)
        return v6


func = Model().to('cpu')


x1 = torch.randn(1, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'linear1' is not defined

jit:
NameError: name 'linear1' is not defined

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.linear = torch.nn.Linear(in_features=25, out_features=16)

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = v1 + x2
        v3 = __torch__.torch.relu(v2)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 25)

x2 = torch.randn(1, 16)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
name '__torch__' is not defined

jit:
NameError: name '__torch__' is not defined

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        return relu(v1, other)


func = Model().to('cpu')


x1 = torch.randn(1, 3)

x2 = torch.randn(1, 8)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
name 'relu' is not defined

jit:
NameError: name 'relu' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
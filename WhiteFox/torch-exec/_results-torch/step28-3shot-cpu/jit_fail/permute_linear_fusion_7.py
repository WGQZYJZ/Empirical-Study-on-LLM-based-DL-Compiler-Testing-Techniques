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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.reshape(1, 1, 2, x1.size(2) * x1.size(3))
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v2 = torch.tanh(v2)
        x2 = torch.nn.functional.threshold(v2, -0.8, 0.8, False)
        v4 = x2 * x2
        v3 = torch.nn.functional.linear(v1, self.linear.weight * 2, self.linear.bias)
        v3 = v3 + x2
        return v2 + v3



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-3, 2], but got 3)

jit:
IndexError: tuple index out of range

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
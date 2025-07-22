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
        self.linear = torch.nn.Linear(10, 7)

    def forward(self, x, other=torch.empty(1)):
        v1 = self.linear(x)
        if (other.shape[1] != 1):
            raise ValueError
        v2 = (v1 + other)
        v3 = torch.relu(v2)
        return v3



func = Model().to('cuda')



x = torch.randn(1, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
tuple index out of range

jit:
list index out of range

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
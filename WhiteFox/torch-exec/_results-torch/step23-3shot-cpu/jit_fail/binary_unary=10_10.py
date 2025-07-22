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
        self.linear1 = torch.nn.Linear(2, 2)

    def forward(self, x):
        v1 = self.linear1(x)
        v2 = v1 + other_tensor
        v3 = torch.relu(v2)
        return v3


func = Model().to('cpu')


x = torch.randn(1, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
name 'other_tensor' is not defined

jit:
NameError: name 'other_tensor' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
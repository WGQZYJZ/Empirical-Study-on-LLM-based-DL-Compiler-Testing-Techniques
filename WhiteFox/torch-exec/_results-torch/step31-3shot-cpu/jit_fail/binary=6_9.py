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
        self.Linear = torch.nn.Linear(67, 33)

    def forward(self, x1):
        v1 = self.Linear(x1)
        v2 = v1 - other
        return



func = Model().to('cpu')


x1 = torch.randn(1, 67)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'other' is not defined

jit:
NameError: name 'other' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
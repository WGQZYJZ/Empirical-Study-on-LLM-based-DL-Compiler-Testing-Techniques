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

    def forward(self, x1, x2):
        v1 = x1 * x2
        return v1 + other



func = Model().to('cpu')


x1 = torch.randn(1, 2, 3, 2)

x2 = torch.randn(1, 2, 3, 2)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
name 'other' is not defined

jit:
NameError: name 'other' is not defined

from user code:
   File "<string>", line 17, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def forward(self, x):
        y = x.clone()
        y[1.0, 1.0, 0.0] = 2.0
        return y



func = Model().to('cpu')


x = torch.randn(2, 2, 2)

test_inputs = [x]

# JIT_FAIL
'''
direct:
only integers, slices (`:`), ellipsis (`...`), None and long or byte Variables are valid indices (got float)

jit:
backend='inductor' raised:
IndexError: only integers, slices (`:`), ellipsis (`...`), None and long or byte Variables are valid indices (got float)

While executing %setitem : [num_users=0] = call_function[target=operator.setitem](args = (%y, (1.0, 1.0, 0.0), 2.0), kwargs = {})
Original traceback:
  File "<string>", line 20, in forward



You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def forward(self, x, z):
        y = x.view(x.size(1), (- 1))
        y = (z * z)
        y = y.sum().mean()
        return y




func = Model().to('cuda')



x = torch.randn(2, 10, 20)

z = 1

test_inputs = [x, z]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'sum'

jit:
'int' object has no attribute 'sum'

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
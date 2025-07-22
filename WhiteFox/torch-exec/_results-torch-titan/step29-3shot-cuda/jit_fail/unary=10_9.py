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
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(800, 400)

    def forward(self, x2):
        v7 = F.relu(self.linear(x2))
        v8 = (v7 + 3)
        v9 = F.relu(0, 6)
        v10 = (v9 / 6)



func = Model().to('cuda')



x2 = torch.randn(1, 800)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
relu_(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <function relu at 0x796dfaf9fca0>(*(0, 6), **{}):
relu_(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
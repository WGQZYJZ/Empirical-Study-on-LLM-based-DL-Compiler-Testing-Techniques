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

    def forward(self, x1):
        v1 = torch.cat((x1, x1), dim=1)
        v2 = v1.shape[0]
        v3 = torch.relu(v2)
        return v3.view((- 1))




func = Model().to('cuda')



x1 = torch.randn(1, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
relu(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <built-in method relu of type object at 0x7efc634699e0>(*(1,), **{}):
relu(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
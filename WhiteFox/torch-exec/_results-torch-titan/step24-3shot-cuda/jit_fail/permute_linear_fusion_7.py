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
        x2 = torch.relu(torch.tanh(x1))
        x2 = x2.squeeze(dim=(- 1))
        x3 = x2.permute(0, 2, 1)
        x3 = x3.squeeze(dim=(- 1))
        return torch.nn.functional.softmax(torch.nn.functional.linear(x3, self.linear.weight, self.linear.bias), dim=(- 1))




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'linear'

jit:
linear

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
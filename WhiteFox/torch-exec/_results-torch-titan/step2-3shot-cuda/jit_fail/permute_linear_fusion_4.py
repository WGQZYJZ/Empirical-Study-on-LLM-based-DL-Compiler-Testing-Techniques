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
        self.linear = torch.nn.Linear(3, 3)

    def forward(self, x1):
        return torch.nn.functional.fold(x1.view((- 1), x1.size()[(- 3)], x1.size()[(- 1)]), x_size=x1.size()[(- 2):], kernel_size=self.linear.weight.shape[0], stride=self.linear.weight.shape[0], dilation=self.linear.weight.shape[0])



func = Model().to('cuda')



x1 = torch.randn(1, 1, 4, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
fold() got an unexpected keyword argument 'x_size'

jit:
Failed running call_function <function fold at 0x76aa8b278ca0>(*(FakeTensor(..., device='cuda:0', size=(4, 1, 4)),), **{'x_size': (4, 4), 'kernel_size': 3, 'stride': 3, 'dilation': 3}):
fold() got an unexpected keyword argument 'x_size'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
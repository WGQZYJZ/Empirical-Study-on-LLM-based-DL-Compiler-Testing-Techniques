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
        self.linear = torch.nn.Linear(48, 16, bias=True)

    def forward(self, x1, x2):
        v1 = self.linear(x1, other=x2)
        return v1



func = Model().to('cuda')



x1 = torch.randn(1, 48)



x2 = torch.randn(1, 48)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() got an unexpected keyword argument 'other'

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 48)),), **{'other': FakeTensor(..., device='cuda:0', size=(1, 48))}):
forward() got an unexpected keyword argument 'other'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
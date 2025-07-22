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
        self.dropout = nn.Dropout2d()

    def forward(self, x1, x2):
        x3 = self.dropout(x1, p=0.5)
        x4 = self.dropout(x2, p=0.3)
        x5 = (x3 * x4).sum((- 1))
        return x5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 3, requires_grad=True)



x2 = torch.randn(1, 3, 3, requires_grad=True)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() got an unexpected keyword argument 'p'

jit:
Failed running call_module L__self___dropout(*(FakeTensor(..., device='cuda:0', size=(1, 3, 3)),), **{'p': 0.5}):
forward() got an unexpected keyword argument 'p'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
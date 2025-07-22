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
        self.fc = torch.nn.Linear((((3 * 4) * 4) * 4), 128)

    def forward(self, x1, x2, x3, x4):
        v1 = torch.concat((x1, x2, x3, x4))
        v2 = v1.view((- 1), (((3 * 4) * 4) * 4))
        v3 = self.linear(v2)
        v4 = torch.sigmoid(v3)
        return v4



func = Model().to('cuda')



x1 = torch.randn(4, 3, 4, 4)



x2 = torch.randn(4, 3, 4, 4)



x3 = torch.randn(4, 3, 4, 4)



x4 = torch.randn(4, 3, 4, 4)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'linear'

jit:
linear

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
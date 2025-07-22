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
        self.conv = torch.nn.Conv2d(2, 5, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 - [0.5561, 1])
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 2, 21, 21)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
unsupported operand type(s) for -: 'Tensor' and 'list'

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(1, 5, 23, 23)), [0.5561, 1]), **{}):
unsupported operand type(s) for -: 'FakeTensor' and 'immutable_list'

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
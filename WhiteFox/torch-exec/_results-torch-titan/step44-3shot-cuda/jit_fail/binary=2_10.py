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
        self.conv = torch.nn.Conv3d(1, 10, (2, 3, 4), stride=2, padding=2)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 - '42.0')
        return v2




func = Model().to('cuda')



x = torch.randn(1, 1, 3, 4, 5)


test_inputs = [x]

# JIT_FAIL
'''
direct:
unsupported operand type(s) for -: 'Tensor' and 'str'

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(1, 10, 3, 3, 3)), '42.0'), **{}):
unsupported operand type(s) for -: 'FakeTensor' and 'str'

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
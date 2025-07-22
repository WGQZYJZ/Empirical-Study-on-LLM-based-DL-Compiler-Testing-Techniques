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
        self.conv = torch.nn.Conv2d(3, 8, kernel_size=(1, 1), padding=(2, 1), stride=(4, 1))

    def forward(self, x3):
        v1 = self.conv(x3)
        v2 = (v1 - 'foo')
        return v2




func = Model().to('cuda')



x3 = torch.randn(1, 3, 100, 100)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
unsupported operand type(s) for -: 'Tensor' and 'str'

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 26, 102)), 'foo'), **{}):
unsupported operand type(s) for -: 'FakeTensor' and 'str'

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def __init__(self, s):
        super().__init__()
        self.s = s
        self.m = 10
        self.l = [self.m, 2, 10]

    def forward(self, x1):
        x2 = torch.nn.functional.dropout(self.s, p=0.5)
        x3 = torch.nn.functional.dropout(self.l, p=0.5)
        x3 += 2
        return x2



s = 1

func = Model(s).to('cuda')



x1 = torch.randn(3, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
dropout(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <function dropout at 0x75ed05ca08b0>(*(1,), **{'p': 0.5}):
dropout(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
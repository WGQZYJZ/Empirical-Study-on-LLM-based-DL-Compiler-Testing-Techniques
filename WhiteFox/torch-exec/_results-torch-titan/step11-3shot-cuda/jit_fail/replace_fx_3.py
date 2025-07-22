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



class m1(torch.nn.Module):

    def __init__(self, n):
        super().__init__()
        self.n = n

    def forward(self, x):
        a1 = torch.nn.functional.dropout(x, p=0)
        a2 = self.n
        a2 = torch.nn.functional.dropout(a2, p=0)
        return a1



n = 1
func = m1(1).to('cuda')



x1 = torch.randn(1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
dropout(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_function <function dropout at 0x73de8515d8b0>(*(1,), **{'p': 0}):
dropout(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
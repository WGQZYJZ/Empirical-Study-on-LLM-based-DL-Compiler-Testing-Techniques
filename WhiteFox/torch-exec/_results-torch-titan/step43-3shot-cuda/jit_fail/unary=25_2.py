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
        self.linear = torch.nn.Linear(8, 8)

    def forward(self, x1):
        t1 = self.linear(x1)
        t2 = (t1 > 0)
        t3 = (t1 * negative_slope)
        t4 = torch.where(t2, t1, t3)
        return t4



func = Model().to('cuda')



__input__ = torch.randn(1, 8)


test_inputs = [__input__]

# JIT_FAIL
'''
direct:
name 'negative_slope' is not defined

jit:
name 'negative_slope' is not defined

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
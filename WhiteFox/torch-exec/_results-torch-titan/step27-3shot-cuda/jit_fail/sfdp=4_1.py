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
        self.query = torch.nn.Linear(8, 8)
        self.key = torch.nn.Linear(8, 8)
        self.value = torch.nn.Linear(8, 8)

    def forward(self, x1):
        q = self.query(x1)
        k = self.key(x1)
        v = self.value(x1)
        k = (k / math.sqrt(k.size((- 1))))
        qk = (q @ k.transpose((- 2), (- 1)))
        qk = (qk + attn_mask)
        a = torch.softmax(qk, dim=(- 1))
        o = (a @ v)
        return o



func = Model().to('cuda')



x1 = torch.randn(12, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'attn_mask' is not defined

jit:
name 'attn_mask' is not defined

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.query = torch.nn.Linear(128, 128)
        self.key = torch.nn.Linear(128, 128)
        self.value = torch.nn.Linear(128, 128)

    def forward(self, x1, x2, x3):
        qk = (self.query(x1) @ self.key(x2).transpose((- 2), (- 1)))
        qk = (self.qk + x3)
        attn_weight = torch.softmax(qk, dim=(- 1))
        output = (attn_weight @ self.value(x1))
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 128)



x2 = torch.randn(1, 128)



x3 = torch.randn(1, 1, 128)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'qk'

jit:
qk

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
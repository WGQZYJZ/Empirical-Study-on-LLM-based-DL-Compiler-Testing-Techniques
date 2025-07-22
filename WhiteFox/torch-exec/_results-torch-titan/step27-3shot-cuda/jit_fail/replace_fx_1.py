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



class model(torch.nn.Module):

    def __init__(self, p):
        super().__init__()
        self.p = p
        self.dropout_1 = torch.nn.Dropout(p=self.p)
        self.dropout_2 = torch.nn.Dropout(p=self.p)
        self.dropout_3 = torch.nn.Dropout(p=self.p)

    def forward(self, x):
        v1 = self.dropout_1(1)
        v2 = self.dropout_2(2)
        v3 = self.dropout_3(3)
        out = (((x + v1) + v2) + v3)
        return out



p = 1

func = model(p).to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
dropout(): argument 'input' (position 1) must be Tensor, not int

jit:
Failed running call_module L__self___dropout_1(*(1,), **{}):
dropout(): argument 'input' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
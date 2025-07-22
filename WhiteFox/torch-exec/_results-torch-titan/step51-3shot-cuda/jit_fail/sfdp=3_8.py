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
        self.dropout = torch.nn.Dropout(0.5)
        self.q_proj = torch.nn.Linear(16, 32)
        self.k_proj = torch.nn.Linear(24, 32)
        self.v_proj = torch.nn.Linear(40, 32)
        self.scale_factor = math.sqrt((16 / 576))

    def forward(self, query, key, value, padding_mask):
        q = self.q_proj(query)
        k = self.k_proj(key)
        v = self.v_proj(value)
        dot = torch.matmul(q, k.transpose((- 2), (- 1)))
        dot = (dot * self.scale_factor)
        dot_mask = dot.masked_fill(padding_mask, (- float('inf')))
        softmax = F.softmax(dot_mask, dim=(- 1))
        dropout = self.dropout(softmax)
        ouput = torch.matmul(dropout, v)
        return output




func = Model().to('cuda')



query = torch.randn(16, 16)



key = torch.randn(16, 24)



value = torch.randn(16, 40)




padding_mask = torch.empty(16, 16, dtype=torch.bool).bernoulli_(0.5)


test_inputs = [query, key, value, padding_mask]

# JIT_FAIL
'''
direct:
name 'output' is not defined

jit:
name 'output' is not defined

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
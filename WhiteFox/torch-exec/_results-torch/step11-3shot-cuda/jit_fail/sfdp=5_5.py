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

    def __init__(self, hidden_dims, dropout_p):
        super().__init__()
        self.attn_mask = torch.tril(torch.randn(1, hidden_dims, hidden_dims))
        self.attn_mask = self.attn_mask.triu(diagonal=1)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, input):
        q = k = input
        attn = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
        attn = attn + self.attn_mask
        attn = self.dropout(attn)
        out = attn @ v
        return out


hidden_dims = 1
dropout_p = 1
func = Model(16, 0.1).to('cuda')


input = torch.randn(1, 16, 16)

test_inputs = [input]

# JIT_FAIL
'''
direct:
name 'v' is not defined

jit:
NameError: name 'v' is not defined

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
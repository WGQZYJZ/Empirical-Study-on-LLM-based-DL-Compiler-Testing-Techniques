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

    def __init__(self, hidden):
        super().__init__()
        self.linear_query = torch.nn.Linear(3, hidden)
        self.linear_key = torch.nn.Linear(3, hidden)
        self.linear_value = torch.nn.Linear(3, hidden)
        self.attn_drop = nn.Dropout(0.0)
        self.proj = torch.nn.Linear(hidden, 3)

    def forward(self, x1, x2):
        v1 = self.linear_query(x1)
        v2 = self.linear_key(x2)
        v3 = self.linear_value(x2)
        qk = q @ k.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk += attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn = attn_weight @ v
        attn = self.attn_drop(attn)
        output = self.proj(attn)
        return (output, v, attn_weight)


hidden = 1
func = Model(3).to('cuda')


x1 = torch.randn(3, 3)

x2 = torch.randn(3, 3)

attn_mask = torch.zeros(3, 3)

test_inputs = [x1, x2, attn_mask]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''
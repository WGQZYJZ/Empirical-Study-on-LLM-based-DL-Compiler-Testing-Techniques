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

    def __init__(self, in_dim: int, out_dim: int, nhead: int, window_size: int, dropout: float, use_bias: bool=True):
        super().__init__()
        self.in_proj_weight = torch.nn.Parameter(torch.empty(nhead, in_dim, window_size))
        if use_bias:
            self.in_proj_bias = torch.nn.Parameter(torch.empty(nhead, in_dim * window_size))
        else:
            self.register_parameter('in_proj_bias', None)
        self.out_proj_weight = torch.nn.Parameter(torch.empty(nhead, in_dim, window_size))
        if use_bias:
            self.out_proj_bias = torch.nn.Parameter(torch.empty(nhead, out_dim))
        else:
            self.register_parameter('out_proj_bias', None)
        self.reset_parameters()

    def reset_parameters(self):
        stdv = 1.0 / math.sqrt(self.in_proj_weight.size(1))
        self.in_proj_weight.data.uniform_(-stdv, stdv)
        if self.in_proj_bias is not None:
            self.in_proj_bias.data.zero_()
        self.out_proj_weight.data.uniform_(-stdv, stdv)
        if self.out_proj_bias is not None:
            self.out_proj_bias.data.zero_()

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, key_padding_mask: torch.Tensor, need_weights: bool=True):
        r


in_dim = 1
out_dim = 1
nhead = 1
window_size = 1
dropout = 1

func = Model(in_dim, out_dim, nhead, window_size, dropout).to('cpu')

query = 1
key = 1
value = 1
key_padding_mask = 1

test_inputs = [query, key, value, key_padding_mask]

# JIT_FAIL
'''
direct:
name 'r' is not defined

jit:
NameError: name 'r' is not defined

from user code:
   File "<string>", line 39, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
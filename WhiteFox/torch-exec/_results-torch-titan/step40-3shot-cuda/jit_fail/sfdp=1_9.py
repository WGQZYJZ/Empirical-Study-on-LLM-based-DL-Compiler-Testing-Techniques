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

    def __init__(self, n_head, d_model, dropout_p=0, bias=True, pad=False):
        super().__init__()
        self.n_head = n_head
        self.d_model = d_model
        self.dropout_p = dropout_p
        self.bias = bias
        self.pad = pad
        self.inner_dims = (d_model // n_head)
        self.proj_factor = (self.inner_dims ** (- 0.5))
        self.proj_value = torch.nn.Linear(self.inner_dims, self.inner_dims, bias=bias)
        self.proj_query = torch.nn.Linear(self.inner_dims, self.inner_dims, bias=bias)
        self.proj_out = torch.nn.Linear(self.d_model, self.d_model, bias=bias)

    def forward(self, x):
        (n_batch, len_seq, _) = x.size()
        x_reshape = x.view((n_batch * len_seq), self.n_head, self.inner_dims)
        x_query = self.proj_query(x_reshape)
        x_key = self.proj_key(x_reshape)
        x_value = self.proj_value(x_reshape)
        x_query = x_query.view((n_batch * len_seq), (self.n_head * self.inner_dims))
        x_query = x_query.view(n_batch, (len_seq * self.n_head), self.inner_dims)
        x_key = x_key.view((n_batch * len_seq), (self.n_head * self.inner_dims))
        x_value = x_value.view((n_batch * len_seq), (self.n_head * self.inner_dims))
        x_attn = x_query.view(((n_batch * len_seq) * self.n_head), self.inner_dims, 1)
        x_prod = torch.matmul(x_attn, x_key.transpose(1, 2).view(((n_batch * len_seq) * self.n_head), self.inner_dims, (self.n_head * self.inner_dims)))
        x_prod = x_prod.view(n_batch, (len_seq * self.n_head), self.inner_dims, (self.n_head * self.inner_dims))
        x_prod = (x_prod / self.proj_factor)
        x_prod = torch.matmul(x_prod, x_value.view(n_batch, (len_seq * self.n_head), self.inner_dims, self.inner_dims).transpose(2, 3))
        x_prod = x_prod.view(((n_batch * len_seq) * self.n_head), self.inner_dims)
        x_out = torch.nn.functional.dropout(x_prod, (1 - self.dropout_p))
        x_out = x_out.view(n_batch, (len_seq * self.n_head), self.inner_dims)
        x_out = x_out.view(n_batch, len_seq, self.d_model)
        output = self.proj_out(x_out)
        return output



n_head = 1
d_model = 1
func = Model(n_head, d_model, dropout_p).to('cuda')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'size'

jit:
'int' object has no attribute 'size'

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
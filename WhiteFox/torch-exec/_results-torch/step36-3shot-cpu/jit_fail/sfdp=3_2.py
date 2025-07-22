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

    def __init__(self, n_head, d_model, d_k, d_v):
        super().__init__()
        self.n_head = n_head
        self.d_k = d_k
        self.d_v = d_v
        self.scale_factor = 1 / math.sqrt(d_k)
        self.dropout_p = 0.1
        weight_list = []
        for i in range(n_head):
            for j in range(d_v):
                weight = torch.nn.Parameter(torch.randn(d_model, 1, d_k))
                weight_list.append(weight)
        self.weight_list = torch.nn.ParameterList(weight_list)

    def forward(self, q, k, v):
        new_q = None
        new_k = None
        new_v = None
        for i in range(self.n_head):
            q_i_reshape = q[i:q.shape[0]:self.n_head]
            k_i_reshape = k[i:k.shape[0]:self.n_head]
            v_i_reshape = v[i:v.shape[0]:self.n_head]
            k_i_transpose = torch.transpose(k_i_reshape, 1, 2)
            new_k_i = torch.matmul(q_i_reshape, k_i_transpose) * self.scale_factor
            k_i_transpose = torch.transpose(k_i_reshape, 1, 2)
            new_v_i = torch.matmul(q_i_reshape, k_i_transpose)
            if i == 0:
                new_q = q_i_reshape
                new_k = new_k_i
                new_v = new_v_i
            else:
                new_q = torch.cat([new_q, q_i_reshape], 2)
                new_k = torch.cat([new_k, new_k_i], 2)
                new_v = torch.cat([new_v, new_v_i], 2)
        softmax = torch.nn.Softmax(dim=2)
        dropout = torch.nn.Dropout(self.dropout_p)
        softmax_qk = softmax(new_k)
        dropout_qk = dropout(softmax_qk)
        output = torch.matmul(dropout_qk, new_v)
        return output


n_head = 2
d_model = 512
d_k = 64
d_v = 64
func = Model(n_head, d_model, d_k, d_v).to('cpu')


d_model = 512
seq_len = 8
n_batch = 1
q = torch.randn(n_batch, seq_len, d_model)

d_model = 512
seq_len = 8
n_batch = 1
k = torch.randn(n_batch, seq_len, d_model)

d_model = 512
seq_len = 8
n_batch = 1
v = torch.randn(n_batch, seq_len, d_model)

test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 2. Expected size 1 but got size 0 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7f0cc8f96ec0>(*([FakeTensor(..., size=(1, 8, 512)), FakeTensor(..., size=(0, 8, 512))], 2), **{}):
Sizes of tensors must match except in dimension 2. Expected 1 in dimension 0 but got 0 for tensor number 1 in the list

from user code:
   File "<string>", line 46, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
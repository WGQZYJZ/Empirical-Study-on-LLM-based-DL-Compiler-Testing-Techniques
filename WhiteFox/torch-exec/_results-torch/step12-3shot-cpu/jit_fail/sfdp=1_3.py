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

    def __init__(self, n_head, d_model, d_query_key, d_value, dropout_p=0.1, inv_scale_factor=1.0):
        super().__init__()
        self.n_head = n_head
        self.d_model = d_model
        self.d_query_key = d_query_key
        self.d_value = d_value
        self.dropout_p = dropout_p
        self.inv_scale_factor = inv_scale_factor
        self.weight_query = torch.nn.Parameter(torch.FloatTensor(n_head, d_query_key, int(d_model / d_query_key)))
        self.weight_value = torch.nn.Parameter(torch.FloatTensor(n_head, d_query_key, int(d_model / d_query_key)))

    def forward(self, query, key, value):
        q = torch.matmul(query, self.weight_query).view([query.size(0), query.size(1), self.n_head, self.d_query_key])
        k = torch.matmul(key, self.weight_query).view([key.size(0), key.size(1), self.n_head, self.d_query_key])
        v = torch.matmul(value, self.weight_value).view([value.size(0), value.size(1), self.n_head, self.d_query_key])
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v)
        output = output.reshape([query.size(0), query.size(1), -1])
        return output


n_head = 1
d_model = 1
d_query_key = 1
d_value = 1
func = Model(n_head, d_model, d_query_key, d_value).to('cpu')

query = 1
key = 1
value = 1

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
matmul(): argument 'input' (position 1) must be Tensor, not int

jit:
matmul(): argument 'input' (position 1) must be Tensor, not int
'''
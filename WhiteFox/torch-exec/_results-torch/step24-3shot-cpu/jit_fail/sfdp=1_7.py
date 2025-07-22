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

    def __init__(self, query, key, value, inv_scale_factor, dropout_p):
        super().__init__()
        self.key_transpose = key.transpose(-2, -1)
        self.inv_scale_factor = inv_scale_factor
        self.dropout_p = dropout_p

    def forward(self, query):
        qk = torch.matmul(query, self.key_transpose)
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = dropout(softmax_qk, self.dropout_p)
        output = torch.matmul(dropout_qk, value)
        return output


query = torch.randn(32, 128, 25)
key = torch.randn(32, 32, 128)
value = torch.randn(32, 32, 128)
inv_scale_factor = torch.randn(32, 1, 25)
dropout_p = 0.8
func = Model(query, key, value, inv_scale_factor, dropout_p).to('cpu')


key = torch.randn(32, 32, 128)

query = torch.randn(32, 128, 25)

inv_scale_factor = torch.randn(32, 1, 25)

x1 = torch.randn(32, 25, 128)

test_inputs = [key, query, inv_scale_factor, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 5 were given

jit:
forward() takes 2 positional arguments but 5 were given
'''
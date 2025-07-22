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

    def __init__(self, n_heads, value_size, dropout_p):
        super().__init__()
        self.n_heads = n_heads
        self.value_size = value_size
        self.dropout_p = dropout_p
        self.softmax_d = Softmax(dim=1)
        self.dropout = Dropout(dropout_p)

    def forward(self, query, key, value, scale_factor):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk * scale_factor
        softmax_qk = self.softmax_d(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        qo = dropout_qk.matmul(value)
        return qo

class Model(torch.nn.Module):

    def __init__(self, n_heads, value_size, dropout_p):
        super().__init__()
        self.n_heads = n_heads
        self.value_size = value_size
        self.dropout_p = dropout_p
        self.weight = Parameter(torch.Tensor(1, n_heads, value_size, value_size))
        self.softmax_q = Softmax(dim=1)
        self.softmax_d = Softmax(dim=3)
        self.dropout = Dropout(dropout_p)
        self.softmax_v = Softmax(dim=2)

    def forward(self, query, key, value, scale_factor):
        wq = torch.matmul(query, self.weight)
        qk = torch.matmul(wq, key.transpose(-2, -1))
        scaled_qk = qk * scale_factor
        softmax_qk = self.softmax_q(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        dv = dropout_qk.matmul(value)
        softmax_dv = self.softmax_d(dv)
        dropout_dv = self.dropout(softmax_dv)
        softmax_dropout_dv = self.softmax_v(dropout_dv)
        output = softmax_dropout_dv.mul(dv)
        return output


n_heads = 1
value_size = 1
dropout_p = 1
func = Model(config.num_heads, config.hidden_dims, config.dropout_p).to('cpu')


query = torch.randn(1, 100, 50)

key = torch.randn(1, 100, 40)

value = torch.randn(1, 100, 40)
scale_factor = 1

test_inputs = [query, key, value, scale_factor]

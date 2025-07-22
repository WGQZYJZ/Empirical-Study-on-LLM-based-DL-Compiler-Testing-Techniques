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

    def __init__(self, query_dim, key_dim, value_dim):
        super().__init__()
        self.query_proj = nn.Linear(query_dim, key_dim, bias=False)
        self.key_proj = nn.Linear(key_dim, query_dim, bias=False)
        self.v = torch.rand(key_dim, value_dim)
        self.register_buffer('scale_factor', torch.sqrt_inv(torch.reshape(torch.rand(query_dim), (key_dim,))))
        self.softmax = torch.nn.Softmax(dim=-1)

    def forward(self, query, key):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        return dropout_qk.matmul(self.v)


query_dim = 1
key_dim = 1
value_dim = 1

func = Model(query_dim, key_dim, value_dim).to('cpu')


query = torch.randn(2, 8)

key = torch.randn(2, 8)

test_inputs = [query, key]

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

    def __init__(self, query, key, value):
        super().__init__()
        self.q_key = torch.nn.Linear(query_size, key_size, bias=False)
        self.v = torch.nn.Linear(value_size, output_size)
        self.qk_norm = 1024 ** (-0.5)
        self.dropout = torch.nn.Dropout(dropout_p, _mode='2d')

    def compute_attention(self, q, k, v):
        qk = self.q_key(q).transpose(-2, -1)
        qk = qk / self.qk_norm
        scaled_qk = torch.matmul(qk, k)
        softmax_qk = scaled_qk.softmax(dim=-1)
        return (self.dropout(softmax_qk), torch.matmul(softmax_qk, v))

    def forward(self, q, k, v):
        (attention, val) = self.compute_attention(q, k, v)
        output = self.v(val)
        return output


query = 1
key = 1
value = 1

func = Model(query, key, value).to('cpu')

q = 1
k = 1
v = 1

test_inputs = [q, k, v]

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

    def __init__(self, d_model, nhead, dropout=0.1):
        super().__init__()
        hidden_dims = d_model // nhead
        self.attention = torch.nn.MultiheadAttention(hidden_dims, nhead, dropout=dropout)

    def forward(self, query, key, value, scale_factor=1.0):
        qk = torch.matmul(query, key.transpose(-2, -1))
        inv_scale_factor = 1.0 / scale_factor
        scale_factor = inv_scale_factor
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


d_model = 1
nhead = 1
func = Model(d_model, nhead, dropout).to('cpu')

query = 1
key = 1
value = 1

test_inputs = [query, key, value]

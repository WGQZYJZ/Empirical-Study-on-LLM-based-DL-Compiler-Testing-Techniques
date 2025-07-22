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

    def __init__(self, num_qkv, num_heads, dropout_p, inv_scale_factor):
        super().__init__()
        self.query = torch.nn.Dense(num_qkv, num_qkv)
        self.key = torch.nn.Dense(num_qkv, num_qkv)
        self.value = torch.nn.Dense(num_qkv, num_qkv)
        self.inv_scale_factor = inv_scale_factor
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, x1):
        q = self.query(x1)
        k = self.key(x1)
        v = self.value(x1)
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(v)
        return output


num_qkv = 1
num_heads = 1
dropout_p = 1
inv_scale_factor = 1

func = Model(num_qkv, num_heads, dropout_p, inv_scale_factor).to('cpu')


x1 = torch.randn(1, 10)

test_inputs = [x1]

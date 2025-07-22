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

    def __init__(self, query, key, value, dropout_p, inv_scale_factor):
        super().__init__()
        self.matmul1 = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        self.dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        self.matmul2 = torch.matmul(self.dropout_qk, value)

    def forward(self, q, k, v):
        v1 = self.matmul1(q, k.transpose((- 2), (- 1)))
        v2 = (v1 / inv_scale_factor)
        v3 = v2.softmax(dim=(- 1))
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        v5 = self.matmul2(v4, v)
        return v5




query = torch.randn(batch_size, num_heads, query_sequence_length, head_size)


key = torch.randn(batch_size, num_heads, key_sequence_length, head_size)


value = torch.randn(batch_size, num_heads, key_sequence_length, head_size)

dropout_p = 1
inv_scale_factor = 1
func = Model(query, key, value, dropout_p, inv_scale_factor).to('cuda')

q = 1
k = 1
v = 1

test_inputs = [q, k, v]

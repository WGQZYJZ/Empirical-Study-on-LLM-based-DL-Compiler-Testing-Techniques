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

    def __init__(self, dim, num_heads, batch_size):
        super().__init__()
        self.mha_query = torch.nn.Linear(dim, dim)
        self.mha_key = torch.nn.Linear(dim, dim)
        self.mha_value = torch.nn.Linear(dim, dim)
        self.mha_scale_factor = (1 / math.sqrt(dim))
        self.dropout_p = 0.1

    def forward(self, x1):
        batch_size = x1.size(0)
        query = x1
        key = x1.transpose(0, 1)
        value = x1
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.mha_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output



dim = 1
num_heads = 1
batch_size = 1
func = Model(256, 4, 1).to('cuda')



x1 = torch.randn(1, 256, 8, 8)



x2 = torch.randn(256, 256, 8, 8)



x3 = torch.randn(256, 256, 8, 8)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''
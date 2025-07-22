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

    def __init__(self, num_heads, key_dim, dropout_p):
        super(Model, self).__init__()
        self.embedding = np.float32(np.random.normal(loc=0.0, scale=0.01, size=(64, num_heads, key_dim)).astype(np.float32))
        self.query = torch.randn(1, 3, 64)
        self.key = None
        self.value = None
        self.scale_factor = (1.0 / np.sqrt(key_dim))
        self.dropout_p = dropout_p

    def forward(self):
        self.key = torch.tensor(self.embedding)
        self.value = torch.tensor(self.embedding)
        qk = torch.matmul(self.query, self.key.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = value.matmul(dropout_qk)
        return output



num_heads = 1
key_dim = 1
dropout_p = 1
func = Model(2, 3, 0.0).to('cuda')

input_tensor = torch.randn(1, 1, 1)

test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
forward() takes 1 positional argument but 2 were given

jit:
forward() takes 1 positional argument but 2 were given
'''
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

    def __init__(self):
        super().__init__()
        self.dropout_p = 0.0

    def forward(self, query, key, value, invscale_factor):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(invscale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout)
        output = dropout_qk.matmul(value)
        return (output, dropout_qk)


func = Model().to('cpu')


shape = (1, 128, 5)
query = torch.randn(shape)

shape = (1, 128, 5)
key = torch.randn(shape)

shape = (1, 128, 5)
value = torch.randn(shape)
shape = (1, 128, 5)
shape = (1, 128, 5)

invscale_factor = torch.randn(shape[0], shape[1], 1)

test_inputs = [query, key, value, invscale_factor]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'dropout'

jit:
'Model' object has no attribute 'dropout'
'''
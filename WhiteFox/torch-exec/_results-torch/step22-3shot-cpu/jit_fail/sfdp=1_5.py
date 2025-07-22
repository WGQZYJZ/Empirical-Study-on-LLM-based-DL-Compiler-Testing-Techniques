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

    def forward(self, query, key, value):
        inv_scale_factor = torch.sqrt(1.0 / query.shape[-1])
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk * inv_scale_factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=qk.dim() - 1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = torch.matmul(key, dropout_qk)
        return output


func = Model().to('cpu')


query = torch.randn(1, 1, 64)

key = torch.randn(1, 1, 64)

value = torch.randn(1, 1, 64)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
sqrt(): argument 'input' (position 1) must be Tensor, not float

jit:
sqrt(): argument 'input' (position 1) must be Tensor, not float
'''
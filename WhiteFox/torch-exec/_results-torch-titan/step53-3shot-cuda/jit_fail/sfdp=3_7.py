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

    def __init__(self, query, key, value, scale_factor, dropout_p):
        super().__init__()
        self.query = query
        self.key = key
        self.value = value
        self.scale_factor = scale_factor
        self.dropout_p = dropout_p

    def forward(self, query, key, value, scale_factor, dropout_p):
        qk = matmul(query, key)
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output




query = torch.randn(1, 1, 128)


key = torch.randn(1, 1, 256)


value = torch.randn(1, 1, 256)


scale_factor = torch.randn(1, 128, 256)


dropout_p = torch.tensor([0.5])

func = Model(query, key, value, scale_factor, dropout_p).to('cuda')



query = torch.randn(1, 1, 128)



key = torch.randn(1, 1, 256)



value = torch.randn(1, 1, 256)



scale_factor = torch.randn(1, 128, 256)



dropout_p = torch.tensor([0.5])



x1 = torch.ones(1, 1, 128, requires_grad=True)



x2 = torch.ones(1, 1, 256, requires_grad=True)



x3 = torch.ones(1, 1, 256, requires_grad=True)



x4 = torch.ones(1, 128, 256, requires_grad=True)



x5 = torch.ones(1, requires_grad=True)


test_inputs = [query, key, value, scale_factor, dropout_p, x1, x2, x3, x4, x5]

# JIT_FAIL
'''
direct:
forward() takes 6 positional arguments but 11 were given

jit:
forward() takes 6 positional arguments but 11 were given
'''
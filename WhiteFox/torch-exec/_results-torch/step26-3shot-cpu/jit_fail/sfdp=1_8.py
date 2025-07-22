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

    def __init__(self, dropout_p=0.125, inv_scale_factor=1.5):
        super().__init__()

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


query = torch.randn(1, 32, 64)

key = torch.randn(1, 512, 64)

value = torch.randn(1, 512, 512)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'inv_scale_factor'

jit:
'Model' object has no attribute 'inv_scale_factor'
'''
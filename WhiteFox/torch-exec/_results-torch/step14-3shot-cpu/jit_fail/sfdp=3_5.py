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

class Model(nn.Module):

    def __init__(self):
        super().__init__()

    def attention(self, query, key, value, dropout=0.3):
        q = query
        k = key
        v = value
        scale_factor = float(q.size(-1)) ** (-0.5)
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        dropout_qk = F.dropout(softmax_qk, p=dropout)
        output = torch.matmul(dropout_qk, v)
        return output


func = Model().to('cpu')


query = torch.randn(16, 8, 64)

key = torch.rand(16, 8, 128)

test_inputs = [query, key]

# JIT_FAIL
'''
direct:
Module [Model] is missing the required "forward" function

jit:
Module [Model] is missing the required "forward" function
'''
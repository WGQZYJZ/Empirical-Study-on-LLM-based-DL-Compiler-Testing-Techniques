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

    def forward(self, q, k):
        scaled_qk = torch.matmul(q, k.transpose(-2, -1)) * math.sqrt(float(q.size(-1)))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        return dropout_qk.transpose(-2, -1).matmul(v)


func = Model().to('cpu')


q = torch.randn(2, 8, 32, 32)

k = torch.randn(2, 7, 32, 32)

v = torch.randn(2, 7, 32, 32)

test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''
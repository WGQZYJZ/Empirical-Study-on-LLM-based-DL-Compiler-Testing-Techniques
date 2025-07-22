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

    def forward(query, key, value, scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



query = torch.randn(1, 3, 10)



key = torch.randn(1, 4, 10)



value = torch.randn(1, 4, 10)




scale_factor = torch.arange(0, 3, 1, dtype=torch.float32)


test_inputs = [query, key, value, scale_factor]

# JIT_FAIL
'''
direct:
matmul(): argument 'input' (position 1) must be Tensor, not Model

jit:
matmul(): argument 'input' (position 1) must be Tensor, not Model
'''
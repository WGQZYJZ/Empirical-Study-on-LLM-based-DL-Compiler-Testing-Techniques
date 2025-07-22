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

    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


x1 = torch.randn(8, 1024, 32)

x2 = torch.randn(8, 32, 32)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'inv_scale_factor'

jit:
'Model' object has no attribute 'inv_scale_factor'
'''
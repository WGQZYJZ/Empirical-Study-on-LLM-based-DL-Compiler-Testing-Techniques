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
        self.dropout_1 = torch.nn.Dropout(dropout_p)

    def forward(self, x1, x2):
        x11 = self.dropout_1(x1)
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        t2 = dropout_qk.matmul(x2)
        return t2


func = Model().to('cpu')

x1 = 1
x2 = 1

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
dropout(): argument 'input' (position 1) must be Tensor, not int

jit:
dropout(): argument 'input' (position 1) must be Tensor, not int
'''
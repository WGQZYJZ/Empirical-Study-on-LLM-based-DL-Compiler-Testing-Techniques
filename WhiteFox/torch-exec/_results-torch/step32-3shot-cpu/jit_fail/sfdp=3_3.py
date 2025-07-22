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
        self.query = torch.nn.Conv2d(3, 4, 1, stride=1, padding=1)
        self.key = torch.nn.Conv2d(3, 1, 1, stride=1, padding=1)

    def forward(self, x1):
        q = self.query(x1)
        k = self.key(x1).squeeze(1)
        scale_factor = q.size(-1) ** (-0.5)
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        dropout_p = 0.8
        output = torch.nn.functional.dropout(scaled_qk.softmax(dim=-1), p=dropout_p).matmul(self.value(x1))
        return output


func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'value'

jit:
'Model' object has no attribute 'value'
'''
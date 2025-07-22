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
        self.query = [1.0, 1.0, 1.0]
        self.key = [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
        self.value = [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]

    def forward(self, qk, dropout_p):
        inv_scale_factor = (1.0 / math.sqrt(3))
        qk = torch.matmul(qk, self.key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(self.value)
        return output



func = Model().to('cuda')



qk = torch.randn(2, 3)

dropout_p = 1

test_inputs = [qk, dropout_p]

# JIT_FAIL
'''
direct:
'list' object has no attribute 'transpose'

jit:
'list' object has no attribute 'transpose'
'''
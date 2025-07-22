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
        self.inv_sf = float(64)

    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_qk = qk
        scaled_qk = scaled_qk / self.inv_sf
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(x2)
        return output


func = Model().to('cpu')


x1 = torch.randn(1, 3, 1)

x2 = torch.randn(1, 8, 1)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'dropout_p'

jit:
'Model' object has no attribute 'dropout_p'
'''
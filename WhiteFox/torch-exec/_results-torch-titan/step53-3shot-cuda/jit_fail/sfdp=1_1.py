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

    def __init__(self, dropout_p=0.25, scale_factor=None):
        super().__init__()
        self.dropout_p = dropout_p
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.dropout = torch.nn.Dropout(dropout_p)
        self.scale_factor = scale_factor

    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        v = v1
        if (self.scale_factor is not None):
            scales = (torch.ones_like(v1).type_as(v1) / self.scale_factor)
            v = (scales * v)
        v2 = self.softmax(v)
        v3 = self.dropout(v2)
        v4 = torch.matmul(v3, x3)
        return v4



func = Model(scale_factor=1.0).to('cuda')



x1 = torch.randn(1, 6, 8)



x2 = torch.randn(1, 10, 8)



x3 = torch.randn(1, 10, 6)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
forward() takes 3 positional arguments but 4 were given

jit:
forward() takes 3 positional arguments but 4 were given
'''
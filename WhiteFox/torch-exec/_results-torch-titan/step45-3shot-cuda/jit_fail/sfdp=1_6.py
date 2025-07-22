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

    def __init__(self, query, key, value, dropout_p, inv_scale_factor):
        super().__init__()
        self.dropout_p = dropout_p
        self.inv_scale_factor = inv_scale_factor
        self.softmax_f = torch.nn.Softmax(dim=(- 1))
        self.dropout_f = torch.nn.Dropout(p=dropout_p)

    def forward(self, x1):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scl = qk.div(self.inv_scale_factor)
        soft_s = self.softmax_f(scl)
        drop_soft = self.dropout_f(soft_s)
        output = torch.matmul(drop_soft, value)
        return output




query = torch.randn(1, 5, 10, 64)


key = torch.randn(1, 3, 10, 7)


value = torch.randn(1, 3, 10, 64)


dropout_p = 0.1


inv_scale_factor = (query.size(3) * (key.size((- 1)) ** (- 0.5)))

func = Model(query, key, value, dropout_p, inv_scale_factor).to('cuda')



query = torch.randn(1, 5, 10, 64)



key = torch.randn(1, 3, 10, 7)



x1 = torch.randn(1, 10, 64)


test_inputs = [query, key, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 4 were given

jit:
forward() takes 2 positional arguments but 4 were given
'''
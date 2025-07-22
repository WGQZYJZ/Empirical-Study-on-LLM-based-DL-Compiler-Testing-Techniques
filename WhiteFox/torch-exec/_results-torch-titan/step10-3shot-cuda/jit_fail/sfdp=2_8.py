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
        self.query = torch.rand([8, 64, 1, 128])
        self.key = torch.rand([8, 128, 1, 128])
        self.value = torch.rand([8, 128, 1, 128])
        self.dropout_p = 0.5

    def forward(self):
        qk = torch.matmul(self.query, self.key.transpose((- 2), (- 1)))
        inv_scale_factor = math.sqrt((128 / 128))
        v1 = qk.div(inv_scale_factor)
        softmax_qk = v1.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk.div(self.dropout_p), p=self.dropout_p)
        v2 = dropout_qk.matmul(self.value)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
forward() takes 1 positional argument but 2 were given

jit:
forward() takes 1 positional argument but 2 were given
'''
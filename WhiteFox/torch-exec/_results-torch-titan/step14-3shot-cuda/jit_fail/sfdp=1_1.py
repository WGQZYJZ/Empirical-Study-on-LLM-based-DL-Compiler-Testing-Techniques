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

    def forward(q1, k2, v3, inv_scale_factor4, dropout_p5):
        qk = torch.matmul(q1, k2.transpose((- 2), (- 1)))
        scaled_qk = qk.div(inv_scale_factor4)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p5)
        output = dropout_qk.matmul(v3)
        return output



func = Model().to('cuda')



q1 = torch.randn(1, 512, 32, 32)



k2 = torch.randn(1, 512, 32, 32)



v3 = torch.randn(1, 512, 32, 32)



inv_scale_factor4 = torch.randn(1)



dropout_p5 = torch.randn(1)


test_inputs = [q1, k2, v3, inv_scale_factor4, dropout_p5]

# JIT_FAIL
'''
direct:
forward() takes 5 positional arguments but 6 were given

jit:
forward() takes 5 positional arguments but 6 were given
'''
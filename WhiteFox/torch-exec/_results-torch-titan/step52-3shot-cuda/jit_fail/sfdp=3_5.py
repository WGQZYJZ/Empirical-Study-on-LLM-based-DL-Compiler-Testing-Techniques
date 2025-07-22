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

    def forward(self, v1, v2, v3):
        qk = torch.matmul(v1, v2.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v3)
        return output



func = Model().to('cuda')




scale_factor = torch.nn.Parameter(torch.tensor(1.0))



v1 = torch.randn(1, 1, 12, 64)



v2 = torch.randn(1, 1, 64, 512)



v3 = torch.randn(1, 512, 5)


test_inputs = [scale_factor, v1, v2, v3]

# JIT_FAIL
'''
direct:
forward() takes 4 positional arguments but 5 were given

jit:
forward() takes 4 positional arguments but 5 were given
'''
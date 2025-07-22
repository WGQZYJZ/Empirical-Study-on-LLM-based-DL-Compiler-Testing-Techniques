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

    def forward(self, __input__):
        qk = torch.matmul(__input__.query, __input__.key.transpose((- 2), (- 1)))
        scaled_qk = qk.div((1 / __input__.scale_factor))
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=__input__.dropout_p)
        output = dropout_qk.matmul(__input__.value)
        return output



func = Model().to('cuda')



input_x = torch.randn(2, 4, 32)



input_y = torch.randn(2, 4, 32)


test_inputs = [input_x, input_y]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''
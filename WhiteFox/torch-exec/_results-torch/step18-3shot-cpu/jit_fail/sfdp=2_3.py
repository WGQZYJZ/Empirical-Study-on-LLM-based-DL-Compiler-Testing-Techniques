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

    def forward(self, query, key, value):
        output = torch.matmul(query, key.transpose(-2, -1))
        scaled_output = output.div(inv_scale_factor)
        softmax_output = scaled_output.softmax(dim=-1)
        if training:
            dropout_output = torch.nn.functional.dropout(softmax_output, p=dropout_p)
        else:
            dropout_output = softmax_output
        output = dropout_output.matmul(value)
        return output


func = Model().to('cpu')


query = torch.randn(1, 12, 512)

key = torch.randn(1, 12, 512)

value = torch.randn(1, 12, 512)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
name 'inv_scale_factor' is not defined

jit:
NameError: name 'inv_scale_factor' is not defined

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
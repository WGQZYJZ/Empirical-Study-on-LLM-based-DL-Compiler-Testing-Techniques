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

    def forward(self, inputs):
        q = torch.randn(len(inputs), 8, 8)
        k = torch.randn(len(inputs), 8, 8)
        v = torch.randn(len(inputs), 8, 8)
        scale_factor = 4
        dropout_p = 0.7
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = qk.div(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')

inputs = 1

test_inputs = [inputs]

# JIT_FAIL
'''
direct:
object of type 'int' has no len()

jit:
object of type 'int' has no len()

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
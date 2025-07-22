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

    def forward(self, q, k, v):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        sf = (1.0 / math.sqrt(dim[1]))
        scaled_qk = (qk * sf)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')


dim = [4, 5]



q = torch.randn(1, dim[0])

k = 1
v = 1

test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'transpose'

jit:
'int' object has no attribute 'transpose'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
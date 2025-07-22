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
        self.embedding = np.random.randint(0, 100, (10, 32))
        self.dropout = torch.nn.Dropout(0.5)

    def forward(self, q, k, v):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        inv_scale_factor = (1 / np.sqrt(32))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = torch.matmul(dropout_qk, v)
        return output



func = Model().to('cuda')

q = 1
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
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
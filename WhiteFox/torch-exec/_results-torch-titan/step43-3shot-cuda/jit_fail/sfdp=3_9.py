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

    def __init__(self, dim, dropout_p=0.6):
        super().__init__()
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, x):
        (n, c, h, w) = x.shape
        q = torch.randn(n, c, 1, 1)
        k = torch.randn(n, c, h, w)
        scaled_qk = torch.matmul(q, k.transpose((- 2), (- 1))).mul((1.0 / np.sqrt(c)))
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        o = torch.matmul(dropout_qk, x)
        return o



dim = 1

func = Model(dim).to('cuda')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'shape'

jit:
'int' object has no attribute 'shape'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
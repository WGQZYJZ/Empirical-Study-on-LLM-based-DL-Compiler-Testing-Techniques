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
        self.dropout = torch.nn.Dropout(p=0.2)

    def forward(self, x1, x2):
        v1 = torch.matmul(query, key.transpose((- 2), (- 1)))
        v2 = v1.div(inv_scale_factor)
        v3 = v2.softmax(dim=(- 1))
        v4 = self.dropout(v3)
        return v4.matmul(value)



func = Model().to('cuda')



x1 = torch.randn(60, 30, 100)



x2 = torch.randn(60, 30, 100)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
name 'query' is not defined

jit:
name 'query' is not defined

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
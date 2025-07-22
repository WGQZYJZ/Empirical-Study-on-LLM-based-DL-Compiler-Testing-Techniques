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
        self.dropout_p = torch.nn.Parameter(torch.tensor(0.75))
        self.dropout = torch.nn.Dropout(self.dropout_p)

    def forward(self, x, y):
        v1 = torch.matmul(x, y.transpose((- 2), (- 1)))
        v2 = v1.div(self.inv_scale_factor)
        v3 = torch.nn.functional.softmax(v2, dim=(- 1))
        v4 = self.dropout(v3)
        v5 = torch.matmul(v4, y)
        return v5



func = Model().to('cuda')



x = torch.randn(1, 4, 1)



y = torch.randn(4, 2, 1)


test_inputs = [x, y]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'inv_scale_factor'

jit:
inv_scale_factor

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
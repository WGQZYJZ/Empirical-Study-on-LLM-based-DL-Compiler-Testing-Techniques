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
        self.dot_product = torch.nn.Softmax(dim=(- 1))

    def forward(self, query, key):
        v1 = torch.matmul(query, key.transpose((- 2), (- 1)))
        v2 = v1.div(inv_scale_factor)
        v3 = self.dot_product(v2)
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        v5 = torch.matmul(v4, value)
        return v5



func = Model().to('cuda')



query = torch.randn(1, 100, 10)



key = torch.randn(1, 200, 10)


test_inputs = [query, key]

# JIT_FAIL
'''
direct:
name 'inv_scale_factor' is not defined

jit:
name 'inv_scale_factor' is not defined

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
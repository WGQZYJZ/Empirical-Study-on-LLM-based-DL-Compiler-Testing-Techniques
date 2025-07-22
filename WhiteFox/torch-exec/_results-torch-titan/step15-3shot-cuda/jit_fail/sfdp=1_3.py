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
        self.matmul1 = torch.matmul

    def forward(self, x1, x2):
        v1 = self.matmul1(x1, x2)
        v2 = v1.__div__(inv_scale_factor)
        v3 = torch.nn.functional.softmax(v2, dim=(- 1))
        dropout_v3 = torch.nn.functional.dropout(v3, p=dropout_p)
        v4 = dropout_v3.matmul(value)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 16, 20)



x2 = torch.randn(1, 20, 40)


test_inputs = [x1, x2]

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
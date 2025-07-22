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

    def forward(self, q1, k1, v1):
        x1 = torch.matmul(q1, k1.transpose((- 2), (- 1)))
        x1 = (x1 * self.scale_factor)
        x2 = x1.softmax(dim=(- 1))
        x3 = torch.nn.functional.dropout(x2, p=self.dropout_p)
        x4 = x3.matmul(v1)
        return x4




func = Model().to('cuda')



q1 = torch.randn(1, 64, 1024)



k1 = torch.randn(1, 64, 1024)



v1 = torch.randn(1, 64, 1024)


test_inputs = [q1, k1, v1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'scale_factor'

jit:
scale_factor

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
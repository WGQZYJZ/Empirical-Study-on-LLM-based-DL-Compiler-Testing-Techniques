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

    def forward(self, data):
        data1 = data.reshape(2, 2)
        data2 = data.reshape(1, 2)
        result = (data1 + data2).reshape(2, -1)
        return result



func = Model().to('cpu')


data = torch.randn(200, 2)

test_inputs = [data]

# JIT_FAIL
'''
direct:
shape '[2, 2]' is invalid for input of size 400

jit:
Failed running call_method reshape(*(FakeTensor(..., size=(200, 2)), 2, 2), **{}):
shape '[2, 2]' is invalid for input of size 400

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
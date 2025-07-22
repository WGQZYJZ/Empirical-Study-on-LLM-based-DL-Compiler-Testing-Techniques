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

    def forward(self, input1):
        input2 = input1.view(20).unsqueeze_(0).unsqueeze_(0)
        input3 = torch.ones([2, 5])
        output = input2 + input3
        return output



func = Model().to('cpu')


input1 = torch.randn(5, 10)

test_inputs = [input1]

# JIT_FAIL
'''
direct:
shape '[20]' is invalid for input of size 50

jit:
Failed running call_method view(*(FakeTensor(..., size=(s0, s1)), 20), **{}):
shape '[20]' is invalid for input of size s0*s1

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
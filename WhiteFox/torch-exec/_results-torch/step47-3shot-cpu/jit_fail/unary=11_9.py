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

    def forward(self, x1):
        v1 = nn.functional.pixel_shuffle(x1, 4)
        v2 = torch.reshape(v1, (1, 32, 32, 32))
        v3 = torch.transpose(v2, 2, 3)
        v4 = torch.transpose(v3, 1, 2)
        v5 = nn.functional.conv_transpose3d(v4, weight=None, bias=None, stride=(1, 1, 4), padding=(0, 0, 1), output_padding=(0, 0, 0), groups=1, dilation=1)
        v6 = v5 + 3
        v7 = v6 + v1
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 16, 8, 8)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
shape '[1, 32, 32, 32]' is invalid for input of size 1024

jit:
Failed running call_function <built-in method reshape of type object at 0x7f1778196ec0>(*(FakeTensor(..., size=(1, 1, 32, 32)), (1, 32, 32, 32)), **{}):
shape '[1, 32, 32, 32]' is invalid for input of size 1024

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
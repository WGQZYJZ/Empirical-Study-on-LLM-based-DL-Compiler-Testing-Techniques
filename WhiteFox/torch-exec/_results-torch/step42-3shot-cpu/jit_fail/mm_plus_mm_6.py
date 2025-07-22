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

    def forward(self, input1, input2, input3, input4):
        var1 = torch.reshape(input1, (1, 20))
        var1 = var1.view((-1,))
        var2 = input2.view((-1,))
        t1 = torch.mm(var1, var2)
        var3 = input3.view(10, 10)
        var4 = input4.view(10, 10)
        t2 = torch.mm(var3, var4)
        return t1 + t2



func = Model().to('cpu')


input1 = torch.rand([1, 48032])

input2 = torch.rand([1, 128])

input3 = torch.rand([10, 256])

input4 = torch.rand([10, 256])

test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
shape '[1, 20]' is invalid for input of size 48032

jit:
Failed running call_function <built-in method reshape of type object at 0x73791e796ec0>(*(FakeTensor(..., size=(1, s0)), (1, 20)), **{}):
shape '[1, 20]' is invalid for input of size s0

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
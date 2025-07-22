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

    def forward(self, inputs):
        t0 = torch.add(inputs, inputs)
        s = inputs.size(0)
        d = inputs.size(1)
        t1 = torch.add(t0, inputs)
        shape = ((s / d), d)
        t2 = torch.reshape(t1, shape)
        out = torch.tanh(t2)
        return out




func = Model().to('cuda')



x = torch.randn(20, 30)


test_inputs = [x]

# JIT_FAIL
'''
direct:
reshape(): argument 'shape' (position 2) must be tuple of ints, but found element of type float at pos 0

jit:
Failed running call_function <built-in method reshape of type object at 0x75e8be4699e0>(*(FakeTensor(..., device='cuda:0', size=(20, 30)), (0.6666666666666666, 30)), **{}):
reshape(): argument 'shape' (position 2) must be tuple of ints, but found element of type float at pos 0

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
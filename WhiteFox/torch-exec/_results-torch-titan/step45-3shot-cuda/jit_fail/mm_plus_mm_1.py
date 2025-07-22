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

    def forward(self, x, w):
        shape = w.shape
        x = x.reshape((*shape, 1))
        y = (x.squeeze() * w)
        return y




func = Model().to('cuda')



x = torch.randn(10, 3, 4)



w = torch.randn(3, 4, 5)


test_inputs = [x, w]

# JIT_FAIL
'''
direct:
shape '[3, 4, 5, 1]' is invalid for input of size 120

jit:
Failed running call_method reshape(*(FakeTensor(..., device='cuda:0', size=(10, 3, 4)), (3, 4, 5, 1)), **{}):
shape '[3, 4, 5, 1]' is invalid for input of size 120

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
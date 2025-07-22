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
        self.x = torch.randn(3, 4)

    def forward(self, x):
        y = torch.cat((x, x), dim=1)
        y = y.view(y.shape[0], (- 1))
        x = self.x
        if (x.shape[0] != y.shape[0]):
            x = x.repeat(y.shape[0], 1, 1)
        y = torch.tanh((y * x))
        return y.sum()




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (24) must match the size of tensor b (4) at non-singleton dimension 2

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(2, 24)), FakeTensor(..., device='cuda:0', size=(2, 3, 4))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([2, 3, 4]); but expected shape should be broadcastable to [1, 2, 24]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
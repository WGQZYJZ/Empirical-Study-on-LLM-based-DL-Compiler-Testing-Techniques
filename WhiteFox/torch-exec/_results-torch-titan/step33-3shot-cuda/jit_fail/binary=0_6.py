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
        self.conva = torch.nn.Conv2d(3, 8, (1, 3), (1, 1), (0, 1))
        self.convb = torch.nn.Conv2d(8, 4, (7, 1), (1, 1), (0, 1))

    def forward(self, x1, other=None):
        var1 = self.conva(x1)
        var2 = self.convb(var1)
        if (other == None):
            other = torch.randn([var2.shape[0]])
        var3 = (var2 + other)
        return var3




func = Model().to('cuda')



x1 = torch.randn(3, 3, 255, 255)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (257) must match the size of tensor b (3) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(3, 4, 249, 257)), FakeTensor(..., size=(3,))), **{}):
Attempting to broadcast a dimension of length 3 at -1! Mismatching argument at index 1 had torch.Size([3]); but expected shape should be broadcastable to [3, 4, 249, 257]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_transpose1 = nn.ConvTranspose2d(49, 9, 3, stride=1, padding=1)
        self.conv_transpose2 = nn.ConvTranspose2d(9, 6, 3, stride=2, padding=1, output_padding=(1, 1))

    def forward(self, x):
        x = self.conv_transpose1(x)
        x = (x * 0.5)
        x = ((x * x) * x)
        x = (x * 0.044715)
        x = (x + self.conv_transpose2(x))
        x = (x * 0.7978845608028654)
        x = torch.tanh(x)
        x = (x + 1)
        x = (x * x)
        return x




func = Model().to('cuda')



x1 = torch.randn((1, 49, 2, 5))


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (5) must match the size of tensor b (10) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 9, 2, 5)), FakeTensor(..., device='cuda:0', size=(1, 6, 4, 10))), **{}):
Attempting to broadcast a dimension of length 10 at -1! Mismatching argument at index 1 had torch.Size([1, 6, 4, 10]); but expected shape should be broadcastable to [1, 9, 2, 5]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
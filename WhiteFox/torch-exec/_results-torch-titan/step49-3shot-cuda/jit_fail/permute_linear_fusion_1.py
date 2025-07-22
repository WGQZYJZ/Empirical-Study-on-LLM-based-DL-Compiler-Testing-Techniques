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
        self.conv2d_0 = torch.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), dilation=(1, 1))

    def forward(self, x1):
        v1 = self.conv2d_0(x1)
        return (x1 + v1[:, :, 1, 1])




func = Model().to('cuda')



x1 = torch.randn(1, 3, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (3) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(1, 3, 2, 2)), FakeTensor(..., device='cuda:0', size=(1, 3))), **{}):
Attempting to broadcast a dimension of length 3 at -1! Mismatching argument at index 1 had torch.Size([1, 3]); but expected shape should be broadcastable to [1, 3, 2, 2]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
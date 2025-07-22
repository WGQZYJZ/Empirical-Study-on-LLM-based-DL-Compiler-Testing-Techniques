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
        self.conv1x1_weight_bias = torch.nn.Parameter(torch.randn(1, 882, 787, 82))

    def forward(self, x7):
        v1 = self.conv1x1_weight_bias
        v2 = (x7 * v1)
        return v2




func = Model().to('cuda')



x7 = torch.randn(1, 82, 628, 118)


test_inputs = [x7]

# JIT_FAIL
'''
direct:
The size of tensor a (118) must match the size of tensor b (82) at non-singleton dimension 3

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(1, 82, 628, 118)), Parameter(FakeTensor(..., device='cuda:0', size=(1, 882, 787, 82), requires_grad=True))), **{}):
Attempting to broadcast a dimension of length 82 at -1! Mismatching argument at index 1 had torch.Size([1, 882, 787, 82]); but expected shape should be broadcastable to [1, 82, 628, 118]

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
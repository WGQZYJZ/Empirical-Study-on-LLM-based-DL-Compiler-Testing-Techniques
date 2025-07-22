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

    def forward(self, x1, x2, x3):
        out1 = torch.bmm(torch.matmul(x3.permute(0, 2, 1), x1), x2.permute(0, 2, 1))
        out2 = torch.bmm(out1, out1)
        out3 = torch.matmul(torch.bmm(out2, out1), x2.permute(0, 2, 1))
        return out2




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)



x2 = torch.randn(2, 2)



x3 = torch.randn(2, 2)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 2 is not equal to len(dims) = 3

jit:
Failed running call_method permute(*(FakeTensor(..., device='cuda:0', size=(2, 2)), 0, 2, 1), **{}):
Dimension out of range (expected to be in range of [-2, 1], but got 2)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
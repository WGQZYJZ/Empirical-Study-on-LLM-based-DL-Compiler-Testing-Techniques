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
        self.linear = torch.nn.Linear(2, 2).cuda()
        self.linear1 = torch.nn.Linear(2, 2).cuda()

    def forward(self, x1):
        v4 = x1.cuda()
        v5 = torch.nn.functional.relu(v4)
        v1 = torch.nn.functional.linear(v4, self.linear.weight, self.linear.bias)
        v2 = torch.nn.functional.relu6(v1)
        v3 = v2.permute(0, 1, 3, 2)
        v6 = torch.min(v3, dim=2, keepdim=False, out=None).values
        v7 = torch.nn.functional.linear(v5.permute(0, 2, 1), self.linear1.weight, self.linear1.bias)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2, device='cuda')


test_inputs = [x1]

# JIT_FAIL
'''
direct:
permute(sparse_coo): number of dimensions in the tensor input does not match the length of the desired ordering of dimensions i.e. input.dim() = 3 is not equal to len(dims) = 4

jit:
Failed running call_method permute(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), 0, 1, 3, 2), **{}):
Dimension out of range (expected to be in range of [-3, 2], but got 3)

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
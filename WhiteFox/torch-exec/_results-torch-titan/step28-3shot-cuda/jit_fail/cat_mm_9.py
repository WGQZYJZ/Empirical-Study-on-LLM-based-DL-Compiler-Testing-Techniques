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

    def forward(self, a, b, c):
        v1 = torch.cat([a], 1)
        v2 = (b + a)
        v3 = torch.cat([c, v2, b, b, a, a], 1)
        return torch.cat([v1, v3, v2, v3, v2, v3, v1], 0)




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, a, b, c):
        v1 = torch.cat([a], 1)
        v2 = (b + a)
        v3 = torch.cat([a, b, c, v2, a, b, c, b, c, v2, b, c, a, v2, c, a, b, c, b, c, a], 1)
        return torch.cat([v1, v3, v2, v3, v2, v3, v1], 0)




func = Model().to('cuda')





a = torch.mm(torch.randn(2, 3), torch.randn(3, 4))





b = torch.mm(torch.randn(2, 2), torch.randn(2, 4))





c = torch.mm(torch.randn(2, 5), torch.randn(5, 4))


test_inputs = [a, b, c]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 0. Expected size 4 but got size 84 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7f12d7a699e0>(*([FakeTensor(..., device='cuda:0', size=(2, 4)), FakeTensor(..., device='cuda:0', size=(2, 84)), FakeTensor(..., device='cuda:0', size=(2, 4)), FakeTensor(..., device='cuda:0', size=(2, 84)), FakeTensor(..., device='cuda:0', size=(2, 4)), FakeTensor(..., device='cuda:0', size=(2, 84)), FakeTensor(..., device='cuda:0', size=(2, 4))], 0), **{}):
Sizes of tensors must match except in dimension 0. Expected 4 but got 84 for tensor number 1 in the list

from user code:
   File "<string>", line 38, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
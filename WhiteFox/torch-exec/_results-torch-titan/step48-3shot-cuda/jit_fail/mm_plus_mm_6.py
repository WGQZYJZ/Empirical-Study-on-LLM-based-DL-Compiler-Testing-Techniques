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

    def forward(self, input):
        (A, B, C, D, E, F, G) = input.split([7, 8, 8, 7, 7, 9, 10], dim=2)
        F = F[(A > 1258)]
        V = (torch.mm(A, A) + torch.mm(B, D))
        t = (torch.mm(C, B) + torch.mm(D, E))
        x = (t == torch.mm(E, E))
        return torch.mm(V, x)




func = Model().to('cuda')



input = torch.randn(5, 7, 15)


test_inputs = [input]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 15 (input tensor's size at dimension 2), but got split_sizes=[7, 8, 8, 7, 7, 9, 10]

jit:
Failed running call_method split(*(FakeTensor(..., device='cuda:0', size=(5, 7, 15)), [7, 8, 8, 7, 7, 9, 10]), **{'dim': 2}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
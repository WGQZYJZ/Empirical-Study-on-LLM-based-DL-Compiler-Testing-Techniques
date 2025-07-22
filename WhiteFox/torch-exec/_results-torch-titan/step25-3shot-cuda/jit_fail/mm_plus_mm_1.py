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

    def forward(self, input1, input2, input3):
        t1 = torch.einsum('ij,jk->ik', (input1, input2))
        t2 = torch.einsum('ij,jk->ik', (t1, input3))
        return torch.mm(t2, input1)




func = Model().to('cuda')



input1 = torch.randn(3, 6)



input2 = torch.randn(6, 3)



input3 = torch.randn(6, 3)


test_inputs = [input1, input2, input3]

# JIT_FAIL
'''
direct:
einsum(): subscript j has size 6 for operand 1 which does not broadcast with previously seen size 3

jit:
Failed running call_function <function einsum at 0x78c28a6ee160>(*('ij,jk->ik', (FakeTensor(..., device='cuda:0', size=(3, 3)), FakeTensor(..., device='cuda:0', size=(6, 3)))), **{}):
einsum(): subscript j has size 6 for operand 1 which does not broadcast with previously seen size 3

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
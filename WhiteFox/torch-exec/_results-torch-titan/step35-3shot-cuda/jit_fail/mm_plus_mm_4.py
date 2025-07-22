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

    def forward(self, input1, input2, input3, input4):
        t1 = torch.einsum('ij, j', [input1, input2])
        t2 = torch.mm(input3, input4)
        t3 = torch.einsum('ij, i, j', [input2, input1, input4])
        t4 = torch.einsum('i, j', [input1, input3])
        return (((t1 + t2) + t3) + t4)




func = Model().to('cuda')



input1 = torch.randn(5, 5)



input2 = torch.randn(5, 5)



input3 = torch.randn(5, 5)



input4 = torch.randn(5, 5)


test_inputs = [input1, input2, input3, input4]

# JIT_FAIL
'''
direct:
einsum(): the number of subscripts in the equation (1) does not match the number of dimensions (2) for operand 1 and no ellipsis was given

jit:
Failed running call_function <function einsum at 0x7a0ca8cef160>(*('ij, j', [FakeTensor(..., device='cuda:0', size=(5, 5)), FakeTensor(..., device='cuda:0', size=(5, 5))]), **{}):
einsum(): the number of subscripts in the equation (1) does not match the number of dimensions (2) for operand 1 and no ellipsis was given

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
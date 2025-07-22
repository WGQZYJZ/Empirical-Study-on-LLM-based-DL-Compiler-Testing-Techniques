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

    def forward(self, x1, x2, x3, x4, x5, size):
        c1 = torch.cat([x1, x2, x3, x4, x5])
        i1 = torch.tensor([70273749298880, 38956906369248, 16316086777680, 83297495521792, 191839786542528, 376992761456332, 221880851359940, 0, (- 16781096230092), (- 27847728347500), (- 98222995813580), 0, 793685538262556])
        i2 = torch.tensor([65279, 44612, 19652, 83839, 17440, 34485, 151729, 0, (- 20462), (- 38108), (- 123384), 0, 561049])
        c2 = (i1 * c1)
        b1 = c2[:, (- 170141183460469231731687303715884105728)]
        l1 = c2[:, i2.tolist()]
        a1 = torch.cat([b1, l1], dim=1)
        return l1[:, :size]



func = Model().to('cuda')



x1 = torch.randn(1, 6, 64, 64)



x2 = torch.randn(1, 7, 64, 64)



x3 = torch.randn(1, 8, 64, 64)



x4 = torch.randn(1, 9, 64, 64)



x5 = torch.randn(7, 10, 64, 64)

size = 1

test_inputs = [x1, x2, x3, x4, x5, size]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 0. Expected size 6 but got size 7 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7ced5a0699e0>(*([FakeTensor(..., device='cuda:0', size=(1, 6, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 7, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 9, 64, 64)), FakeTensor(..., device='cuda:0', size=(7, 10, 64, 64))],), **{}):
Sizes of tensors must match except in dimension 0. Expected 6 but got 7 for tensor number 1 in the list

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
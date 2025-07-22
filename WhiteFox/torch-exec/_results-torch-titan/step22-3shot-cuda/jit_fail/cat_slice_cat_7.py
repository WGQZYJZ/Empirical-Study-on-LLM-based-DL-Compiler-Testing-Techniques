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

    def forward(self, *xs):
        xs_cat = torch.cat(xs, dim=1)
        l1 = list(range(np.iinfo(np.int64).max))
        sl1 = slice(0, 9223372036854775807)
        sl2 = slice(sl1.start, (sl1.stop - 2))
        xs_cat_sliced = xs_cat[:, sl2]
        l1.extend(list(range(((abs(sl1.stop) - sl1.start) - 2))))
        xs_cat_sliced = torch.cat([xs_cat, xs_cat_sliced], dim=1)
        return xs_cat_sliced



func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 3, 32, 32)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Sizes of tensors must match except in dimension 1. Expected size 64 but got size 32 for tensor number 1 in the list.

jit:
Failed running call_function <built-in method cat of type object at 0x7ed905e699e0>(*((FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)), FakeTensor(..., device='cuda:0', size=(1, 3, 32, 32))),), **{'dim': 1}):
Sizes of tensors must match except in dimension 1. Expected 64 but got 32 for tensor number 1 in the list

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
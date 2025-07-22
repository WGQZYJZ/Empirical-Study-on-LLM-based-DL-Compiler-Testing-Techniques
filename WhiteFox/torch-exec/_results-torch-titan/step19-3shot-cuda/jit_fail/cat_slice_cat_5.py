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

    def forward(self, _input_):
        t1 = torch.cat(_input_, dim=1)
        t2 = t1[:, 0:9223372036854775807]
        t3 = t2[:, 0:_input_.size()]
        t4 = torch.cat([t1, t3], dim=1)
        return t4



func = Model().to('cuda')

_input_ = 1

test_inputs = [_input_]

# JIT_FAIL
'''
direct:
cat() received an invalid combination of arguments - got (int, dim=int), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
 * (tuple of Tensors tensors, name dim, *, Tensor out)


jit:
Failed running call_function <built-in method cat of type object at 0x7cec5ca699e0>(*(1,), **{'dim': 1}):
cat() received an invalid combination of arguments - got (int, dim=int), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
 * (tuple of Tensors tensors, name dim, *, Tensor out)


from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
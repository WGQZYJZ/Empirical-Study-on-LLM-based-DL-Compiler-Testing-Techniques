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

    def forward(self, m1, m2):
        qk = torch.matmul(m1, m2.transpose((- 2), (- 1)))
        scale_factor = torch.tensor.type(torch.float32).pow((2.0 / (m1.shape[(- 1)] ** 0.5)))
        dropout_p = 0.2
        output = torch.nn.functional.dropout(qk.mul(scale_factor).softmax(dim=(- 1)), p=dropout_p).matmul(m2)
        return output




func = Model().to('cuda')




m1 = torch.nn.init.uniform_(torch.Tensor(3, 4))




m2 = torch.nn.init.uniform_(torch.Tensor(4, 3))


test_inputs = [m1, m2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x4 and 3x4)

jit:
Failed running call_function <built-in method matmul of type object at 0x71740a2699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 4)), FakeTensor(..., device='cuda:0', size=(3, 4))), **{}):
a and b must have same reduction dim, but got [3, 4] X [3, 4].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
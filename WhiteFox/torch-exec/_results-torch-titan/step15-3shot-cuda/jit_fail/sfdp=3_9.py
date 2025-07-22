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
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, input_tensor, x1, x2):
        v1 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        v2 = (v1 * scale_factor)
        v3 = v2.softmax(dim=(- 1))
        v4 = self.dropout(v3)
        v5 = v4.matmul(x3)
        return v5



func = Model().to('cuda')



x1 = torch.randn(5, 128)



x2 = torch.randn(5, 128)



x3 = torch.randn(5, 128)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu!

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(5, 5)), FakeTensor(..., size=(1,))), **{}):
Unhandled FakeTensor Device Propagation for aten.mul.Tensor, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, size, tensors1, tensors2, tensors3):
        t1 = torch.cat(tensors1, tensors2, tensors3, dim=1)
        t2 = t1[:, 0:9223372036854775807]
        t3 = t2[:, 0:size]
        t4 = torch.cat([t1, t3])
        return t4



func = Model().to('cuda')



tensor1 = torch.randn(1, 4, 5, 5)



tensor2 = torch.randn(1, 4, 5, 6)



tensor3 = torch.randn(1, 4, 5, 7)

size = 1

test_inputs = [tensor1, tensor2, tensor3, size]

# JIT_FAIL
'''
direct:
cat() received an invalid combination of arguments - got (Tensor, Tensor, int, dim=int), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
      didn't match because some of the keywords were incorrect: dim
 * (tuple of Tensors tensors, name dim, *, Tensor out)
      didn't match because some of the keywords were incorrect: dim


jit:
Failed running call_function <built-in method cat of type object at 0x7687c2c699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 4, 5, 6)), FakeTensor(..., device='cuda:0', size=(1, 4, 5, 7)), 1), **{'dim': 1}):
cat() received an invalid combination of arguments - got (FakeTensor, FakeTensor, int, dim=int), but expected one of:
 * (tuple of Tensors tensors, int dim, *, Tensor out)
      didn't match because some of the keywords were incorrect: dim
 * (tuple of Tensors tensors, name dim, *, Tensor out)
      didn't match because some of the keywords were incorrect: dim


from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
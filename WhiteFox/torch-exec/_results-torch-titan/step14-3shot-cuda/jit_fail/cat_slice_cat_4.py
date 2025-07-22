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

    def forward(self, x1, x2, x3, x4):
        v1 = torch.cat([x1, x2, x3], dim=1)
        v2 = v1[:, 0:x2.size(1)]
        v3 = v2[:, 0:x4.size(3)]
        v4 = [v1, v3]
        v5 = torch.cat([v4, x4], dim=1)
        return v5



func = Model().to('cuda')



x1 = torch.randn(1, 4, 32, 32)


x1 = torch.randn(1, 4, 32, 32)


x1 = torch.randn(1, 4, 32, 32)


x1 = torch.randn(1, 4, 32, 32)



x2 = torch.randn(1, (x1.size(1) - 1), x1.size(2), x1.size(3))


x2 = torch.randn(1, (x1.size(1) - 1), x1.size(2), x1.size(3))


x2 = torch.randn(1, (x1.size(1) - 1), x1.size(2), x1.size(3))


x2 = torch.randn(1, (x1.size(1) - 1), x1.size(2), x1.size(3))



x3 = torch.randn(1, (x2.size(1) - 1), x2.size(2), x2.size(3))


x3 = torch.randn(1, (x2.size(1) - 1), x2.size(2), x2.size(3))


x3 = torch.randn(1, (x2.size(1) - 1), x2.size(2), x2.size(3))


x3 = torch.randn(1, (x2.size(1) - 1), x2.size(2), x2.size(3))



x4 = torch.randn(1, (x3.size(1) + 2), x3.size(2), x3.size(3))


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
expected Tensor as element 0 in argument 0, but got list

jit:
Failed running call_function <built-in method cat of type object at 0x7a897bc699e0>(*([[FakeTensor(..., device='cuda:0', size=(1, 9, 32, 32)), FakeTensor(..., device='cuda:0', size=(1, 3, 32, 32))], FakeTensor(..., device='cuda:0', size=(1, 4, 32, 32))],), **{'dim': 1}):
expected Tensor as element 0 in argument 0, but got immutable_list

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
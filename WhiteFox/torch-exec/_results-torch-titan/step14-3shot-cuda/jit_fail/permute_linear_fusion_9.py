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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = torch.randn_like(x1[:, :1, :])
        v1 = v1.to(torch.int32)
        v2 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v2, self.linear.weight, self.linear.bias)
        x2 = torch.nn.functional.relu(v2)
        v3 = torch.matmul(x1, v1)
        return torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 2] but got: [1, 1].

jit:
Failed running call_function <built-in method matmul of type object at 0x7e6d484699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), FakeTensor(..., device='cuda:0', size=(1, 1, 2), dtype=torch.int32)), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 2] but got: [1, 1].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
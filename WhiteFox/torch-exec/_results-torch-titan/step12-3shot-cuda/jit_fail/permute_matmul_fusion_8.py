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

    def forward(self, x1, x2):
        return torch.matmul(x1.permute(0, 2, 1), x2)




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)



x2 = torch.randn(1, 1, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 2] but got: [1, 1].

jit:
Failed running call_function <built-in method matmul of type object at 0x79b9418699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), FakeTensor(..., device='cuda:0', size=(1, 1, 2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 2] but got: [1, 1].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
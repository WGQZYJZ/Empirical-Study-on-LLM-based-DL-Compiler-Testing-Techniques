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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Linear(256, 256)

    def forward(self, x):
        x = self.layers(x)
        x = torch.transpose(x, 0, 1)
        x = torch.matmul(x, x)
        return x




func = Model().to('cuda')



x = torch.randn(20, 1, 256)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 256] but got: [1, 20].

jit:
Failed running call_function <built-in method matmul of type object at 0x7e57cda699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 20, 256)), FakeTensor(..., device='cuda:0', size=(1, 20, 256))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 256] but got: [1, 20].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
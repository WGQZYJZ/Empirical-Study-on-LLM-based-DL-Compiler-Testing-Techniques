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

    def forward(self, x, w0, w1, w2):
        y = torch.cat((x, w0.view(w0.size(0), (- 1))), dim=1)
        y = (y + w1.view(w1.size(0), (- 1)))
        return (y.tanh() + w2.view(w2.size(0), (- 1)).tanh())




func = Model().to('cuda')



w0 = torch.randn(64, 4096, 7, 7)



w1 = torch.randn(64, 4096, 1, 1)



w2 = torch.randn(64)



x = torch.randn(64, 3, 224, 224)


test_inputs = [w0, w1, w2, x]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 4 and 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(64, 8192, 7, 7)), FakeTensor(..., device='cuda:0', size=(64, 1))), **{}):
Attempting to broadcast a dimension of length 64 at -2! Mismatching argument at index 1 had torch.Size([64, 1]); but expected shape should be broadcastable to [64, 8192, 7, 7]

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
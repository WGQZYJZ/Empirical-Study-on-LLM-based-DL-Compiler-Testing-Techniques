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
        self.features = torch.nn.Sequential(torch.nn.Linear(1, 3, bias=False))
        self.classifier = torch.nn.Sequential(torch.nn.Sigmoid(), torch.nn.Linear(3, 3, bias=False), torch.nn.Tanh(), torch.nn.Softmax(dim=0))
        self.add_feature = torch.nn.Sigmoid()

    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=0)
        concatenated_tensor = torch.cat(split_tensors, dim=0)
        return (concatenated_tensor, v1.split(1, dim=0))




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 1 (input tensor's size at dimension 0), but got split_sizes=[1, 1, 1]

jit:
Failed running call_function <function split at 0x7824975700d0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), [1, 1, 1]), **{'dim': 0}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
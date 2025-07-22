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
        self.features = torch.nn.ModuleList([torch.nn.Conv2d(3, 32, 3, 1, 1), torch.nn.ReLU(inplace=False)])
        self.classifier = torch.nn.ModuleList([torch.nn.Conv2d(32, 16, 3, 3, 1), torch.nn.Conv2d(16, 8, 3, 3, 1)])

    def forward(self, v1):
        split_tensors = torch.split(v1, [4, 4], dim=0)
        concatenated_tensor = torch.cat(split_tensors, dim=0)
        for x in self.features:
            y = x(concatenated_tensor)
        for x in self.classifier:
            y = x(y)
        return (concatenated_tensor, split_tensors)




func = Model().to('cuda')



x1 = torch.randn(1, 1, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 1 (input tensor's size at dimension 0), but got split_sizes=[4, 4]

jit:
Failed running call_function <function split at 0x790a68f6f0d0>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 64, 64)), [4, 4]), **{'dim': 0}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
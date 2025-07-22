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
        self.features = torch.nn.ModuleList([torch.nn.Linear(128, 10), torch.nn.ReLU(), torch.nn.Linear(10, 10)])
        self.fc1 = torch.nn.Linear(10, 16)

    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        output1 = torch.add(self.features[0](concatenated_tensor), self.features[1](concatenated_tensor))
        output2 = torch.add(self.features[2](output1), self.features[3](output1))
        return (concatenated_tensor, self.features(v1), (self.features(v1), output2), v1, split_tensors, concatenated_tensor, self.fc1(output2))




func = Model().to('cuda')



x1 = torch.randn(1, 10, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 10 (input tensor's size at dimension 1), but got split_sizes=[1, 1, 1]

jit:
Failed running call_function <function split at 0x716090aef0d0>(*(FakeTensor(..., device='cuda:0', size=(1, 10, 1)), [1, 1, 1]), **{'dim': 1}):
Split sizes don't add up to the tensor's size in the given dimension

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
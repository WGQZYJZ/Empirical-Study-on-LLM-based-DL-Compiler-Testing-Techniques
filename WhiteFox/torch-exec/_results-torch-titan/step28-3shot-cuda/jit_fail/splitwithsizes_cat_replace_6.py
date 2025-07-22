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
        self.features = torch.nn.ModuleList([torch.nn.Sequential(torch.nn.Conv2d(3, 16, 3, 1, 1), torch.nn.Conv2d(3, 16, 3, 1, 1), torch.nn.Conv2d(3, 16, 3, 1, 1)), torch.nn.Sequential(torch.nn.Conv2d(3, 16, 3, 1, 1), torch.nn.Conv2d(3, 16, 3, 1, 1), torch.nn.Conv2d(3, 16, 3, 1, 1))])
        self.add = torch.add

    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        for model in self:
            split_tensors = torch.split(v1, [1, 1, 1], dim=1)
            concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=1))




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object is not iterable

jit:
Model

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
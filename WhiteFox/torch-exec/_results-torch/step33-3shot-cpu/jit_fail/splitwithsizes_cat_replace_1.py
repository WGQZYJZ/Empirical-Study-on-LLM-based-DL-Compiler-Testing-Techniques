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
        self.layers = torch.nn.ModuleList([torch.nn.Conv2d(3, 32, 3, 1, 1), torch.nn.MaxPool2d(kernel_size=2), torch.nn.BatchNorm2d(32), torch.nn.Linear(32, 64), torch.nn.MaxPool2d(kernel_size=2), torch.nn.BatchNorm1d(64), torch.nn.Softmax(dim=-1)])

    def forward(self, input_tensor):
        split_tensors = torch.split(self.layers[0](input_tensor), [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat([self.layers[1](split_tensors[0]), self.layers[2](split_tensors[1]), self.layers[3](split_tensors[2])], dim=1)
        return (concatenated_tensor, torch.cat([split_tensors[0], split_tensors[1], split_tensors[2]], dim=1))



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
split_with_sizes expects split_sizes to sum exactly to 32 (input tensor's size at dimension 1), but got split_sizes=[1, 1, 1]

jit:
Failed running call_function <function split at 0x748dfeffcf70>(*(FakeTensor(..., size=(1, 32, 64, 64)), [1, 1, 1]), **{'dim': 1}):
Split sizes add up to 3 but got the tensor's size of 32

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
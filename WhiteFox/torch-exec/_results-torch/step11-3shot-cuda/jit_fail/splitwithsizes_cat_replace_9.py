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
        self.features = torch.nn.Sequential(torch.nn.Conv2d(3, 16, 3, 1, 1), torch.nn.Conv2d(16, 32, 7, 2, 2), torch.nn.Conv2d(32, 16, 5, 1, 1), torch.nn.Conv2d(16, 8, 13, 2, 2), torch.nn.ConvTranspose2d(8, 1, 7, 1, 0), torch.nn.ConvTranspose2d(8, 16, 4, 1, 0))
        self.split = torch.nn.Sequential(torch.nn.MaxPool2d(5, 3, 0, 1), torch.nn.MaxPool2d(4, 2, 2, 2), torch.nn.MaxPool2d(3, 1, 2, 1))

    def forward(self, x1):
        v1 = self.features(x1)
        split_tensors = torch.split(v1, [9, 5, 9], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [9, 5, 9], dim=1))



func = Model().to('cuda')


x1 = torch.randn(1, 3, 56, 56)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [8, 16, 4, 4], expected input[1, 1, 15, 15] to have 8 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7e0817d96ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 15, 15)), Parameter(FakeTensor(..., device='cuda:0', size=(8, 16, 4, 4), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(16,), requires_grad=True)), (1, 1), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [8, 16, 4, 4], expected input[1, 1, 15, 15] to have 8 channels, but got 1 channels instead

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
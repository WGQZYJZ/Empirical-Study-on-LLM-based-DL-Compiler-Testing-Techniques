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
        for i in range(10):
            self.features = torch.nn.Sequential(torch.nn.Sequential(torch.nn.MaxPool2d(3, 2, 1), torch.nn.GELU(), torch.nn.BatchNorm2d(32, eps=0.0010000000474974513, momentum=0.0, affine=True, track_running_stats=True)), torch.nn.GELU(), torch.nn.BatchNorm2d(32, eps=0.0010000000474974513, momentum=0.0, affine=True, track_running_stats=True))

    def forward(self, x4):
        split_tensors = torch.split(x4, [1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, concatTensor1, dim=1)
        return (concatenated_tensor, torch.split(x4, [1, 1], dim=1))




func = Model().to('cuda')



concatTensor1 = torch.randn(1, 2, 2, 2, 2)



x4 = torch.randn(1, 2, 2, 2, 2)


test_inputs = [concatTensor1, x4]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''
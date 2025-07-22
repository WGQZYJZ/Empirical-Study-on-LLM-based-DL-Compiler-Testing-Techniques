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
    __linear = torch.nn.Linear(8, 8)

    def __init__(self):
        super().__init__()
        for (name, v) in self.__linear.named_parameters():
            if name.endswith('weight'):
                torch.nn.init.orthogonal_(v)

    def forward(self, x1):
        v1 = self.__linear(x1)
        v2 = (v1 - 5)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument mat1 in method wrapper_CUDA_addmm)

jit:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument mat1 in method wrapper_CUDA_addmm)
'''
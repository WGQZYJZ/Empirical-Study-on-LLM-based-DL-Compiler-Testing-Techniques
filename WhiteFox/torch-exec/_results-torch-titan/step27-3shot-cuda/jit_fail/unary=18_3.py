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
        self.conv1 = nn.Conv2d(4, 8, kernel_size=1)
        self.conv2 = nn.Conv2d(8, 4, kernel_size=5, stride=2)
        self.conv3 = torch.nn.Conv2d(4, 8, kernel_size=(1, 2), stride=(2, 1), padding=(0, 1), dilation=(1, 2))

    def forward(self, x1):
        x = torch.randn(1, 4, 5, 5)
        v1 = self.conv1(x)
        v1 = self.conv2(v1)
        v2 = self.conv3(x)
        return (v1, v2)




func = Model().to('cuda')



x1 = torch.randn(1, 4, 5, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument weight in method wrapper_CUDA___slow_conv2d_forward)

jit:
Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument weight in method wrapper_CUDA___slow_conv2d_forward)
'''
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
        self.features = torch.nn.Sequential(torch.nn.Conv2d(3, 24, 5, 1, 2), torch.nn.Conv2d(24, 48, 1, 1, 0), torch.nn.Conv2d(24, 48, 1, 1, 0))
        if True:
            self.pad = torch.nn.Sequential(torch.nn.ConstantPad2d([0, 0, 1, 1], value=0.422196), torch.nn.PixelShuffle(2))
        self.res = torch.nn.Sequential(torch.nn.Conv2d(48, 48, 3, 2, 0, dilation=1, groups=24), torch.nn.ReLU(), torch.nn.Conv2d(48, 192, 1, 1, 0), torch.nn.Conv2d(192, 192, 1, 1, 0))
        self.relu = torch.nn.Sequential(torch.nn.ReLU(inplace=False), torch.nn.Conv2d(3, 192, 1, 1, 0), torch.nn.MaxPool2d(3, 2, 1), torch.nn.AdaptiveAvgPool2d(7), torch.nn.ReLU(inplace=False), torch.nn.Conv2d(192, 1000, 1, 1, 0))

    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1, 1], dim=0)
        concatenated_tensor = torch.cat(split_tensors, dim=0)
        return (concatenated_tensor, torch.split(v1, [1, 1, 1], dim=0))



func = Model().to('cpu')


v1 = torch.Tensor(3, 47, 224, 1024)

test_inputs = [v1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp4ynaaiyr/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp4ynaaiyr/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp4ynaaiyr', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
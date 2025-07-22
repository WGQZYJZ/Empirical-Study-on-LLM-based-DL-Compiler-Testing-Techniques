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
        self.features = torch.nn.Sequential(torch.nn.ReflectionPad2d([0, 1, 2, 1]), torch.nn.Conv2d(6, 24, (5, 5), stride=(2, 2), padding=[0, 1, 2, 1]))
        self.avgpool1 = torch.nn.Sequential(torch.nn.ReflectionPad2d((3, 0, 3, 0)), torch.nn.AvgPool2d(2, stride=1, padding=[3, 0, 3, 0]))
        self.conv2 = torch.nn.Sequential(torch.nn.ReflectionPad2d((0, 1, 0, 1)), torch.nn.Conv2d(24, 6, (5, 5), stride=(2, 2), padding=[0, 1, 0, 1]))

    def forward(self, v1):
        split_tensors = torch.split(v1, [3, 2, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(v1, [3, 2, 1], dim=1))



func = Model().to('cpu')


v1 = torch.Tensor(1, 6, 4, 4)

test_inputs = [v1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpycrknkoi/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpycrknkoi/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpycrknkoi', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
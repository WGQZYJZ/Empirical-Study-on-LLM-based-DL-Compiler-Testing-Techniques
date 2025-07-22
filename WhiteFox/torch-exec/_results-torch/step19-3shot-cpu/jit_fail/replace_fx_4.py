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

    def forward(self, x1, x2):
        x1 = F.conv2d(x1, torch.ones(1, 1, 7) * 0.2, torch.zeros(1), stride=1, padding=3, groups=1, bias=torch.ones(1))
        x1 = F.avg_pool2d(x1, kernel_size=3, stride=1, padding=1)
        x1 = F.conv2d(x1, torch.ones(1, 7, 1) * 0.5, torch.zeros(1), stride=1, padding=1, groups=1, bias=torch.ones(1))
        x1 = F.conv2d(x1, torch.ones(1, 7, 1) * 0.5, torch.zeros(1), stride=1, padding=2, groups=1, bias=torch.ones(1))
        x1 = F.conv2d(x1, torch.ones(1, 7, 1) * 0.25, torch.zeros(1), stride=1, padding=0, groups=1, bias=torch.ones(1))
        x1 = F.conv2d(x1, torch.ones(1, 1, 7) * 0.125, torch.zeros(1), stride=1, padding=2, groups=1, bias=torch.ones(1))
        x1 = F.avg_pool2d(x1, kernel_size=3, stride=1, padding=1)
        x1 = F.conv2d(x1, torch.ones(1, 7, 1) * 0.25, torch.zeros(1), stride=1, padding=0, groups=1, bias=torch.ones(1))
        x1 = F.conv2d(x1, torch.ones(1, 1, 7) * 0.5, torch.zeros(1), stride=1, padding=0, groups=1, bias=torch.ones(1))
        x1 = F.conv2d(x1, torch.ones(1, 7, 1) * 0.5, torch.zeros(1), stride=1, padding=3, groups=1, bias=torch.ones(1))
        x1 = F.conv2d(x1, torch.ones(1, 1, 7) * 0.5, torch.zeros(1), stride=1, padding=0, groups=1, bias=torch.ones(1))
        x1 = F.max_pool2d(x1, 3, 1, 1)
        x1 = F.conv2d(x1, torch.ones(1, 7, 1) * 0.25, torch.zeros(1), stride=1, padding=0, groups=1, bias=torch.ones(1))
        x1 = F.gelu(x1)
        x1 = torch.cat([x1, x2])
        x1 = F.avg_pool2d(x1, 3, 1, 1)
        x1 = x1.reshape(x1.size(0), -1)
        x1 = torch.nn.functional.dropout(x1, p=0.8, training=True)
        return x1



func = Model().to('cpu')


x1 = torch.randn(1, 2048, 7, 7)

x2 = torch.randn(1, 2048)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (Tensor, Tensor, Tensor, groups=int, bias=Tensor, padding=int, stride=int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, tuple of ints padding = 0, tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the keywords were incorrect: groups, bias, padding, stride
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, str padding = "valid", tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the keywords were incorrect: groups, bias, padding, stride


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpd1k5u2zh/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpd1k5u2zh/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpd1k5u2zh', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
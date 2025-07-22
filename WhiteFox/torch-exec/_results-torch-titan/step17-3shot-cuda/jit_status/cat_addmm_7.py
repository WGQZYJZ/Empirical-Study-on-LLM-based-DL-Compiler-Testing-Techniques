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



class Model(nn.Module):

    def __init__(self, input_channels, output_channels, kernel):
        super().__init__()
        self.layers = nn.Conv2d(input_channels, output_channels, kernel)

    def forward(self, x):
        x = self.layers(x)
        return x




input_channels = 3


output_channels = 6


kernel = 2


func = Model(input_channels, output_channels, kernel).to('cuda')



x = torch.randn(20, 3, 299, 299)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpkom6cuq5/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpkom6cuq5', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpkom6cuq5/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.features = torch.nn.ModuleDict({'conv2d': torch.nn.Conv2d(3, 32, 3, 1, 1), 'add': torch.nn.ReLU(), 'add_1': torch.nn.ReLU(), 'linear': torch.nn.Linear(1, 1), 'conv2d_1': torch.nn.Conv2d(32, 32, 3, 1, 1)})

    def forward(self, input, **kwargs):
        split_tensors = torch.split(input, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (self.features['conv2d'](concatenated_tensor), split_tensors)




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmptj7kv3si/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmptj7kv3si', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmptj7kv3si/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.features = torch.nn.Sequential(torch.nn.Linear(10, 32), torch.nn.ReLU(inplace=True))
        self.split = torch.nn.Sequential(torch.nn.BatchNorm1d(32), torch.nn.Linear(32, 32), torch.nn.ReLU(inplace=True), torch.nn.Linear(32, 1))
        self.concat = torch.nn.Sequential(torch.nn.Linear(32, 32), torch.nn.BatchNorm1d(32), torch.nn.Linear(32, 32), torch.nn.ReLU(inplace=True))

    def forward(self, x1):
        x1 = self.features(x1)
        split_tensors = torch.split(x1, [1, 1, 1, 1, 1], dim=0)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(x1, [1, 1, 1, 1, 1], dim=0))




func = Model().to('cuda')



x1 = torch.randn(5, 10, requires_grad=True)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp88ljoic9/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp88ljoic9', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp88ljoic9/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
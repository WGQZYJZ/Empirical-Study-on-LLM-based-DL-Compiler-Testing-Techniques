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
        self.conv1 = torch.nn.Conv1d(7, 7, 3)
        self.conv2 = torch.nn.Conv1d(7, 8, 3)
        torch.manual_seed(1)
        self.bn1 = torch.nn.BatchNorm1d(7)
        torch.manual_seed(0)
        self.bn2 = torch.nn.BatchNorm1d(8)
        torch.manual_seed(1)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        t1 = self.relu(self.bn1(self.conv1(x1)))
        t2 = self.relu(self.bn2(self.conv2(t1)))
        y = torch.tanh(t2)
        return (t1, t2, y)




func = Model().to('cuda')



x1 = torch.randn(1, 7, 6)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpbsqufmks/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpbsqufmks', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpbsqufmks/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
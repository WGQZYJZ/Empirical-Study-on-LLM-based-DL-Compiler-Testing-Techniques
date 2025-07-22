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
        self.layer1 = torch.nn.Sequential(torch.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1), torch.nn.BatchNorm2d(num_features=16), torch.nn.ReLU(), torch.nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer2 = torch.nn.Sequential(torch.nn.Conv2d(in_channels=16, out_channels=32, kernel_size=5, stride=1, padding=2), torch.nn.BatchNorm2d(num_features=32), torch.nn.ReLU(), torch.nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer3 = torch.nn.Sequential(torch.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1), torch.nn.BatchNorm2d(num_features=64), torch.nn.ReLU(), torch.nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer4 = torch.nn.Sequential(torch.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=3, stride=1, padding=1))

    def forward(self, x1):
        v1 = self.layer1.forward(x1)
        v2 = self.layer2.forward(v1)
        v3 = self.layer3.forward(v2)
        v4 = self.layer4.forward(v3)
        v5 = torch.sigmoid(v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpzmkgiuwr/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpzmkgiuwr', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpzmkgiuwr/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
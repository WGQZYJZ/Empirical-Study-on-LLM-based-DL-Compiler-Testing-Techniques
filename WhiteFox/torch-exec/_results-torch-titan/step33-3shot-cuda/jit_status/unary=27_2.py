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



class MnistModel(torch.nn.Module):

    def __init__(self, min, max):
        super(MnistModel, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 20, kernel_size=5)
        self.conv2 = torch.nn.Conv2d(20, 20, kernel_size=5)
        self.conv2_drop = torch.nn.Dropout2d()
        self.fc1 = torch.nn.Linear(320, 50)
        self.fc2 = torch.nn.Linear(50, 10)
        self.max = min
        self.min = max

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2(x), 2))
        x = x.view((- 1), 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        x = torch.clamp_min(x, self.min)
        x = torch.clamp_max(x, self.max)
        return F.log_softmax(x, dim=1)




min = 0.0


max = 1.0


func = MnistModel(min, max).to('cuda')



x = torch.randn(1, 1, 28, 28, requires_grad=True)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpl8vukk76/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpl8vukk76', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpl8vukk76/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
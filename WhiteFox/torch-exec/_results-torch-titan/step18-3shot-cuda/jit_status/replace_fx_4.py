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



class MyModel(torch.nn.Module):

    def __init__(self):
        super(MyModel, self).__init__()

    def forward(self, a):
        a = a.unsqueeze(dim=(- 1))
        a = torch.nn.functional.dropout(input=a, p=0.5, training=self.training, inplace=False)
        a = a.squeeze(dim=(- 1))
        return a




func = MyModel().to('cuda')



a1 = torch.rand([8, 2, 3])


test_inputs = [a1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp2621jm4m/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp2621jm4m', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp2621jm4m/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
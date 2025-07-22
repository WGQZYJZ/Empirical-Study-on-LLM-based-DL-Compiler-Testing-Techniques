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

    def forward(self, z):
        t1 = torch.nn.functional.dropout(z, p=0.3)
        t2 = torch.rand_like(z)
        t3 = torch.nn.functional.dropout(z, p=0.4)
        t4 = torch.nn.functional.dropout(z, p=0.3)
        t5 = torch.nn.functional.dropout(z, p=0.2)
        return ((((t1 + t2) + t3) + t4) + t5)




func = MyModel().to('cuda')



z1 = torch.zeros([1, 2])


test_inputs = [z1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp7t_t5tl1/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp7t_t5tl1', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp7t_t5tl1/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
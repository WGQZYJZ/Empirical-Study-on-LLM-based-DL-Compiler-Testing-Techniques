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

    def forward(self, input1, input2):
        y1 = torch.mm(input1, input1)
        y2 = torch.mm(input2, input2)
        y3 = torch.mm(input1, input2)
        return ((((((y1 + y2) + y3) + (y1 * y2)) + (y2 * y3)) + (y2 * y2)) + y3)




func = Model().to('cuda')



input1 = torch.randn(50, 50)



input2 = torch.randn(50, 50)


test_inputs = [input1, input2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp9d6pmv70/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp9d6pmv70', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp9d6pmv70/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
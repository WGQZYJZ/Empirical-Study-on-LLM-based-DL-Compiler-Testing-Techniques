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

    def forward(self, tensor1, tensor2):
        t1 = torch.mm(tensor1, tensor1)
        t2 = torch.mm(tensor2, tensor2)
        t3 = torch.mm(t1, t1)
        t4 = torch.mm(t2, t2)
        t5 = torch.mm(t3, t3)
        t1 = (t3 + t5)
        t6 = torch.mm(t4, t4)
        t2 = (t6 + t1)
        return (((t3 + t6) + t1) + t2)




func = Model().to('cuda')



tensor1 = torch.randn(100, 100)



tensor2 = torch.randn(100, 100)


test_inputs = [tensor1, tensor2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpnzpdyobx/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpnzpdyobx', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpnzpdyobx/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
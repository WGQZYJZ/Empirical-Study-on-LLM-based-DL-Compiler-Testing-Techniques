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



class ModelA(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=0.2)

    def forward(self, x):
        b1 = self.dropout(x)
        return b1




class ModelB(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        b1 = (x * 2)
        c1 = torch.nn.functional.dropout(b1, p=0.5)
        c2 = torch.nn.functional.dropout(c1, p=0.5)
        c3 = (c1 * 2)
        return x




class model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        p1 = torch.nn.functional.dropout(x, p=0.3)
        p2 = torch.nn.functional.dropout(p1, p=0.4)
        p3 = torch.nn.functional.dropout(y, p=0.3)
        p4 = torch.nn.functional.dropout(p2, p=0.7)
        p5 = torch.nn.functional.dropout(p3, p=0.2)
        p6 = torch.nn.functional.dropout(p4, p=0.2)
        return (p5, p6)




func = model().to('cuda')



x1 = torch.randn(1, 28)



x2 = torch.randn(1, 4)


test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmppckywq0h/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmppckywq0h', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmppckywq0h/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
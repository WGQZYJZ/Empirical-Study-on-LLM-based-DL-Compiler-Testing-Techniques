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
        self.linear = torch.nn.Linear(7, 7)

    def forward(self, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
        v11 = x1
        v1 = torch.nn.functional.linear(v11, self.linear.weight, self.linear.bias)
        v2 = v1.permute(0, 2, 1)
        v12 = x2
        v3 = torch.nn.functional.linear(v12, self.linear.weight, self.linear.bias)
        v4 = v3.permute(0, 2, 1)
        v5 = x3
        v6 = torch.nn.functional.linear(v5, self.linear.weight, self.linear.bias)
        v7 = v6.permute(0, 2, 1)
        v8 = x4
        v9 = torch.nn.functional.linear(v8, self.linear.weight, self.linear.bias)
        v10 = v9.permute(0, 2, 1)
        v13 = x5
        v14 = torch.nn.functional.linear(v13, self.linear.weight, self.linear.bias)
        v15 = torch.nn.functional.linear(v14, self.linear.weight, self.linear.bias)
        v16 = v15.permute(0, 2, 1)
        v17 = x6
        v18 = torch.nn.functional.linear(v17, self.linear.weight, self.linear.bias)
        v19 = torch.nn.functional.linear(v18, self.linear.weight, self.linear.bias)
        v20 = v19.permute(0, 2, 1)
        v21 = x7
        v22 = torch.nn.functional.linear(v21, self.linear.weight, self.linear.bias)
        v23 = torch.nn.functional.linear(v22, self.linear.weight, self.linear.bias)
        v24 = v23.permute(0, 2, 1)
        v25 = x8
        v26 = torch.nn.functional.linear(v25, self.linear.weight, self.linear.bias)
        v27 = torch.nn.functional.linear(v26, self.linear.weight, self.linear.bias)
        v28 = v27.permute(0, 2, 1)
        v29 = x9
        v30 = torch.nn.functional.linear(v29, self.linear.weight, self.linear.bias)
        v31 = torch.nn.functional.linear(v30, self.linear.weight, self.linear.bias)
        v32 = v31.permute(0, 2, 1)
        v33 = x10
        v34 = torch.nn.functional.linear(v33, self.linear.weight, self.linear.bias)
        return (((((((((v2 + v4) + v7) + v10) + v16) + v20) + v24) + v28) + v32) + v34)




func = Model().to('cuda')



x1 = torch.randn(1, 7, 7, device='cpu')



x2 = torch.randn(1, 7, 7, device='cpu')



x3 = torch.randn(1, 7, 7, device='cpu')



x4 = torch.randn(1, 7, 7, device='cpu')



x5 = torch.randn(1, 7, 7, device='cpu')



x6 = torch.randn(1, 7, 7, device='cpu')



x7 = torch.randn(1, 7, 7, device='cpu')



x8 = torch.randn(1, 7, 7, device='cpu')



x9 = torch.randn(1, 7, 7, device='cpu')



x10 = torch.randn(1, 7, 7, device='cpu')


test_inputs = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpqktcwu2v/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpqktcwu2v', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpqktcwu2v/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
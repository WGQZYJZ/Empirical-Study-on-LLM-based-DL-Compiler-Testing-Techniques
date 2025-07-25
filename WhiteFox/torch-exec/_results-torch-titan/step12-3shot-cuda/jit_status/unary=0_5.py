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
        self.linear1 = torch.nn.Linear(64, 64)
        self.linear2 = torch.nn.Linear(64, 64)
        self.linear3 = torch.nn.Linear(64, 64)
        self.linear4 = torch.nn.Linear(64, 16)

    def forward(self, x):
        v1 = self.linear1(x)
        v2 = (v1 * 0.5)
        v3 = (v1 * v1)
        v4 = (v3 * v1)
        v5 = (v4 * 0.044715)
        v6 = (v1 + v5)
        v7 = (v6 * 0.7978845608028654)
        v8 = torch.tanh(v7)
        v9 = (v8 + 1)
        v10 = (v2 * v9)
        v11 = self.linear2(v10)
        v12 = (v11 * 0.5)
        v13 = (v11 * v11)
        v14 = (v13 * v11)
        v15 = (v14 * 0.044715)
        v16 = (v11 + v15)
        v17 = (v16 * 0.7978845608028654)
        v18 = torch.tanh(v17)
        v19 = (v18 + 1)
        v20 = (v12 * v19)
        v21 = self.linear3(v20)
        v22 = (v21 * 0.5)
        v23 = (v21 * v21)
        v24 = (v23 * v21)
        v25 = (v24 * 0.044715)
        v26 = (v21 + v25)
        v27 = (v26 * 0.7978845608028654)
        v28 = torch.tanh(v27)
        v29 = (v28 + 1)
        v30 = (v22 * v29)
        v31 = self.linear4(v30)
        v32 = (v31 * 0.5)
        v33 = (v31 * v31)
        v34 = (v33 * v31)
        v35 = (v34 * 0.044715)
        v36 = (v31 + v35)
        v37 = (v36 * 0.7978845608028654)
        v38 = torch.tanh(v37)
        v39 = (v38 + 1)
        v40 = (v32 * v39)
        return v40




func = Model().to('cuda')



x = torch.randn(16, 64)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpa1dbi0wi/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpa1dbi0wi', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpa1dbi0wi/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.linear1 = torch.nn.Linear(64, 128)
        self.linear2 = torch.nn.Linear(32, 16)
        self.linear3 = torch.nn.Linear(16, 16)
        self.linear4 = torch.nn.Linear(16, 32)
        self.linear5 = torch.nn.Linear(16, 16)
        self.linear6 = torch.nn.Linear(32, 16)
        self.linear7 = torch.nn.Linear(128, 128)
        self.linear8 = torch.nn.Linear(32, 16)

    def forward(self, x7):
        v1 = self.linear1(x7)
        v2 = v1 * 0.5
        v3 = v1 * v1
        v4 = v3 * v1
        v5 = v4 * 0.044715
        v6 = v1 + v5
        v7 = v6 * 0.7978845608028654
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = v2 * v9
        v11 = self.linear2(v10)
        v12 = v11 * 0.5
        v13 = v11 * v11
        v14 = v13 * v11
        v15 = v14 * 0.044715
        v16 = v11 + v15
        v17 = v16 * 0.7978845608028654
        v18 = torch.tanh(v17)
        v19 = v18 + 1
        v20 = v12 * v19
        v21 = self.linear4(v20)
        v22 = v21 * 0.5
        v23 = v21 * v21
        v24 = v23 * v21
        v25 = v24 * 0.044715
        v26 = v21 + v25
        v27 = v26 * 0.7978845608028654
        v28 = torch.tanh(v27)
        v29 = v28 + 1
        v30 = v22 * v29
        v31 = self.linear5(v30)
        v32 = v31 * 0.5
        v33 = v31 * v31
        v34 = v33 * v31
        v35 = v34 * 0.044715
        v36 = v31 + v35
        v37 = v36 * 0.7978845608028654
        v38 = torch.tanh(v37)
        v39 = v38 + 1
        v40 = v32 * v39
        v41 = self.linear7(v40)
        v42 = v41 * 0.5
        v43 = v41 * v41
        v44 = v43 * v41
        v45 = v44 * 0.044715
        v46 = v41 + v45
        v47 = v46 * 0.7978845608028654
        v48 = torch.tanh(v47)
        v49 = v48 + 1
        v50 = v42 * v49
        v51 = self.linear8(v50)
        v52 = v51 * 0.5
        v53 = v51 * v51
        v54 = v53 * v51
        v55 = v54 * 0.044715
        v56 = v51 + v55
        v57 = v56 * 0.7978845608028654
        v58 = torch.tanh(v57)
        v59 = v58 + 1
        v60 = v52 * v59
        v61 = self.linear6(v60)
        v62 = v61 * 0.5
        v63 = v61 * v61
        v64 = v63 * v61
        v65 = v64 * 0.044715
        v66 = v61 + v65
        v67 = v66 * 0.7978845608028654
        v68 = torch.tanh(v67)
        v69 = v68 + 1
        v70 = v62 * v69
        return v70



func = Model().to('cpu')


x7 = torch.randn(1, 64)

test_inputs = [x7]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x128 and 32x16)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 128)), Parameter(FakeTensor(..., size=(16, 32), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [1, 128] X [32, 16].

from user code:
   File "<string>", line 37, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/linear.py", line 125, in forward
    return F.linear(input, self.weight, self.bias)


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
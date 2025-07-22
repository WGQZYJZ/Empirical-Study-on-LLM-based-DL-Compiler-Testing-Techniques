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

    def __init__(self, size=20):
        super().__init__()
        self.weight = torch.nn.Parameter(torch.empty(size, size))
        self.bias = torch.nn.Parameter(torch.empty(size, size))
        torch.nn.init.normal_(self.weight, std=0.1)
        torch.nn.init.normal_(self.bias, std=0.1)

    def forward(self, x1, other=None):
        v1 = torch.matmul(x1, self.weight)
        if (other is not None):
            v1 += other
        v2 = torch.matmul(v1, self.weight)
        v3 = torch.matmul(v1, self.weight)
        v4 = torch.matmul(v3, self.weight)
        v5 = torch.matmul(v3, self.weight)
        v6 = torch.matmul(v5, self.weight)
        v7 = torch.matmul(v5, self.weight)
        v8 = torch.matmul(v7, self.weight)
        v9 = torch.matmul(v7, self.weight)
        v10 = torch.matmul(v9, self.weight)
        v11 = torch.matmul(v9, self.weight)
        v12 = torch.matmul(v11, self.weight)
        v13 = torch.matmul(v11, self.weight)
        v14 = torch.matmul(v13, self.weight)
        v15 = torch.matmul(v13, self.weight)
        v16 = torch.matmul(v15, self.weight)
        v17 = torch.matmul(v15, self.weight)
        v18 = torch.matmul(v17, self.weight)
        v19 = torch.matmul(v17, self.weight)
        v20 = torch.matmul(v19, self.weight)
        v21 = torch.matmul(v19, self.weight)
        v22 = torch.matmul(v21, self.weight)
        v23 = torch.matmul(v21, self.weight)
        v24 = torch.matmul(v23, self.weight)
        v25 = torch.matmul(v23, self.weight)
        v26 = torch.matmul(v25, self.weight)
        v27 = torch.matmul(v25, self.weight)
        v28 = torch.matmul(v27, self.weight)
        v29 = torch.matmul(v27, self.weight)
        v30 = torch.matmul(v29, self.weight)
        v31 = torch.matmul(v29, self.weight)
        v32 = torch.matmul(v31, self.weight)
        v33 = torch.matmul(v31, self.weight)
        v34 = torch.matmul(v31, self.weight)
        v35 = torch.matmul(v31, self.weight)
        v36 = torch.matmul(v31, self.weight)
        v37 = torch.matmul(v31, self.weight)
        v38 = torch.matmul(v31, self.weight)
        v39 = torch.matmul(v31, self.weight)
        v40 = torch.matmul(v31, self.weight)
        v41 = torch.matmul(v31, self.weight)
        v42 = torch.matmul(v31, self.weight)
        v43 = torch.matmul(v31, self.weight)
        v44 = torch.matmul(v31, self.weight)
        return v20



func = Model().to('cuda')



x1 = torch.randn(20, 100)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (20x100 and 20x20)

jit:
Failed running call_function <built-in method matmul of type object at 0x706c1e0699e0>(*(FakeTensor(..., device='cuda:0', size=(20, 100)), Parameter(FakeTensor(..., device='cuda:0', size=(20, 20), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [20, 100] X [20, 20].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
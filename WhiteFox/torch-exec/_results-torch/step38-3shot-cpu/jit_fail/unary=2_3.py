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
        self.module_1 = torch.nn.ModuleList([torch.nn.ConvTranspose2d(2, 5, 3), torch.nn.ConvTranspose2d(2, 6, 1), torch.nn.ConvTranspose2d(2, 7, 1), torch.nn.ConvTranspose2d(2, 8, 1)])
        self.module_2 = 128
        self.module_3 = 128
        self.module_4 = torch.nn.ModuleList([torch.nn.Linear(128, 10), torch.nn.Linear(128, 5)])

    def forward(self, x1):
        v3 = self.module_1[0](x1)
        v5 = self.module_1[1](x1)
        v7 = self.module_1[2](x1)
        v9 = self.module_1[3](x1)
        v15 = self.module_4[0](v3.reshape(x1.shape[0], -1))
        v16 = self.module_4[1](v15)
        v6 = v15 + 0.5
        v18 = self.module_1[0].weight
        v20 = self.module_1[0].bias
        v19 = self.module_1[1].weight
        v21 = self.module_1[1].bias
        v22 = self.module_1[2].weight
        v23 = self.module_1[2].bias
        v24 = self.module_1[3].weight
        v25 = self.module_1[3].bias
        v26 = self.module_4[0].weight
        v27 = self.module_4[0].bias
        v28 = self.module_4[1].weight
        v29 = self.module_4[1].bias
        v11 = v3 * 0.044715
        v33 = self.module_1
        v8 = v3 + v11
        v35 = self.module_4[0]
        v14 = v8 * 0.7978845608028654
        v34 = self.module_4
        v12 = torch.tanh(v14)
        v40 = self.module_3
        v16 = v12 + 1
        v42 = self.module_4[1]
        v41 = self.module_2
        v9 = v9 + 0.5
        v32 = self.module_1[0]
        v13 = v9 * v16
        v1 = v32.bias
        v44 = self.module_4
        v43 = self.module_1[1]
        v17 = v13 * 0.044715
        v46 = self.module_3
        v18 = v1 + v17
        v31 = self.module_1[1]
        v2 = v31.bias
        v48 = self.module_4
        v47 = self.module_1[2]
        v20 = v20 + 0.044715
        v30 = self.module_1[2]
        v19 = v2 + v18
        v50 = self.module_4
        v51 = self.module_1[3]
        v22 = v22 + 0.7978845608028654
        v29 = 50 * self.module_1[3].bias
        v21 = v21 + v19
        v23 = v23 + v14
        v24 = 1 * v24
        v49 = self.module_2
        v53 = self.module_4[1]
        v55 = self.module_3
        v25 = 1 * v25
        v52 = self.module_1[3]
        v26 = v27 + 0.7978845608028654
        v28 = v28 + v13
        v39 = self.module_4[0]
        v37 = self.module_1[0]
        v38 = self.module_4[1]
        v17 = v26 * v21
        v27 = v28 * v25 * 1.0
        v36 = self.module_4[1]
        v10 = v24 * v1
        v45 = self.module_1[2]
        v11 = v10 * 0.5
        v33 = self.module_2
        v12 = v10 * v10 * v10
        v34 = self.module_3
        v21 = self.module_2
        v32 = self.module_4[0]
        v9 = v21 * self.module_1[1].bias
        v40 = self.module_1[2].bias
        v13 = v9 * 0.5
        v14 = v9 * v9 * v9
        v41 = self.module_3
        v15 = v32.bias
        v22 = v21 * self.module_1[2].bias
        v31 = self.module_4[0]
        v16 = v22 * 0.5
        v30 = self.module_1[3]
        v17 = v15 * v13
        v23 = v21 * self.module_1[3].bias
        v42 = self.module_1[0].bias
        v24 = v23 * 1.0
        v25 = v23 * v23
        v43 = self.module_3
        v26 = v31.bias
        v27 = v30.bias
        v28 = v26 * 0.5
        v39 = v24 * v28
        v44 = self.module_1[3]
        v49 = v30.bias
        return v17



func = Model().to('cpu')


x1 = torch.randn(5, 5, 5, 5)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [2, 5, 3, 3], expected input[5, 5, 5, 5] to have 2 channels, but got 5 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7bb142396ec0>(*(FakeTensor(..., size=(5, 5, 5, 5)), Parameter(FakeTensor(..., size=(2, 5, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(5,), requires_grad=True)), (1, 1), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [2, 5, 3, 3], expected input[5, 5, 5, 5] to have 2 channels, but got 5 channels instead

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
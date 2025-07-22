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
        self.conv_transpose2d = torch.nn.ConvTranspose2d(10, 6, 1, stride=1)

    def forward(self, x1):
        v1 = self.conv_transpose2d(x1)
        v2 = v1 * 0.6931471805599453
        v3 = v2 + 0.916290731874155
        v4 = torch.asin(v3)
        v5 = v4 * 0.7788007830714044
        v6 = torch.sinh(v4)
        v7 = torch.exp(v2)
        v8 = v6 + 0.6364014689549419
        v9 = v7 + 0.8580784870267076
        return v9

class ModelB(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_transpose2d = torch.nn.ConvTranspose2d(6, 12, 1, stride=1)

    def forward(self, x1):
        v1 = self.conv_transpose2d(x1)
        v2 = v1 * 0.3025268441530259
        v3 = v2 + 0.6931471805599453
        v4 = torch.asin(v3)
        v5 = v4 * 0.8224626832041365
        v6 = torch.sinh(v4)
        v7 = torch.exp(v2)
        v8 = v6 + 0.911927109559151
        v9 = v7 + 0.9753444664053098
        return v9

class ModelC(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_transpose2d = torch.nn.ConvTranspose2d(12, 20, 1, stride=1)

    def forward(self, x1):
        v1 = self.conv_transpose2d(x1)
        v2 = v1 * 0.5108256237659907
        v3 = v2 + 0.6931471805599453
        v4 = torch.asin(v3)
        v5 = v4 * 0.8961688482627711
        v6 = torch.sinh(v4)
        v7 = torch.exp(v2)
        v8 = v6 + 1.0986089809758952
        v9 = v7 + 1.0218674335299378
        return v9

class ModelD(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_transpose2d = torch.nn.ConvTranspose2d(20, 23, 1, stride=1)

    def forward(self, x1):
        v1 = self.conv_transpose2d(x1)
        v2 = torch.acos(v1)
        v3 = torch.cosh(v1)
        v4 = torch.exp(v1)
        v5 = v3 + 0.6931471805599453
        v6 = v4 + 0.8744512686152957
        v7 = torch.tanh(v2)
        v8 = torch.exp(v1)
        v9 = v7 + 1.0986089809758952
        v10 = v8 + 1.3132616875182228
        return v10

class ModelE(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_transpose2d = torch.nn.ConvTranspose2d(10, 16, 1, stride=1)

    def forward(self, x1):
        v1 = self.conv_transpose2d(x1)
        v2 = v1 * 0.3025809263930141
        v3 = v1 * 0.887558665268145
        v4 = torch.asin(v3)
        v5 = v1 - 0.6931471805599453
        v6 = torch.sinh(v1)
        v7 = torch.exp(v3)
        v8 = v4 * 0.530919307325527
        v9 = v4 * 0.805914723098916
        return v10

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.modelA = ModelA()
        self.modelB = ModelB()
        self.modelC = ModelC()
        self.modelD = ModelD()
        self.modelE = ModelE()
        self.conv_transpose1 = torch.nn.ConvTranspose2d(24, 23, 1, stride=1)

    def forward(self, x1):
        v1 = self.modelA(x1)
        v2 = self.modelB(x1)
        v3 = self.modelC(x1)
        v4 = self.modelD(x1)
        v5 = self.modelE(x1)
        v6 = v4 + v5
        v7 = v1 * v6
        v8 = v2 * v6
        v9 = v3 + v4
        v10 = v7 + v9
        v11 = v8 + v9
        v12 = v5 + v6
        v13 = v10 + v12
        v14 = v11 + v12
        v15 = v10 * v11
        v16 = v14 + v15
        v17 = v14 * v12
        v18 = v17 + v15
        v19 = v15 + v16
        v20 = v16 * v17
        v21 = v18 + v19
        v22 = v17 * v18
        v23 = v18 + v21
        v24 = v16 * v19
        v25 = v24 + v23
        v26 = v2 * v3
        v27 = v22 + v24
        v28 = v26 * v25
        v29 = v26 + v27
        v30 = v22 * v28
        v31 = v26 + v28
        v32 = v22 * v30
        v33 = v30 + v31
        v34 = v28 * v30
        v35 = v30 * v32
        v36 = v33 + v34
        v37 = v34 + v35
        v38 = v35 + v37
        v39 = v36 * v37
        v40 = v36 * v38
        v41 = v34 * v40
        v42 = v38 * v41
        v43 = v36 * v42
        v44 = v38 * v40
        v45 = v32 * v38
        v46 = v45 + v44
        v47 = v45 * v43
        v48 = v46 + v47



func = Model().to('cpu')


x1 = torch.randn(1, 10, 15, 15)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [6, 12, 1, 1], expected input[1, 10, 15, 15] to have 6 channels, but got 10 channels instead

jit:
Failed running call_function <built-in method conv_transpose2d of type object at 0x7eecdfd96ec0>(*(FakeTensor(..., size=(1, 10, 15, 15)), Parameter(FakeTensor(..., size=(6, 12, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(12,), requires_grad=True)), (1, 1), (0, 0), (0, 0), 1, (1, 1)), **{}):
Given transposed=1, weight of size [6, 12, 1, 1], expected input[1, 10, 15, 15] to have 6 channels, but got 10 channels instead

from user code:
   File "<string>", line 117, in forward
  File "<string>", line 38, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 1162, in forward
    return F.conv_transpose2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def forward(self, x1):
        v1 = torch.squeeze(x1, 1)
        v2 = (v1 - 60)
        v3 = V1(v2)
        v4 = F.relu(v3)
        v5 = V2(v4)
        v6 = F.relu(v5)
        v7 = V3(v6)
        v8 = F.relu(v7)
        v9 = V4(v8)
        v10 = F.relu(v9)
        v11 = V5(v10)
        v12 = F.relu(v11)
        v13 = V6(v12)
        v14 = F.relu(v13)
        v15 = V9(v14)
        v16 = F.relu(v15)
        return v16




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = (x1 - 4)
        v2 = V1(v1)
        v3 = F.relu(v2)
        v4 = V2(v3)
        v5 = F.relu(v4)
        v6 = V3(v5)
        v7 = F.relu(v6)
        v8 = V4(v7)
        v9 = F.relu(v8)
        v10 = V5(v9)
        v11 = F.relu(v10)
        v12 = V6(v11)
        v13 = F.relu(v12)
        v14 = V9(v13)
        v15 = F.relu(v14)
        return v15




func = Model().to('cuda')



x1 = torch.randn(1, 1, 128)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'V1' is not defined

jit:
name 'V1' is not defined

from user code:
   File "<string>", line 49, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
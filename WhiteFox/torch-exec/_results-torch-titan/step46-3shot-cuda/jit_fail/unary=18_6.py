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
        self.conv1 = torch.nn.Conv2d(1, 16, (2, 2), stride=(1, 1), padding=(1, 1))
        self.conv2 = torch.nn.Conv2d(16, 16, (2, 2), stride=(1, 1), padding=(1, 1))
        self.conv3 = torch.nn.Conv2d(16, 32, (2, 2), stride=(1, 1), padding=(3, 3))
        self.conv4 = torch.nn.Conv2d(32, 64, (2, 2), stride=(1, 1), padding=(3, 3))
        self.conv5 = torch.nn.ConvTranspose2d(64, 64, (2, 2), stride=(1, 1), padding=(4, 4))
        self.conv6 = torch.nn.ConvTranspose2d(64, 32, (3, 3), stride=(1, 1), padding=(4, 4))
        self.conv7 = torch.nn.ConvTranspose2d(32, 16, (2, 2), stride=(1, 1), padding=(4, 4))
        self.conv8 = torch.nn.ConvTranspose2d(16, 2, (2, 2), stride=(1, 1), padding=(4, 4))

    def forward(self, x1):
        v0 = x1.to(torch.int32)
        v1 = torch.relu(v0)
        v2 = self.conv1(v1)
        v3 = np.exp(v2)
        v4 = torch.sin(v3)
        v5 = self.conv2(v4)
        v6 = torch.log(v5)
        v7 = np.log(v6)
        v8 = torch.sinh(v7)
        v9 = self.conv3(v8)
        v10 = torch.cos(v9)
        v15 = np.tanh(v10)
        v11 = F.tanh(v10)
        v12 = torch.cos(v11)
        v13 = torch.tanh(v12)
        v14 = torch.sin(v13)
        v15 = torch.asinh(v14)
        v16 = self.conv4(v15)
        v17 = torch.acos(v16)
        v18 = self.conv5(v17)
        v19 = torch.tan(v18)
        v20 = self.conv6(v19)
        v21 = torch.asin(v20)
        v22 = self.conv7(v21)
        v23 = F.tanh(v22)
        v24 = torch.tan(v23)
        v25 = F.silu(v24)
        v26 = self.conv8(v25)
        v27 = torch.tanh(v26)




func = Model().to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'to'

jit:
'int' object has no attribute 'to'

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
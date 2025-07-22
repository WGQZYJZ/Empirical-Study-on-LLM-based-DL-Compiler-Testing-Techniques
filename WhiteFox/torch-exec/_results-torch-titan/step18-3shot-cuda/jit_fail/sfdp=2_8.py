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

    def __init__(self, __param0__, __param1__, __param2__):
        super().__init__()

    def forward(self, __x0__, __x1__):
        scaled_qk = (torch.matmul(__x0__, __x1__.__T__) * (1.0 / __param0__))
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, __param1__)
        output = torch.matmul(dropout_qk, __x1__)
        return output



__param0__ = 1
__param1__ = 1
__param2__ = 1
func = Model(__param0__, __param1__, __param2__).to('cuda')



x0 = torch.randn(1, 64, 64, 64)



x1 = torch.randn(1, 512, 64, 64)


test_inputs = [x0, x1]

# JIT_FAIL
'''
direct:
'Tensor' object has no attribute '__T__'

jit:
'Tensor' object has no attribute '__T__'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
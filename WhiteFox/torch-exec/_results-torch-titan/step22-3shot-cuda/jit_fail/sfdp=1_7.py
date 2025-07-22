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
        self.dropout_p = dropout_p

    def forward(self, input_tensor1, input_tensor2, input_tensor3):
        qk = torch.matmul(input_tensor1, input_tensor2.transpose((- 2), (- 1)))
        inv_scale_factor = (1.0 / (input_tensor2.size((- 1)) ** 0.5))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(input_tensor3)
        return output



func = Model().to('cuda')



x1 = torch.randn(1, 20, 5)



x2 = torch.randn(1, 5, 20)



x3 = torch.randn(5, 20)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 5] but got: [1, 20].

jit:
Failed running call_function <built-in method matmul of type object at 0x775e288699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 20, 5)), FakeTensor(..., device='cuda:0', size=(1, 20, 5))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 5] but got: [1, 20].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
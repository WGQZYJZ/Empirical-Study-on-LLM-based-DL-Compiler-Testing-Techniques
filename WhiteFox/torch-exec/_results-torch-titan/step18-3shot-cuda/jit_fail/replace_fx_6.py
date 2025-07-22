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



class MyModel(torch.nn.Module):

    def __init__(self):
        super(MyModel, self).__init__()

    def forward(self, args, kwargs):
        t1 = torch.nn.functional.dropout(input_1=args, p=0.3)
        t2 = torch.nn.functional.dropout(input=kwargs, p=0.4)
        return (t2 + t1)




func = MyModel().to('cuda')



args1 = torch.zeros(3, 4)



kwargs1 = torch.ones(3, 4)


test_inputs = [args1, kwargs1]

# JIT_FAIL
'''
direct:
dropout() got an unexpected keyword argument 'input_1'

jit:
Failed running call_function <function dropout at 0x751f8e79e8b0>(*(), **{'input_1': FakeTensor(..., device='cuda:0', size=(3, 4)), 'p': 0.3}):
dropout() got an unexpected keyword argument 'input_1'

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
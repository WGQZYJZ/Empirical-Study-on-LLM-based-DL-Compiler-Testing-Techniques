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

    def forward(self, x, weight, bias=None, stride=1, padding=0, dilation=1, groups=1):
        x = torch.ops.aten.conv2d(x, weight, bias, stride, padding, dilation, groups)
        return x




func = Model().to('cuda')



x = torch.randn(1024, 35, 35)



w = torch.randn(35, 1024, 5, 5)

weight = 1

test_inputs = [x, w, weight]

# JIT_FAIL
'''
direct:
Overloaded torch operator invoked from Python failed to many any schema:
aten::conv2d() Expected a value of type 'Optional[Tensor]' for argument 'bias' but instead found type 'int'.
Position: 2
Value: 1
Declaration: aten::conv2d(Tensor input, Tensor weight, Tensor? bias=None, int[2] stride=1, SymInt[2] padding=[0, 0], int[2] dilation=1, int groups=1) -> Tensor
Cast error details: Unable to cast 1 to Tensor

aten::conv2d() Expected a value of type 'Optional[Tensor]' for argument 'bias' but instead found type 'int'.
Position: 2
Value: 1
Declaration: aten::conv2d.padding(Tensor input, Tensor weight, Tensor? bias=None, int[2] stride=1, str padding="valid", int[2] dilation=1, int groups=1) -> Tensor
Cast error details: Unable to cast 1 to Tensor



jit:
Failed running call_function aten.conv2d(*(FakeTensor(..., device='cuda:0', size=(1024, 35, 35)), FakeTensor(..., device='cuda:0', size=(35, 1024, 5, 5)), 1, 1, 0, 1, 1), **{}):
Overloaded torch operator invoked from Python failed to many any schema:
aten::conv2d() Expected a value of type 'Optional[Tensor]' for argument 'bias' but instead found type 'int'.
Position: 2
Value: 1
Declaration: aten::conv2d(Tensor input, Tensor weight, Tensor? bias=None, int[2] stride=1, SymInt[2] padding=[0, 0], int[2] dilation=1, int groups=1) -> Tensor
Cast error details: Unable to cast 1 to Tensor

aten::conv2d() Expected a value of type 'Optional[Tensor]' for argument 'bias' but instead found type 'int'.
Position: 2
Value: 1
Declaration: aten::conv2d.padding(Tensor input, Tensor weight, Tensor? bias=None, int[2] stride=1, str padding="valid", int[2] dilation=1, int groups=1) -> Tensor
Cast error details: Unable to cast 1 to Tensor



from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
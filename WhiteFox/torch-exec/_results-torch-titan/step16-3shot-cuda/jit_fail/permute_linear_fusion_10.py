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



class t1(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)




class t2(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.t1 = t1()
        self.t2 = t2()

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.t1.linear.weight, self.t1.linear.bias)
        v2 = torch.ops.prim.NumToTensor(v2)
        v3 = torch.nn.functional.relu(v2)
        v1 = x1.permute(0, 2, 1)
        v2 = torch.ops.prim.NumToTensor(v1)
        v4 = torch.matmul(v2, v3)
        v5 = torch.mul(v2, v3)
        v5 = torch.nn.functional.relu(v5)
        v5 = torch.add(v5, v3)
        v6 = torch.ops.prim.NumToTensor(v5)
        v5 = (v5 * v4)
        v6 = torch.nn.functional.relu(v6)
        v5 = (v5 + v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Overloaded torch operator invoked from Python failed to many any schema:
prim::NumToTensor() Expected a value of type 'number' for argument 'a' but instead found type 'Tensor'.
Position: 0
Value: tensor([[[ 0.1338,  0.0609],
         [-0.1677, -0.4472]]], device='cuda:0')
Declaration: prim::NumToTensor.Scalar(Scalar a) -> Tensor
Cast error details: Cannot cast tensor([[[ 0.1338,  0.0609],
         [-0.1677, -0.4472]]], device='cuda:0') to number

prim::NumToTensor() Expected a value of type 'bool' for argument 'a' but instead found type 'Tensor'.
Position: 0
Value: tensor([[[ 0.1338,  0.0609],
         [-0.1677, -0.4472]]], device='cuda:0')
Declaration: prim::NumToTensor.bool(bool a) -> Tensor
Cast error details: Unable to cast Python instance of type <class 'torch.Tensor'> to C++ type '?' (#define PYBIND11_DETAILED_ERROR_MESSAGES or compile in debug mode for details)



jit:
Failed running call_function prim.NumToTensor(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)),), **{}):
Overloaded torch operator invoked from Python failed to many any schema:
prim::NumToTensor() Expected a value of type 'number' for argument 'a' but instead found type 'FakeTensor'.
Position: 0
Value: FakeTensor(..., device='cuda:0', size=(1, 2, 2))
Declaration: prim::NumToTensor.Scalar(Scalar a) -> Tensor
Cast error details: Cannot cast FakeTensor(..., device='cuda:0', size=(1, 2, 2)) to number

prim::NumToTensor() Expected a value of type 'bool' for argument 'a' but instead found type 'FakeTensor'.
Position: 0
Value: FakeTensor(..., device='cuda:0', size=(1, 2, 2))
Declaration: prim::NumToTensor.bool(bool a) -> Tensor
Cast error details: Unable to cast Python instance of type <class 'torch._subclasses.fake_tensor.FakeTensor'> to C++ type '?' (#define PYBIND11_DETAILED_ERROR_MESSAGES or compile in debug mode for details)



from user code:
   File "<string>", line 43, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
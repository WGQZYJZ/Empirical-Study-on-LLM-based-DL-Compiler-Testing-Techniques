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

        def v2(x):
            v2_output = torch.matmul(x.permute(0, 2, 1), x1)
            return v2_output
        self.f = torch.jit.trace(v2, x2)

    def forward(self, x1, x2):
        v1 = self.f(x2)
        v3 = torch.bmm(v1, x2.permute(0, 2, 1))
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)



x2 = torch.randn(1, 2, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The following operation failed in the TorchScript interpreter.
Traceback of TorchScript (most recent call last):
<string>(21): v2
/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/jit/_trace.py(866): trace
/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/_dynamo/external_utils.py(17): inner
/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/_dynamo/eval_frame.py(328): _fn
<string>(23): __init__
<string>(33): <module>
/home/yujunzhe/WhiteFox/whitefox/torch-exec/torch_utils.py(214): test_wrapper
<string>(1): <module>
template_exec.py(270): _cross_check
template_exec.py(362): core_oracle
template_exec.py(383): core_loop
template_exec.py(456): main
template_exec.py(460): <module>
RuntimeError: Expected all tensors to be on the same device, but found at least two devices, cuda:0 and cpu! (when checking argument for argument mat2 in method wrapper_CUDA_bmm)


jit:
Failed running call_function <built-in method matmul of type object at 0x7876f1a699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)), FakeTensor(..., size=(1, 2, 2))), **{}):
Unhandled FakeTensor Device Propagation for aten.bmm.default, found two different devices cuda:0, cpu

from user code:
   File "<string>", line 26, in forward
  File "<string>", line 21, in v2


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
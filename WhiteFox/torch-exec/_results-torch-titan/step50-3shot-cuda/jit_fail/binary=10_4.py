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



class Model(nn.Module):

    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.jit.trace(nn.Linear(5, 5), torch.zeros(5, 5))

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + self.linear.weight)
        if self.other:
            v2 = (v2 + self.other)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'other'

jit:
Failed running call_module L__self___linear(*(FakeTensor(..., device='cuda:0', size=(1, 5)),), **{}):
The following operation failed in the TorchScript interpreter.
Traceback of TorchScript (most recent call last):
/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/linear.py(114): forward
/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py(1508): _slow_forward
/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py(1527): _call_impl
/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/nn/modules/module.py(1518): _wrapped_call_impl
/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/jit/_trace.py(1065): trace_module
/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/jit/_trace.py(798): trace
/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/_dynamo/external_utils.py(17): inner
/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/torch/_dynamo/eval_frame.py(328): _fn
<string>(19): __init__
<string>(30): <module>
/home/yujunzhe/WhiteFox/whitefox/torch-exec/torch_utils.py(214): test_wrapper
<string>(1): <module>
template_exec.py(270): _cross_check
template_exec.py(362): core_oracle
template_exec.py(383): core_loop
template_exec.py(456): main
template_exec.py(460): <module>
RuntimeError: 


from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
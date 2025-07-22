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

    def __init__(self, inv_scale_factor):
        super().__init__()
        self.inv_scale_factor = inv_scale_factor

    def forward(self, query, key, value, dropout_p, mask=None):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk / self.inv_scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


inv_scale_factor = 1

func = Model(inv_scale_factor).to('cpu')


query = torch.randn(1, 1, 50)

key = torch.randn(1, 100, 50)

value = torch.randn(1, 100, 10)
key = torch.randn(1, 100, 50)
query = torch.randn(1, 1, 50)

input_mask = torch.zeros(query.size(0), key.size(-2)).byte()
dropout_p = 1

test_inputs = [query, key, value, input_mask, dropout_p]

# JIT_FAIL
'''
direct:
Boolean value of Tensor with more than one value is ambiguous

jit:
Failed running call_function <function dropout at 0x7ed848b65b80>(*(FakeTensor(..., size=(1, 1, s0)),), **{'p': FakeTensor(..., size=(1, s3), dtype=torch.uint8)}):
Cannot call numel() on tensor with symbolic sizes/strides
Exception raised from throw_cannot_call_with_symbolic at /pytorch/c10/core/TensorImpl.cpp:291 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x96 (0x7ed89e4e81b6 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libc10.so)
frame #1: c10::TensorImpl::throw_cannot_call_with_symbolic(char const*) const + 0x9c (0x7ed89e48ff92 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libc10.so)
frame #2: <unknown function> + 0x666af (0x7ed89e4c06af in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libc10.so)
frame #3: at::native::is_nonzero(at::Tensor const&) + 0x18b (0x7ed8858f7e7b in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_cpu.so)
frame #4: <unknown function> + 0x30bbcc1 (0x7ed8868bbcc1 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_cpu.so)
frame #5: <unknown function> + 0x84b6b7 (0x7ed89924b6b7 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_python.so)
frame #6: <unknown function> + 0x8481d5 (0x7ed8992481d5 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_python.so)
frame #7: <unknown function> + 0x1ac7d17 (0x7ed8852c7d17 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_cpu.so)
frame #8: <unknown function> + 0x1ac8217 (0x7ed8852c8217 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_cpu.so)
frame #9: <unknown function> + 0x84b6b7 (0x7ed89924b6b7 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_python.so)
frame #10: <unknown function> + 0x8481d5 (0x7ed8992481d5 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_python.so)
frame #11: <unknown function> + 0x1ac7d17 (0x7ed8852c7d17 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_cpu.so)
frame #12: <unknown function> + 0x2617a85 (0x7ed885e17a85 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_cpu.so)
frame #13: at::_ops::is_nonzero::call(at::Tensor const&) + 0x18d (0x7ed88610370d in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_cpu.so)
frame #14: <unknown function> + 0x5ca3ea (0x7ed898fca3ea in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_python.so)
frame #15: <unknown function> + 0x5ca5f8 (0x7ed898fca5f8 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_python.so)
frame #16: python() [0x4fcb78]
frame #17: python() [0x5305a9]
frame #18: python() [0x58460e]
<omitting python frames>
frame #21: <unknown function> + 0x924154 (0x7ed899324154 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_python.so)
frame #22: python() [0x4e6afa]
frame #26: <unknown function> + 0x924154 (0x7ed899324154 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_python.so)
frame #27: python() [0x4e6afa]
frame #30: <unknown function> + 0x924154 (0x7ed899324154 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_python.so)
frame #31: python() [0x4e6afa]
frame #34: <unknown function> + 0x924154 (0x7ed899324154 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_python.so)
frame #35: python() [0x4f81d3]
frame #37: <unknown function> + 0x924154 (0x7ed899324154 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_python.so)
frame #38: python() [0x4e6afa]
frame #41: <unknown function> + 0x924154 (0x7ed899324154 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_python.so)
frame #42: python() [0x4e6afa]
frame #45: <unknown function> + 0x924154 (0x7ed899324154 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_python.so)
frame #46: python() [0x4e6afa]
frame #50: <unknown function> + 0x924154 (0x7ed899324154 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_python.so)
frame #51: python() [0x4e6afa]
frame #54: <unknown function> + 0x924154 (0x7ed899324154 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_python.so)
frame #55: python() [0x4e6afa]
frame #58: <unknown function> + 0x924154 (0x7ed899324154 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_python.so)
frame #59: python() [0x4f81d3]
frame #61: <unknown function> + 0x924154 (0x7ed899324154 in /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/lib/libtorch_python.so)
frame #62: python() [0x4f81d3]


from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def __init__(self, min_value=0.5, max_value=3):
        super().__init__()
        self.min_value = min_value
        self.max_value = max_value
        self.tanh2 = torch.nn.Tanh()
        self.conv2d_transpose = torch.nn.ConvTranspose2d(3, 3, 1, stride=1, padding=1)

    def forward(self, tensor):
        v1 = torch.clamp(tensor, self.min_value, self.max_value)
        v2 = self.tanh2(v1)
        v3 = self.conv2d_transpose(v2)
        return v3



func = Model().to('cuda')


tensor = torch.randn(1, 3, 64, 64)

test_inputs = [tensor]

# JIT_STATUS
'''
direct:


jit:

SpeculationLog diverged at index 1 (log had 11 entries):
- Expected: <string>:24 (LOAD_FAST at ip=9)
- Actual: <string>:24 (CALL_FUNCTION at ip=12)
Previous instruction: <string>:23(CALL_FUNCTION @ 7)

There are two usual reasons why this may have occured:
- When Dynamo analysis restarted, the second run took a different path than
  the first.  If this occurred, the previous instruction is the critical instruction that
  behaved differently.
- Speculation entries are only added under certain conditions (as seen in
  step()), e.g., there must exist operators in the graph; those conditions may
  have changed on restart.

If this divergence was intentional, clear the speculation log before restarting (do NOT
do this for graph breaks, you will infinite loop).

Otherwise, please submit a bug report, ideally including the contents of TORCH_LOGS=+dynamo


from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
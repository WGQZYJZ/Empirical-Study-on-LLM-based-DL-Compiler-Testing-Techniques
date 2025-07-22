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
        self.dropout = torch.nn.Dropout(0.7)

    def forward(self, x1):
        x2 = self.dropout(x1)
        x3 = torch.rand_like(x1)
        return x3



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:

SpeculationLog diverged at index 2 (log had 5 entries):
- Expected: <string>:21 (LOAD_GLOBAL at ip=5)
- Actual: <string>:21 (CALL_FUNCTION at ip=8)
Previous instruction: /home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/dropout.py:70(CALL_FUNCTION @ 9)

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
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
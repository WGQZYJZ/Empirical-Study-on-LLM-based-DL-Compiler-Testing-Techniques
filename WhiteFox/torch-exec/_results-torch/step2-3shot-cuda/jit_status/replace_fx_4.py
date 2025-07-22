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
        self.dropout = torch.nn.Dropout(p=0.3, inplace=True)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, self.dropout.p)
        v2 = torch.randn_like(x1)
        return (v1 * v2).sum()



func = Model().to('cuda')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:

SpeculationLog diverged at index 1 (log had 5 entries):
- Expected: <string>:21 (LOAD_GLOBAL at ip=10)
- Actual: <string>:21 (CALL_FUNCTION at ip=13)
Previous instruction: <string>:20(CALL_FUNCTION @ 8)

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
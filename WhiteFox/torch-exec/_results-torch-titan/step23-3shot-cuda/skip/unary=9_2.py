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



func = ().to('cuda')



v1 = torch.randn(1, 3, 64, 64)


v2 = (3 + v1)


v3 = v2.clamp(min=0, max=6)


v3 = v2.clamp(min=0, max=6)


v4 = v3.div(6)



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 16, 32, 32)


test_inputs = [v1, v3, v4, x1, x2]

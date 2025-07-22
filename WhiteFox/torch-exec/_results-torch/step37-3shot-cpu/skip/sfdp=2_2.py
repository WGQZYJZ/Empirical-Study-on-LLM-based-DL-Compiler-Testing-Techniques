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



func = ().to('cpu')


x1 = torch.randn(4, 1024, 3)

x2 = torch.randn(4, 1024, 8)


x3 = torch.randint(1024, (4, 1024, 1), dtype=torch.long)

test_inputs = [x1, x2, x3]

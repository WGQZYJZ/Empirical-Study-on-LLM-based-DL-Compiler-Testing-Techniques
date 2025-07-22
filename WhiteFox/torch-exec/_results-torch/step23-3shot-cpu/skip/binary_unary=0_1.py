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


x = torch.randn(1, 16, 64, 64, requires_grad=True)
x = torch.randn(1, 16, 64, 64, requires_grad=True)
model = torch.nn.Conv2d(16, 16, 1, stride=1, padding=0)
y = model(x)
y = model(x)
z = y.detach()

z = y.detach()
a = torch.relu(z)

test_inputs = [x, y, z, a]

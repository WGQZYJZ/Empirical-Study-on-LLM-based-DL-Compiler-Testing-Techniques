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


x1 = torch.randn(1, 50, requires_grad=True)

x2 = torch.randn(1, 50, requires_grad=True)

x3 = torch.randn(1, 50, requires_grad=True)

x4 = torch.randn(1, 50, requires_grad=True)

x5 = torch.randn(1, 50, requires_grad=True)

test_inputs = [x1, x2, x3, x4, x5]

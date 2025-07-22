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

x = torch.randn(3, 2, 10, 10)
t4 = torch.nn.ConvTranspose2d(2, 2, 2, stride=2)
t5 = t4(x)
x = torch.randn(3, 2, 10, 10)
t4 = torch.nn.ConvTranspose2d(2, 2, 2, stride=2)
t1 = t4(x)

x = torch.randn(3, 2, 10, 10)

test_inputs = [t5, t1, x]

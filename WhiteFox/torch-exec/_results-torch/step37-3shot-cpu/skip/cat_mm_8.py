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


x = torch.randn(8, 8)

x1 = torch.randn(5, 5)

x2 = torch.randn(5, 5)

test_inputs = [x, x1, x2]

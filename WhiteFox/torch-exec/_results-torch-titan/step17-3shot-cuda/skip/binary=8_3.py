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



other = torch.randn(8, 3, 64, 64)



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [other, x1]

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



x1 = torch.randn(3, 3, 10)



x2 = torch.randn(3, 3, 10)



x3 = torch.randn(3, 3, 10)


test_inputs = [x1, x2, x3]

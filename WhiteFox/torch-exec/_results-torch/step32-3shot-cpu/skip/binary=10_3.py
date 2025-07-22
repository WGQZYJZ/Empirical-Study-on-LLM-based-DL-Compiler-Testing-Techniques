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


input_tensor = torch.randn(1, 3, 64, 64)

other = torch.randn(1, 128)

test_inputs = [input_tensor, other]

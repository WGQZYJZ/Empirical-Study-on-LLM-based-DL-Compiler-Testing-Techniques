import torch
from torch import nn
from torch.autograd import Variable
inp = torch.tensor([[(- 2), (- 1), 0, 1, 2]], dtype=torch.float32)
out = torch.nn.functional.hardshrink(inp, lambd=0.5)
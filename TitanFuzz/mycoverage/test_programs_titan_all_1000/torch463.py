import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([(- 1.5), 0, 1.5])
y = torch.nn.functional.gelu(x)
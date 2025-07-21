import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[(- 1), (- 2), (- 3)], [1, 2, 3]])
y = torch.negative(x)
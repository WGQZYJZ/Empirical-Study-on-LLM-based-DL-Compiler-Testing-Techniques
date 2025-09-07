import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([(- 1), 0, 1], dtype=torch.float32)
y = torch.nn.Softsign()
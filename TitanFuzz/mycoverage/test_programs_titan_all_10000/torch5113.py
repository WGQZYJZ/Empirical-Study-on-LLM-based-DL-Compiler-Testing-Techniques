import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([(- 1), 0, 1])
softsign = torch.nn.Softsign()
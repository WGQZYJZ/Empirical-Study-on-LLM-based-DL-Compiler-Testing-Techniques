import torch
from torch import nn
from torch.autograd import Variable
x = torch.ones(5, 5)
x = torch.nn.functional.pad(x, (2, 2), 'constant', 0)
x = torch.nn.functional.pad(x, (2, 2), 'constant', 0)
x = torch.nn.functional.pad(x, (2, 2), 'constant', 0)
x = torch.nn.functional.pad(x, (2, 2), 'constant', 0)
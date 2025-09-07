import torch
from torch import nn
from torch.autograd import Variable

data = [1, 2, 3, 4, 5]
char_storage = torch.CharStorage(data)
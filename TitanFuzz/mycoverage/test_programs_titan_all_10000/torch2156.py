import torch
from torch import nn
from torch.autograd import Variable
data = randint(0, 100, (2, 3))
tensor = torch.from_numpy(data)
median = torch.median(tensor, dim=1)
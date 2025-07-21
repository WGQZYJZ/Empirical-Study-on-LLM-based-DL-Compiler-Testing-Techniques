import torch
from torch import nn
from torch.autograd import Variable
a = torch.tensor([1, 2, 3])
b = torch.tensor([1, 2, 3], dtype=torch.float32)
torch.set_default_dtype(torch.float32)
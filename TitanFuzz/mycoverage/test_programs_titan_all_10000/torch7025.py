import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor(2.0, dtype=torch.float32)
torch.set_default_dtype(torch.float64)
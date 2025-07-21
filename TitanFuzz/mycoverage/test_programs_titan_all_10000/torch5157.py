import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, 2, 3], dtype=torch.float32)
torch.get_default_dtype()
torch.set_default_dtype(torch.float64)
torch.get_default_dtype()
torch.set_default_dtype(torch.float32)
torch.get_default_dtype()
torch.set_default_dtype(torch.float64)
torch.get_default_dtype()
import torch
from torch import nn
from torch.autograd import Variable
tensor_float32 = torch.tensor([1.0, 2.0, 3.0])
tensor_float64 = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float64)
torch.set_default_dtype(torch.float64)
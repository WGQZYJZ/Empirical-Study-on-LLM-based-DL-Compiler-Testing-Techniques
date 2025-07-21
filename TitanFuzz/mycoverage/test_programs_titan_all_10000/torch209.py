import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor(10, 10)
torch.Tensor.uniform_(input_tensor, from_=0, to=1)
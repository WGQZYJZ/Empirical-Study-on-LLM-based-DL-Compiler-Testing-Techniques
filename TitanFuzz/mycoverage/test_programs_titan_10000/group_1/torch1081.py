import torch
from torch import nn
from torch.autograd import Variable

input_tensor = torch.tensor([[1, (- 2), 3], [4, (- 5), 6]])
torch.Tensor.conj_physical_(input_tensor)
import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2], [3, 4]])
vec1 = torch.tensor([1, 2])
vec2 = torch.tensor([3, 4])
torch.Tensor.addr(input_tensor, vec1, vec2, beta=1, alpha=1)
batch1 = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
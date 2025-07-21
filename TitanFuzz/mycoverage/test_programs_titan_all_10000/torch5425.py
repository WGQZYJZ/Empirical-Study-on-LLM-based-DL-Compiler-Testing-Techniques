import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
tensor1 = torch.Tensor([[1, 2, 3], [4, 5, 6]])
tensor2 = torch.Tensor([[1, 2, 3], [4, 5, 6]])
torch.Tensor.addcdiv_(input_tensor, tensor1, tensor2, value=1)
import torch
from torch import nn
from torch.autograd import Variable
input_tensor1 = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.bool)
input_tensor2 = torch.tensor([[0, 1], [1, 0], [1, 1], [0, 0]], dtype=torch.bool)
torch.Tensor.logical_xor_(input_tensor1, input_tensor2)
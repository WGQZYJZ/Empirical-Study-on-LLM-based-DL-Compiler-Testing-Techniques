import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor1 = torch.tensor([[10, 20, 30], [40, 50, 60]])
tensor2 = torch.tensor([[100, 200, 300], [400, 500, 600]])
torch.Tensor.addcmul_(input_tensor, tensor1, tensor2, value=1)
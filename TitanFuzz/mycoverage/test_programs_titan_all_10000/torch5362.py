import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], dtype=torch.float32)
y = torch.nn.Tanh()(x)
x = torch.tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]], dtype=torch.float32)
y = torch.tanh(x)
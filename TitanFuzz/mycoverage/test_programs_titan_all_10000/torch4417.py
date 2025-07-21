import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
y = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
loss = torch.nn.functional.mse_loss(x, y)
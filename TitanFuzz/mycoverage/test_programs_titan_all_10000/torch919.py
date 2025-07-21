import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 5, requires_grad=True)
target_data = torch.randn(3, 5)
loss = torch.nn.functional.l1_loss(input_data, target_data)
input_data = torch.randn(3, 5, requires_grad=True)
target_data = torch.randn(3, 5)
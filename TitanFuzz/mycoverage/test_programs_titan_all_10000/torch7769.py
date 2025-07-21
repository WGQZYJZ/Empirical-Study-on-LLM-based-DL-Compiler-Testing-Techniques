import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
target_data = torch.tensor([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])
loss = torch.nn.functional.l1_loss(input_data, target_data)
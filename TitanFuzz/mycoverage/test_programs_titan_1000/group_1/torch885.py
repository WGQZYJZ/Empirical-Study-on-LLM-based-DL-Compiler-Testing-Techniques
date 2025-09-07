import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
target_data = torch.tensor([[0, 0, 0], [1, 0, 0]], dtype=torch.float32)
loss = torch.nn.functional.l1_loss(input_data, target_data)
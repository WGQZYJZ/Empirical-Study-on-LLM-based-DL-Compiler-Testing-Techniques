import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0]])
target_data = torch.tensor([1, 0])
loss = torch.nn.functional.cross_entropy(input_data, target_data)
import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.nn.functional.one_hot(input_data, num_classes=(- 1))
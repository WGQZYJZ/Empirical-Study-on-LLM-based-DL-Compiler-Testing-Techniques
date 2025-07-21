import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
output_data = torch.nn.functional.one_hot(input_data, num_classes=3)
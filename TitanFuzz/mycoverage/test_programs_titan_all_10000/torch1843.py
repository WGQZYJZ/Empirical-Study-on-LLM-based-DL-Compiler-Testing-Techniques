import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 0, 1, 0], [1, 1, 1, 1], [1, 1, 1, 0], [0, 1, 0, 1]], dtype=torch.float32)
output = torch.nn.functional.alpha_dropout(input_data, p=0.5)
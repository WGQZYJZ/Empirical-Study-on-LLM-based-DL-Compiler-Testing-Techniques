import torch
from torch import nn
from torch.autograd import Variable
input_data = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
input_tensor = torch.tensor(input_data)
output = torch.is_tensor(input_tensor)
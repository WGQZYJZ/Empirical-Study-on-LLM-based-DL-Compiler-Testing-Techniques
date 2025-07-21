import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
test_tensor = torch.tensor([[1, 1, 1], [2, 2, 2]])
isin_result = torch.isin(input_tensor, test_tensor)
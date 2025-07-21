import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([1, 2, 3, 4, 5])
test_elements = torch.tensor([1, 3, 5])
isin_result = torch.isin(input_data, test_elements)
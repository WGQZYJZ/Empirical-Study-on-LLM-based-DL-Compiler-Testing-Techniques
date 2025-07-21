import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
other_data = torch.tensor([[1, 2], [3, 4], [5, 6]])
torch.kron(input_data, other_data)
torch.matmul(input_data, other_data)
torch.mm(input_data, other_data)
torch.mv(input_data, torch.tensor([1, 2, 3]))
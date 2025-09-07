import torch
from torch import nn
from torch.autograd import Variable
input_data = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 20, 30], [40, 50, 60], [70, 80, 90]]]
torch.sparse.mm(torch.tensor(input_data[0]), torch.tensor(input_data[1]))
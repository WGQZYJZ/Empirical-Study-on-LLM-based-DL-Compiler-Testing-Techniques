import torch
from torch import nn
from torch.autograd import Variable
input_data = [1, 2, 3, 4, 5]
x = torch.tensor(input_data)
y = torch.zeros(5, dtype=torch.long)
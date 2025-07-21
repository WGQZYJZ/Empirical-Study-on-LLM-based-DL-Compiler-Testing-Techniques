import torch
from torch import nn
from torch.autograd import Variable
input_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
input_data = torch.tensor(input_data)
output = torch.atanh(input_data)
import torch
from torch import nn
from torch.autograd import Variable
input_data = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]])
input_data = Variable(torch.Tensor(input_data))
input_data = input_data.unsqueeze(0)
output = torch.nn.functional.adaptive_avg_pool1d(input_data, 2)
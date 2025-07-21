'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool1d\ntorch.nn.functional.adaptive_max_pool1d(input, output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
x_data = Variable(torch.Tensor([[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]]))
print('x_data: ', x_data)
y_data = torch.nn.functional.adaptive_max_pool1d(x_data, 3)
print('y_data: ', y_data)
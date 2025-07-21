'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool2d\ntorch.nn.functional.max_pool2d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
from torch.autograd import Variable
import torch
input_data = Variable(torch.Tensor([[[[0, 1, 1.5], [2, 2.5, 3], [3.5, 4, 4.5]]]]))
output = torch.nn.functional.max_pool2d(input_data, kernel_size=2, stride=1, padding=0)
print(input_data.shape)
print(output.shape)
print(output)
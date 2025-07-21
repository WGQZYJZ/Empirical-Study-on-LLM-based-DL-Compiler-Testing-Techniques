'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool1d\ntorch.nn.AvgPool1d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
from torch.nn import AvgPool1d
input_data = torch.tensor([[[1, 2, 3, 4, 5, 6, 7]]])
avg_pool1d = AvgPool1d(kernel_size=3, stride=2)
output = avg_pool1d(input_data)
print('output:\n', output)
print('output shape: ', output.shape)
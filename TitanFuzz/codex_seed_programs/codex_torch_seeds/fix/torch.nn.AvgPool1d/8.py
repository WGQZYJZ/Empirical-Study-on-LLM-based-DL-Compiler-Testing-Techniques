'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AvgPool1d\ntorch.nn.AvgPool1d(kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
input_data = torch.tensor([[[1, 2, 3, 4, 5, 6]]])
print('input data: ', input_data)
avg_pool1d = torch.nn.AvgPool1d(kernel_size=3, stride=1, padding=0, ceil_mode=False, count_include_pad=True)
print('avg_pool1d: ', avg_pool1d)
output = avg_pool1d.forward(input_data)
print('output: ', output)
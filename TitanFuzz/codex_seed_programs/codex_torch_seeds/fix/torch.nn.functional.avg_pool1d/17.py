'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool1d\ntorch.nn.functional.avg_pool1d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
input_data = torch.tensor([[[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]]])
print(torch.nn.functional.avg_pool1d(input_data, kernel_size=3, stride=3))
print(torch.nn.functional.avg_pool1d(input_data, kernel_size=3, stride=3, padding=1))
print(torch.nn.functional.avg_pool1d(input_data, kernel_size=3, stride=3, padding=1, ceil_mode=True))
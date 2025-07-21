'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool1d\ntorch.nn.functional.avg_pool1d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True)\n'
import torch
import torch
input = torch.randn(20, 16, 50)
output = torch.nn.functional.avg_pool1d(input, kernel_size=2)
print(output.size())
output = torch.nn.functional.avg_pool1d(input, kernel_size=2, stride=2)
print(output.size())
output = torch.nn.functional.avg_pool1d(input, kernel_size=2, stride=2, padding=1)
print(output.size())
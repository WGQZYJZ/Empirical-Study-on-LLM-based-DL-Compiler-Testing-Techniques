'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isfinite\ntorch.isfinite(input)\n'
import torch
input = torch.randn(3, 4)
output = torch.isfinite(input)
print('Input: ', input)
print('Output: ', output)
print('All elements of input are finite: ', torch.all(output).item())
print('Any element of input is finite: ', torch.any(output).item())
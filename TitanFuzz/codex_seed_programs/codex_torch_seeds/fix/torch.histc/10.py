'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.histc\ntorch.histc(input, bins=100, min=0, max=0, *, out=None)\n'
import torch
import torch
input = torch.randn(10000)
torch.histc(input, bins=100, min=0, max=0, out=None)
print('PyTorch Version: ', torch.__version__)
print('Input size: ', input.size())
print('Output size: ', torch.histc(input, bins=100, min=0, max=0, out=None).size())
print('Output: ', torch.histc(input, bins=100, min=0, max=0, out=None))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isneginf\ntorch.isneginf(input, *, out=None)\n'
import torch
input = torch.tensor([1, float('Inf'), float('-Inf'), float('nan')])
print(torch.isneginf(input))
'\nTask 4: Call the API torch.isposinf\ntorch.isposinf(input, *, out=None)\n'
print(torch.isposinf(input))
'\nTask 5: Call the API torch.isfinite\ntorch.isfinite(input, *, out=None)\n'
print(torch.isfinite(input))
'\nTask 6: Call the API torch.isinf\ntorch.isinf(input, *, out=None)\n'
print(torch.isinf(input))
'\nTask 7: Call the API torch.isnan\ntorch.isnan(input, *, out=None)\n'
print(torch.isnan(input))
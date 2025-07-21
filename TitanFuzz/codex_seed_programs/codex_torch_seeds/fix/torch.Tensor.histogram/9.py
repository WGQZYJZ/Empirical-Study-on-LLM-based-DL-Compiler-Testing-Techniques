'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.histogram\ntorch.Tensor.histogram(_input_tensor, input, bins, *, range=None, weight=None, density=False)\n'
import torch
input_tensor = torch.randn(1000, 2)
print(input_tensor.shape)
print(torch.Tensor.histogram(input_tensor, input=input_tensor, bins=10, range=((- 2), 2)))
'\nTask 4: Call the API torch.histc\ntorch.histc(input, bins=100, min=0, max=0, out=None)\n'
print(torch.histc(input_tensor, bins=10, min=(- 2), max=2))
'\nTask 5: Call the API torch.histc\ntorch.histc(input, bins=100, min=0, max=0, out=None)\n'
print(torch.histc(input_tensor, bins=10, min=(- 2), max=2))
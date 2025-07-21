'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.swapdims\ntorch.swapdims(input, dim0, dim1)\n'
import torch
input = torch.randn(2, 3, 5)
print(input)
print(input.size())
print(torch.swapdims(input, 0, 1))
print(torch.swapdims(input, 0, 1).size())
print(torch.swapdims(input, 1, 2))
print(torch.swapdims(input, 1, 2).size())
print(torch.swapdims(input, 2, 0))
print(torch.swapdims(input, 2, 0).size())
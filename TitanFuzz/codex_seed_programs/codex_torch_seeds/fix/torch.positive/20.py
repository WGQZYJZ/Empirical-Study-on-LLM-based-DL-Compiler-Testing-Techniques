'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.positive\ntorch.positive(input)\n'
import torch
input_data = torch.randn(1, 3)
print(torch.positive(input_data))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pow\ntorch.pow(input, exponent)\n'
import torch
input_data = torch.randn(1, 3)
print(torch.pow(input_data, 2))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.prod\ntorch.prod(input)\ntorch.prod(input, dim, keepdim=False, out=None) -> Tensor\n'
import torch
input_data = torch.randn(1, 3)
print(torch.prod(input_data))
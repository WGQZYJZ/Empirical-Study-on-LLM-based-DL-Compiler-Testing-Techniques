'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.tanh\ntorch.nn.functional.tanh(input)\n'
import torch
input = torch.randn(3, 5, requires_grad=True)
print(input)
output = torch.nn.functional.tanh(input)
print(output)
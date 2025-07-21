'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu_\ntorch.nn.functional.relu_(input)\n'
import torch
input = torch.randn(5, 5)
print('Input: \n', input)
relu_output = torch.nn.functional.relu_(input)
print('Relu Output: \n', relu_output)
relu_output = torch.nn.functional.relu_(input)
print('Relu Output: \n', relu_output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu_\ntorch.nn.functional.relu_(input)\n'
import torch
input = torch.randn(3, 3)
output = torch.nn.functional.relu_(input)
print(output)
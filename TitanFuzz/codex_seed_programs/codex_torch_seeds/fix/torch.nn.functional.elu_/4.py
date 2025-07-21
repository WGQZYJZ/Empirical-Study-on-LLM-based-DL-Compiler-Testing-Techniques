'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.elu_\ntorch.nn.functional.elu_(input, alpha=1.)\n'
import torch
input = torch.randn(1, 1, 3, 3)
print(torch.nn.functional.elu(input))
print(torch.nn.functional.elu_(input))
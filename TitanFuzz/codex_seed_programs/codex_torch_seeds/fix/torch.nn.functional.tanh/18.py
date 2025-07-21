'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.tanh\ntorch.nn.functional.tanh(input)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 3, 4, 4)
output = F.tanh(input)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch._assert\ntorch._assert(condition, message)\n'
import torch
input = torch.randn(3, 3)
torch._assert(input.is_floating_point(), 'input must be floating point')
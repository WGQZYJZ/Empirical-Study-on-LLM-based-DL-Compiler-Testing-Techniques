'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gelu\ntorch.nn.functional.gelu(input)\n'
import torch
import numpy as np
input = torch.randn(1, 2, 3)
print(input)
output = torch.nn.functional.gelu(input)
print(output)
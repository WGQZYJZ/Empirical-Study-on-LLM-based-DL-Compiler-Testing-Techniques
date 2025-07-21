'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.glu\ntorch.nn.functional.glu(input, dim=-1)\n'
import torch
import numpy as np
import torch
input = torch.randn(2, 3, 4)
output = torch.nn.functional.glu(input, dim=(- 1))
print(output)
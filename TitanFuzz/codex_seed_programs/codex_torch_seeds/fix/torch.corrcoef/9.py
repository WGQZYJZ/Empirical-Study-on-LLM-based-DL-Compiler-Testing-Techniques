'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.corrcoef\ntorch.corrcoef(input)\n'
import torch
import numpy as np
input = torch.rand(10, 10)
torch.corrcoef(input)
print(torch.corrcoef(input))
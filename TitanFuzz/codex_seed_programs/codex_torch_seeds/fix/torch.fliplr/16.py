'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fliplr\ntorch.fliplr(input)\n'
import torch
import numpy as np
input = torch.randn(2, 3, 5)
print(input)
output = torch.fliplr(input)
print(output)
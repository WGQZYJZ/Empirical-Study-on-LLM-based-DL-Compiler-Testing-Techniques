'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.random_split\n'
import torch
import numpy as np
input = torch.randn(5, 3)
print(input)
tensors = torch.utils.data.random_split(input, [4, 1])
print(tensors)
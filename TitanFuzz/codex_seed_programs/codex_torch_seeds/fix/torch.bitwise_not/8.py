'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_not\ntorch.bitwise_not(input, *, out=None)\n'
import torch
import numpy as np
input_data = torch.tensor([[0, 1], [1, 0], [1, 1], [0, 0]], dtype=torch.uint8)
print(input_data)
output = torch.bitwise_not(input_data)
print(output)
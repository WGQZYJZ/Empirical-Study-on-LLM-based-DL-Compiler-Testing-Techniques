'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.acosh\ntorch.acosh(input, *, out=None)\n'
import torch
import numpy as np
input_data = np.array([1, 2, 3, 4, 5])
input_data = torch.from_numpy(input_data)
output = torch.acosh(input_data)
print(output)
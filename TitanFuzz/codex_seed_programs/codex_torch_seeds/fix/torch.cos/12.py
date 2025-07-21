'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cos\ntorch.cos(input, *, out=None)\n'
import torch
import numpy as np
input = np.array([[0, (np.pi / 2), np.pi, ((3 * np.pi) / 2), (2 * np.pi)]])
input = torch.from_numpy(input)
output = torch.cos(input)
print(output)
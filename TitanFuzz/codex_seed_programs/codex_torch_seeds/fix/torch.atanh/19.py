'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atanh\ntorch.atanh(input, *, out=None)\n'
import torch
import numpy as np
input_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
input_data = torch.tensor(input_data)
output = torch.atanh(input_data)
print('PyTorch output: ', output)
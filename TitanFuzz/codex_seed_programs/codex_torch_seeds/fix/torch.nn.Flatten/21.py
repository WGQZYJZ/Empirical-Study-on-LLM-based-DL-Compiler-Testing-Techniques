'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Flatten\ntorch.nn.Flatten(start_dim=1, end_dim=-1)\n'
import torch
import numpy as np
import torch
input_data = np.array([[1, 2, 3], [4, 5, 6]])
input_data = torch.tensor(input_data)
print(input_data.shape)
flatten = torch.nn.Flatten(start_dim=1, end_dim=(- 1))
output = flatten(input_data)
print(output.shape)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_normal_\ntorch.nn.init.xavier_normal_(tensor, gain=1.0)\n'
import torch
import numpy as np
input_data = np.array([[1, 2, 3], [4, 5, 6]])
input_data = torch.from_numpy(input_data).float()
print(input_data)
torch.nn.init.xavier_normal_(input_data)
print(input_data)
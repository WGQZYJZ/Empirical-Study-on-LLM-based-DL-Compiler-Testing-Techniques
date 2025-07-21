'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_uniform_\ntorch.nn.init.xavier_uniform_(tensor, gain=1.0)\n'
import torch
import torch
import numpy as np
input_data = np.random.randn(5, 3)
input_data_tensor = torch.from_numpy(input_data).float()
torch.nn.init.xavier_uniform_(input_data_tensor, gain=1.0)
print(input_data_tensor)
torch.nn.init.xavier_uniform_(input_data_tensor, gain=0.5)
print(input_data_tensor)
torch.nn.init.xavier_uniform_(input_data_tensor, gain=2.0)
print(input_data_tensor)
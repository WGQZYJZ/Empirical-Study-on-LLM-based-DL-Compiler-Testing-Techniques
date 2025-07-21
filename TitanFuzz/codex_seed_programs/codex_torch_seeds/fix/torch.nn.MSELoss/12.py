"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MSELoss\ntorch.nn.MSELoss(size_average=None, reduce=None, reduction='mean')\n"
import torch
import numpy as np
input_data = torch.tensor(data=[[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float)
mse_loss = torch.nn.MSELoss()
loss = mse_loss(input_data, input_data)
print(loss)
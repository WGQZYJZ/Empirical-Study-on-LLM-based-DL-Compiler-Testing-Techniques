'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.HalfStorage\ntorch.HalfStorage(*args, **kwargs)\n'
import torch
data = [1.0, 2.0, 3.0, 4.0, 5.0]
half_data = torch.HalfStorage(data)
print('half_data = ', half_data)
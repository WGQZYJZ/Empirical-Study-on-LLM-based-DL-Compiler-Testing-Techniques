'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_uniform_\ntorch.nn.init.xavier_uniform_(tensor, gain=1.0)\n'
import torch
import numpy as np
x = np.random.randn(3, 5)
x = torch.from_numpy(x)
torch.nn.init.xavier_uniform_(x)
print(x)
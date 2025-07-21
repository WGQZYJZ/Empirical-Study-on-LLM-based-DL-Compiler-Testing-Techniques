'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.orthogonal_\ntorch.nn.init.orthogonal_(tensor, gain=1)\n'
import torch
import numpy as np
input_data = np.random.randn(2, 3)
tensor = torch.Tensor(input_data)
torch.nn.init.orthogonal_(tensor, gain=1)
print(tensor)
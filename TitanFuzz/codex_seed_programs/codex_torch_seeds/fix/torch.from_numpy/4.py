'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.from_numpy\ntorch.from_numpy(ndarray)\n'
import torch
import numpy as np
a = np.arange(12).reshape(3, 4)
torch.from_numpy(a)
torch.tensor(a)
torch.as_tensor(a)
torch.as_tensor(a, dtype=torch.float)
torch.from_numpy(a)
torch.from_numpy(a).dtype
torch.from_numpy(a).dtype
torch.from_numpy(a).device
torch
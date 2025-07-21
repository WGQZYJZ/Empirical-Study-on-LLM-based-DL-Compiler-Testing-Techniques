'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.overrides.is_tensor_like\ntorch.overrides.is_tensor_like(inp)\n'
import torch
import numpy as np
inp = np.array([[1, 2, 3], [4, 5, 6]])
torch.overrides.is_tensor_like(inp)
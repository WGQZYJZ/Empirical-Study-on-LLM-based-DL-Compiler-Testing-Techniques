'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
import numpy as np
import torch
np.random.seed(42)
x = np.random.rand(100, 1)
y = ((1 + (2 * x)) + (0.1 * np.random.randn(100, 1)))
torch.utils.data.TensorDataset(torch.from_numpy(x), torch.from_numpy(y))
np.random.seed(42)
x = np.random.rand(100, 1)
y = ((1 + (2 * x)) + (0.1 * np.random.randn(100, 1)))
torch.utils.data.TensorDataset(torch.from_numpy(x), torch.from_numpy(y))
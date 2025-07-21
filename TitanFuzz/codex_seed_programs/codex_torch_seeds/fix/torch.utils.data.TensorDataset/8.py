'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
import numpy as np
x = np.random.rand(100, 3)
y = np.random.randint(0, 2, (100,))
dataset = torch.utils.data.TensorDataset(torch.from_numpy(x), torch.from_numpy(y))
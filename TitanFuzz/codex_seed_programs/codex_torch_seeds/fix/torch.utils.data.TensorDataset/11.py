'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(*tensors)\n'
import torch
import numpy as np
x = torch.randn(100, 3)
y = torch.randn(100, 2)
dataset = torch.utils.data.TensorDataset(x, y)
print(dataset[0])
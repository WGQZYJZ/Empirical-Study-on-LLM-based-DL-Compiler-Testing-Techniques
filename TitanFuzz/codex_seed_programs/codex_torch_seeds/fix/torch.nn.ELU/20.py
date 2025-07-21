'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ELU\ntorch.nn.ELU(alpha=1.0, inplace=False)\n'
import torch
import numpy as np
np.random.seed(42)
x = np.random.randn(100, 20)
y = np.random.randn(100, 20)
elu = torch.nn.ELU()
x_tensor = torch.tensor(x, dtype=torch.float)
y_tensor = torch.tensor(y, dtype=torch.float)
print(elu(x_tensor))
print(elu(y_tensor))
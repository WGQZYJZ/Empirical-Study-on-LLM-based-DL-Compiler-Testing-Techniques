'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.selu\ntorch.nn.functional.selu(input, inplace=False)\n'
import torch
import numpy as np
x_data = np.random.randn(2, 3)
x = torch.tensor(x_data, dtype=torch.float)
y = torch.nn.functional.selu(x)
print(y)
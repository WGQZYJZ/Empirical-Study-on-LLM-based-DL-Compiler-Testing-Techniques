'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.matrix_exp\ntorch.matrix_exp(input)\n'
import torch
import numpy as np
data = np.random.rand(3, 3)
data = torch.from_numpy(data)
print(data)
print(torch.matrix_exp(data))
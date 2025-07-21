'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SELU\ntorch.nn.SELU(inplace=False)\n'
import torch
import numpy as np
x = torch.tensor(np.random.rand(1, 2, 3, 4), dtype=torch.float32)
selu = torch.nn.SELU(inplace=False)
y = selu(x)
print('The input tensor: ', x)
print('The output tensor: ', y)
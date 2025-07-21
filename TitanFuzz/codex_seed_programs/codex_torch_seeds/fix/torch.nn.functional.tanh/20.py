'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.tanh\ntorch.nn.functional.tanh(input)\n'
import torch
import numpy as np
x = torch.tensor(np.random.rand(4, 4))
print(x)
y = torch.nn.functional.tanh(x)
print(y)
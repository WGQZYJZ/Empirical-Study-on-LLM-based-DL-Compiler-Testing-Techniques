'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.tanh\ntorch.nn.functional.tanh(input)\n'
import torch
import numpy as np
x = torch.tensor(np.random.rand(1, 10, 10), dtype=torch.float32)
y = torch.nn.functional.tanh(x)
print(y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.manual_seed\ntorch.random.manual_seed(seed)\n'
import torch
import numpy as np
torch.random.manual_seed(10)
x = torch.randn(4, 4)
print(x)
torch.random.manual_seed(10)
y = torch.randn(4, 4)
print(y)
print(np.allclose(x.numpy(), y.numpy()))
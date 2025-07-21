'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.seed\ntorch.random.seed()\n'
import torch
import numpy as np
x = np.random.rand(10)
x_tensor = torch.tensor(x)
torch.random.seed()
torch.cuda.manual_seed(0)
torch.cuda.manual_seed_all(0)
print(x_tensor)
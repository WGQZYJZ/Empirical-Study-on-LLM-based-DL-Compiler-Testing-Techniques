'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.use_deterministic_algorithms\ntorch.use_deterministic_algorithms(mode)\n'
import torch
import numpy as np
a = torch.rand(2, 2)
b = torch.rand(2, 2)
torch.use_deterministic_algorithms(mode=True)
c = (a + b)
print(c)
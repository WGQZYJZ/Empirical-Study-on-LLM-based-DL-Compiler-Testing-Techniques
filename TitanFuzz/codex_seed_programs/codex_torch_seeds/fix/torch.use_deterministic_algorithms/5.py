'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.use_deterministic_algorithms\ntorch.use_deterministic_algorithms(mode)\n'
import torch
import numpy as np
np.random.seed(0)
torch.use_deterministic_algorithms(mode=True)
input_data = torch.rand(size=(2, 3), dtype=torch.float32, device='cpu')
print(input_data)
torch.use_deterministic_algorithms(mode=True)
tensor = torch.rand(size=(2, 3), dtype=torch.float32, device='cpu')
print(tensor)
tensor = torch.rand(size=(2, 3), dtype=torch.float32, device='cpu')
print(tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.use_deterministic_algorithms\ntorch.use_deterministic_algorithms(mode)\n'
import torch
import numpy as np
import torch
input_data = torch.rand(2, 2)
torch.use_deterministic_algorithms(mode=True)
print(input_data)
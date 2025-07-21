'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.use_deterministic_algorithms\ntorch.use_deterministic_algorithms(mode)\n'
import torch
import numpy as np
input_data = torch.rand(3, 3)
print('Input data: ', input_data)
torch.use_deterministic_algorithms(mode=True)
output_data = torch.rand(3, 3)
print('Output data: ', output_data)
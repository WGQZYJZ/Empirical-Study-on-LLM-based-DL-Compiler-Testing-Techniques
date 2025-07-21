'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.are_deterministic_algorithms_enabled\ntorch.are_deterministic_algorithms_enabled()\n'
import torch
import numpy as np
input_data = np.random.randint(0, 10, size=(4, 4))
print('Input data: ', input_data)
print('Are deterministic algorithms enabled? ', torch.are_deterministic_algorithms_enabled())
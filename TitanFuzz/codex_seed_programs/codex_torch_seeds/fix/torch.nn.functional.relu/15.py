'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu\ntorch.nn.functional.relu(input, inplace=False)\n'
import torch
import numpy as np
input_data = torch.tensor(np.random.random((2, 3)), dtype=torch.float32)
print('Input data:', input_data)
output = torch.nn.functional.relu(input_data)
print('Output data:', output)
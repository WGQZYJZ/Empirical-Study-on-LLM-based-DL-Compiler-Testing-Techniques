'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.use_deterministic_algorithms\ntorch.use_deterministic_algorithms(mode)\n'
import torch
import numpy as np
input_data = np.random.rand(100, 100)
input_data = torch.tensor(input_data, dtype=torch.float32)
torch.use_deterministic_algorithms(mode=True)
output = torch.sigmoid(input_data)
print(output)
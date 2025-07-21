'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.histc\ntorch.Tensor.histc(_input_tensor, bins=100, min=0, max=0)\n'
import torch
import numpy as np
input_tensor = np.random.randint(0, 100, size=100)
input_tensor = torch.from_numpy(input_tensor)
output_tensor = torch.Tensor.histc(input_tensor, bins=100, min=0, max=0)
print(output_tensor)
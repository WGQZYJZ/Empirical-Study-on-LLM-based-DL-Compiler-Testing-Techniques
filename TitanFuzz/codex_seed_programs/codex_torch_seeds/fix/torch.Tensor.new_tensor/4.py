'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_tensor\ntorch.Tensor.new_tensor(_input_tensor, data, dtype=None, device=None, requires_grad=False)\n'
import torch
import numpy as np
input_data = np.array([[1, 2, 3], [4, 5, 6]])
print(input_data)
output_tensor = torch.Tensor.new_tensor(input_data, dtype=torch.float32)
print(output_tensor)
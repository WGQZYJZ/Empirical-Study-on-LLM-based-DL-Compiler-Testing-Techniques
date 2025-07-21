'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_meta\ntorch.Tensor.is_meta(_input_tensor, )\n'
import torch
import numpy as np
input_data = np.array([[1, 2, 3], [4, 5, 6]])
input_tensor = torch.tensor(input_data)
output_tensor = torch.Tensor.is_meta(input_tensor)
print(output_tensor)
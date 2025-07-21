'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_full\ntorch.Tensor.new_full(_input_tensor, size, fill_value, dtype=None, device=None, requires_grad=False)\n'
import torch
import numpy as np
input_data = np.array([[1, 2, 3], [4, 5, 6]])
input_data = torch.from_numpy(input_data)
print(input_data)
output = torch.Tensor.new_full(input_data, size=(2, 3), fill_value=1)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.deg2rad\ntorch.Tensor.deg2rad(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
print('input_tensor = ', input_tensor)
output_tensor = input_tensor.deg2rad()
print('output_tensor = ', output_tensor)
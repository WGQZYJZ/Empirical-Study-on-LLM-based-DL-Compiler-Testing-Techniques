'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumprod_\ntorch.Tensor.cumprod_(_input_tensor, dim, dtype=None)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
print('Input Tensor: ', input_tensor)
output_tensor = input_tensor.cumprod_(dim=0, dtype=torch.float)
print('Output Tensor: ', output_tensor)
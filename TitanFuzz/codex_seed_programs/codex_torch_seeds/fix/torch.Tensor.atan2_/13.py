'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.atan2_\ntorch.Tensor.atan2_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
other = torch.tensor([[2.0, 1.0], [4.0, 3.0]])
output_tensor = input_tensor.atan2_(other)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)